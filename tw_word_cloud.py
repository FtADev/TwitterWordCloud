import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from dotenv import load_dotenv
from twython import Twython
from wordcloud import STOPWORDS as EN_STOPWORDS
from persian_wordcloud.wordcloud import PersianWordCloud, add_stop_words

load_dotenv()
APP_KEY = os.getenv('APP_KEY')
APP_SECRET = os.getenv('APP_SECRET')
USERNAME = os.getenv('APP_USERNAME')

# Connect to Twitter
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
words = raw_string.split(" ")

words = [w for w in words if len(w) > 2]  # ignore a, an, be, ...
words = [w.lower() for w in words]
words = [w for w in words if w not in EN_STOPWORDS]

mask = np.array(Image.open('./github.png'))

clean_string = ','.join(words)
word_cloud = PersianWordCloud(
    only_persian=True,
    max_words=100,
    mask=mask,
    margin=0,
    width=800,
    height=800,
    min_font_size=1,
    max_font_size=500,
    background_color="White"
).generate(clean_string)

f = plt.figure(figsize=(50,50))
f.add_subplot(1,2, 1)
plt.imshow(mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.title('Original Stencil', size=40)
plt.axis("off")

f.add_subplot(1,2, 2)
plt.imshow(word_cloud, interpolation='bilinear')
plt.title('Twitter Generated Cloud', size=40)
plt.axis("off")
plt.show()
