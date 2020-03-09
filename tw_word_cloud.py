from functions import *


def main():
    font_path = './fonts/Blabeloo.ttf'
    max_word = 500
    image_path = './twitter.jpg'

    twitter = connect_twitter()
    timeline = get_user_timeline(twitter)
    raw_tweets = get_tweets(timeline)
    words = clean_tweets(raw_tweets)
    mask = get_image(image_path)
    word_cloud = create_word_cloud(font_path,
                                   max_word,
                                   mask,
                                   words
                                   )
    show_image(word_cloud)
    save_image(word_cloud)


if __name__ == "__main__":
    main()
