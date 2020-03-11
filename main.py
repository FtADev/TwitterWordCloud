from functions import *


def main():
    twitter = connect_twitter()
    timeline = get_user_timeline(twitter)
    raw_tweets = get_tweets(timeline)
    words = clean_tweets(raw_tweets)
    word_cloud = create_word_cloud(words)
    change_color(word_cloud)
    show_image(word_cloud)
    save_image(word_cloud)


if __name__ == "__main__":
    main()
