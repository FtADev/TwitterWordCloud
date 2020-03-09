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


load_dotenv()
APP_KEY = os.getenv('APP_KEY')
APP_SECRET = os.getenv('APP_SECRET')
USERNAME = os.getenv('APP_USERNAME')

twitter = Twython(APP_KEY, APP_SECRET)

user_timeline = twitter.get_user_timeline(screen_name=USERNAME, count=1)

last_id = user_timeline[0]['id'] - 1
for i in range(16):
    batch = twitter.get_user_timeline(screen_name=USERNAME, count=200, max_id=last_id)
    user_timeline.extend(batch)
    last_id = user_timeline[-1]['id'] - 1

raw_tweets = []

for tweets in user_timeline:
    raw_tweets.append(tweets['text'])

raw_string = ''.join(raw_tweets)
no_links = re.sub(r'http\S+', '', raw_string)
no_mention = re.sub(r'@\w*', '', no_links)
no_hashtag = re.sub(r'#\w*', '', no_mention)
words = no_hashtag.split(" ")

stops = codecs.open('persian_stopword', encoding='utf-8').read().split('\n')
words = [w for w in words if len(w) > 2]  # ignore a, an, be, ...
words = [w.lower() for w in words]
words = [w for w in words if w not in EN_STOPWORDS]
words = [w.replace('rt', '') for w in words]
words = [w for w in words if w not in stops]

mask = np.array(Image.open('./twitter.jpg'))

clean_string = ','.join(words)
word_cloud = WordCloud(
    font_path='./fonts/Blabeloo.ttf',
    max_words=500,
    mask=mask,
    margin=0,
    width=800,
    height=800,
    min_font_size=1,
    max_font_size=500,
    background_color="White"
).generate(clean_string)

word_cloud.recolor(color_func=grey_color_func, random_state=3)

plt.figure(figsize=(10, 10))
plt.imshow(word_cloud, interpolation="bilinear")
plt.show()
word_cloud.to_file("my_word_cloud.png")
