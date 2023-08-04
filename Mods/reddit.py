import praw
import os
import requests
from Utils import config, logger
import main as main
import random


# Initialize the needed variables.
reddit_id = config.reddit_id
reddit_secret = config.reddit_secret
reddit_user_agent = config.reddit_user_agent
time_span = config.reddit_time_span
sub_reddits = config.subreddits


def reddit_menu():
    # Clear screen and print main logo.
    os.system("cls")
    logger.print_logo()

    print(
        f" {logger.Colors.magenta}[{logger.Colors.white}~{logger.Colors.magenta}]{logger.Colors.white} Reddit Subreddit to Scrape"
    )
    print(
        f" {logger.Colors.magenta}[{logger.Colors.white}>{logger.Colors.magenta}]{logger.Colors.white} ",
        end="",
    )
    subreddit_name = input()

    # Setup the Reddit API Client.
    reddit = praw.Reddit(
        client_id=reddit_id, client_secret=reddit_secret, user_agent=reddit_user_agent
    )

    # Fetch the top posts from the subreddit.
    sub_reddit = reddit.subreddit(subreddit_name)
    top_posts = sub_reddit.top(time_filter=time_span.lower(), limit=100)

    reddit_path = (
        config.memes_path
    )  # Scraped images go directly to the memes directory.

    for i, post in enumerate(top_posts):
        if post.is_self or not post.url.endswith((".png", ".jpg", ".jpeg", ".webp")):
            continue  # Skip non-static media

        resp = requests.get(post.url)

        if resp.status_code == 200:
            meme_content = resp.content
            meme_guid = post.id
            upvotes = post.ups
            meme_file_name = f"{reddit_path}/{meme_guid}-{upvotes}.jpg"
            with open(meme_file_name, "wb") as file:
                file.write(meme_content)
            logger.prefix_stats(
                f"Downloaded image: {meme_guid} with {upvotes} upvotes."
            )

    logger.prefix_stats(
        f"Finished downloading images from {subreddit_name}. Press any key to return."
    )
    input()
    main.main()


def auto_reddit():
    os.system("cls")
    logger.print_art()
    subreddit_name = random.choice(sub_reddits)

    # Setup the Reddit API Client.
    reddit = praw.Reddit(
        client_id=reddit_id, client_secret=reddit_secret, user_agent=reddit_user_agent
    )

    # Fetch the top posts from the subreddit.
    sub_reddit = reddit.subreddit(subreddit_name)
    top_posts = sub_reddit.top(time_filter=time_span.lower(), limit=50)

    reddit_path = (
        config.memes_path
    )  # Scraped images go directly to the memes directory.

    for i, post in enumerate(top_posts):
        if (
            post.is_self
            or not post.url.endswith((".png", ".jpg", ".jpeg", ".webp"))
            or post.over_18
        ):
            continue  # Skip non-static media

        resp = requests.get(post.url)

        if resp.status_code == 200:
            meme_content = resp.content
            meme_guid = post.id
            upvotes = post.ups
            meme_file_name = f"{reddit_path}/{meme_guid}-{upvotes}.jpg"
            with open(meme_file_name, "wb") as file:
                file.write(meme_content)
            logger.prefix_stats(
                f"Downloaded image: {meme_guid} with {upvotes} upvotes."
            )
