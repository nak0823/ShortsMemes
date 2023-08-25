import os
import random
import time
import uuid
from moviepy.editor import *

import Mods.title as title
import Utils.config as config
import Utils.logger as logger
import main as main

compiled_videos = []


def compile(is_auto):
    os.system("cls")
    logger.print_logo()

    # Initialize variables from the config.
    background_paths = config.background_paths
    music_paths = config.music_paths
    output_path = config.output_path
    memes_path = config.memes_path
    output_path = config.output_path
    clip_fps = config.clip_fps
    clip_duration = config.clip_duration
    padding_top = config.padding_top
    padding_bottom = config.padding_bottom
    padding_side = config.padding_side

    # Create the needed output directories
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    if not os.path.exists(memes_path):
        os.makedirs(memes_path)

    # Gather the memes from memes directory.
    memes_to_use = [os.path.join(memes_path, meme) for meme in os.listdir(memes_path)]
    amount_to_make = len(memes_to_use) // 2

    # Print a summarization of the current settings.
    logger.prefix_stats(f"Shorts Fps: {logger.Colors.cyan}{clip_fps}")
    logger.prefix_stats(f"Shorts Duration: {logger.Colors.cyan}{clip_duration} sec")
    logger.prefix_stats(
        f"Starting Compiling {logger.Colors.cyan}{amount_to_make}{logger.Colors.white} Shorts"
    )
    print()

    for i in range(amount_to_make):
        # Time variable to calculate the time of creation.
        start_time = time.time()

        # Set the background by choosing a random background from Assets.
        short = VideoFileClip(random.choice(background_paths))

        # Pick 2 random memes and remove them from the memes list.
        random_memes = random.sample(memes_to_use, 2)
        memes_to_use.remove(random_memes[0])
        memes_to_use.remove(random_memes[1])

        # Load the memes in as ImageClips.
        top_meme = ImageClip(random_memes[0])
        bottom_meme = ImageClip(random_memes[1])

        # Calculate the target dimensions.
        target_height = (short.size[1] - 2 * padding_top - 2 * padding_top) // 2
        target_width = short.size[0] - (2 * padding_side)

        # Resize the memes if necessary.
        top_meme = top_meme.resize(height=target_height)
        if top_meme.size[0] > target_width:
            top_meme = top_meme.resize(width=target_width)

        bottom_meme = bottom_meme.resize(height=target_height)
        if bottom_meme.size[0] > target_width:
            bottom_meme = bottom_meme.resize(width=target_width)

        top_meme_pos = (
            short.size[0] // 2 - top_meme.size[0] // 2,
            padding_top + target_height // 2 - top_meme.size[1] // 2,
        )

        bottom_meme_pos = (
            short.size[0] // 2 - bottom_meme.size[0] // 2,
            short.size[1]
            - padding_bottom
            - target_height // 2
            - bottom_meme.size[1] // 2,
        )

        # Set the memes position and duration.
        top_meme = top_meme.set_position(top_meme_pos).set_duration(clip_duration)
        bottom_meme = bottom_meme.set_position(bottom_meme_pos).set_duration(
            clip_duration
        )

        # Set a random audio under the video. (Note: Audios are precompiled to be the same length as the duration).
        comp = CompositeVideoClip(
            [short.subclip(0, clip_duration), top_meme, bottom_meme]
        )
        comp = comp.set_audio(AudioFileClip(random.choice(music_paths)))

        # Random file name to avoid duplicates.
        random_uuid = uuid.uuid4().hex
        save_position = f"{output_path}/{title.title_maker()}.mp4"

        # Write the final composition to a mp4.
        comp.write_videofile(
            save_position,
            fps=clip_fps,
            codec="libx264",
            audio_codec="aac",
            threads=4,
            logger=None,
        )
        compiled_videos.append(save_position)

        end_time = time.time()
        elapsed_time = round(end_time - start_time, 2)

        os.remove(random_memes[0])
        os.remove(random_memes[1])

        logger.prefix_stats(
            f"Finished Writing Short # {logger.Colors.cyan}{i + 1}{logger.Colors.white}. Time Taken: {logger.Colors.cyan}{elapsed_time}"
        )
        logger.console_title(
            f"Multi Functional Shorts Tool by Serialized - Creating Shorts {i}/{amount_to_make}"
        )

    if not is_auto:
        logger.prefix_stats(f"Finished Writing All Shorts. Press any key to return")
        input()
        main.main()
