import re
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from dotenv import load_dotenv
from twython import Twython
from wordcloud import WordCloud, STOPWORDS as EN_STOPWORDS
from collections import Counter
import random
import codecs


def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    # Colors HSL: hsl(A, B%, C%) means: "hsl(A, B%%, %d%%)" % random.randint(C, 100)
    return "hsl(208, 59%%, %d%%)" % random.randint(14, 100)


def change_color(word_cloud):
    word_cloud.recolor(color_func=grey_color_func, random_state=3)


def connect_with_dev_acc():
    load_dotenv()
    APP_KEY = os.getenv('APP_KEY')
    APP_SECRET = os.getenv('APP_SECRET')
    return Twython(APP_KEY, APP_SECRET)


def connect_without_dev_acc():
    print('haha')


def account_switcher(argument):
    switcher = {
        "y": connect_with_dev_acc(),
        "n": connect_without_dev_acc(),
    }
    func = switcher.get(argument, lambda: "Invalid answer")
    return func()


def connect_twitter():
    have_dev_account = raw_input("Do you have a developer twitter account?[y/n] ")
    account_switcher(have_dev_account)


def get_user_timeline(twitter):
    username = os.getenv('APP_USERNAME')
    user_timeline = twitter.get_user_timeline(screen_name=username, count=1)
    last_id = user_timeline[0]['id'] - 1
    for i in range(16):
        batch = twitter.get_user_timeline(screen_name=username, count=200, max_id=last_id)
        user_timeline.extend(batch)
        last_id = user_timeline[-1]['id'] - 1
    return user_timeline


def get_tweets(user_timeline):
    raw_tweets = []
    for tweets in user_timeline:
        raw_tweets.append(tweets['text'])
    return raw_tweets


def remove_links(raw_string):
    return re.sub(r'http\S+', '', raw_string)


def remove_mentions(raw_string):
    return re.sub(r'@\w*', '', raw_string)


def remove_others(word_list):
    return [w.replace('RT', '') for w in word_list]


def remove_stop_words(word_list):
    stops = codecs.open('persian_stopword', encoding='utf-8').read().split('\n')
    words = [w for w in word_list if w not in stops]
    words = [w for w in words if w not in EN_STOPWORDS]
    return words


def remove_hashtags(raw_string):
    return re.sub(r'#\w*', '', raw_string)


def create_word_cloud(font_path, max_word, mask, words):
    return WordCloud(
        font_path=font_path,
        max_words=max_word,
        mask=mask,
        margin=0,
        width=800,
        height=800,
        min_font_size=1,
        max_font_size=500,
        background_color="White"
    ).generate(words)


def get_image(image_path):
    return np.array(Image.open(image_path))


def get_font():
    print(a)


def save_image(word_cloud):
    word_cloud.to_file("my_word_cloud.png")


def show_image(word_cloud):
    plt.figure(figsize=(10, 10))
    plt.imshow(word_cloud, interpolation="bilinear")
    plt.show()


def remove_emoji(raw_string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u'\U00010000-\U0010ffff'
                               u"\u200d"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\u3030"
                               u"\ufe0f"
                               u"\u2069"
                               u"\u2066"
                               u"\u2068"
                               u"\u2067"
                               "]+", flags=re.UNICODE)

    return emoji_pattern.sub(r'', raw_string)


def clean_tweets(raw_tweets):
    raw_string = ''.join(raw_tweets)
    raw_string = remove_links(raw_string)
    raw_string = remove_mentions(raw_string)
    raw_string = remove_hashtags(raw_string)
    raw_string = remove_emoji(raw_string)
    words = raw_string.split(" ")
    words = remove_others(words)
    words = remove_stop_words(words)
    return ','.join(words)


def get_username():
    print(a)

# words = [w for w in words if len(w) > 2]  # ignore a, an, be, ...
# words = [w.lower() for w in words]
