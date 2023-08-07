import toml
import os
import sys

import Mods.compiler as compiler
import Mods.imgur as imgur
import Mods.reddit as reddit
import Utils.config as config
import Utils.logger as logger
import Auto.auto as auto

def main():
    # Clears the terminal
    os.system('cls')

    # Checks if a config file exists, if not it creates 
    # a new config file with default values and initializes the variables.
    config.check_config()
    
    # Prints the beautiful ascii art
    logger.print_logo()
    logger.print_menu()
    logger.console_title("ShortsMemes | Generate Meme Shorts | By Serialized - fixed by xFlippy")

    user_input = int(input())

    match (user_input):
        case 1:
         compiler.compile(False)
        case 2:
         reddit.reddit_menu()
        case 3:
         imgur.imgur_menu()
        case 4:
         auto.run()
         
        case _:
            main()

if __name__ == '__main__':
  main()
        




