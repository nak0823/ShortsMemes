import os
import requests
import uuid
from Utils import config, logger
import main as main


def imgur_menu():
    # Clear screen and print main logo.
    os.system("cls")
    logger.print_art()

    # Initialize the needed variables.
    imgur_auth = config.imgur_auth
    imgur_path = config.memes_path  # Scraped images go directly to the memes directory.

    print(
        f" {logger.Colors.magenta}[{logger.Colors.white}~{logger.Colors.magenta}]{logger.Colors.white} Imgur Gallery to Scrape"
    )
    print(
        f" {logger.Colors.magenta}[{logger.Colors.white}>{logger.Colors.magenta}]{logger.Colors.white} ",
        end="",
    )
    gallery_to_scrape = input()
    gallery_to_scrape = gallery_to_scrape.split("/")[-1]

    fetch_api = f"https://api.imgur.com/3/gallery/{gallery_to_scrape}/images"
    headers = {"Authorization": f"Client-ID {imgur_auth}"}
    resp = requests.get(fetch_api, headers=headers)

    if resp.status_code == 200:
        data = resp.json()
        images = data["data"]

        if not images:
            logger.prefix_stats(f"Gallery is empty. Press any key to return")
            input()
            main.main()

        if not os.path.exists(imgur_path):
            os.makedirs(imgur_path)

        for i, image in enumerate(images, 1):
            image_url = image["link"]
            image_resp = requests.get(image_url)

            if image_resp.status_code == 200:
                ext = os.path.splitext(image_url)[1]
                guid = uuid.uuid4().hex
                file_name = f"{guid}{ext}"
                image_path = os.path.join(imgur_path, file_name)

                with open(image_path, "wb") as image_file:
                    image_file.write(image_resp.content)
                logger.prefix_stats(f"Downloaded image: {guid}.")

        logger.prefix_stats(
            f"Finished downloading the gallery. Press any key to return."
        )
        input()
        main.main()
    else:
        logger.prefix_stats(f"Invalid Authorization key. Press any key to return.")
        input()
        main.main()
