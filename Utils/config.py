import toml
import os

config_file = "Settings.toml"

def check_config():
    default_config = {}

    if not os.path.exists(config_file):
        default_config = {
            "Paths": {
                "backgroundPaths": ["Assets/Fuji.mp4"],
                "musicPaths": ["Assets/1.mp3", "Assets/2.mp3", "Assets/3.mp3", "Assets/4.mp3", "Assets/5.mp3", "Assets/6.mp3", "Assets/7.mp3", "Assets/8.mp3"],
                "outputPath": "Output",
                "memesPath": "Assets/Memes",
                "imgurPath": "Assets/Memes/Imgur",
                "redditPath": "Assets/Memes/Reddit"
            },
            "Settings": {
                "clipFps": 60,
                "clipDuration": 4
            },
            "Display": {
                "paddingTop": 100,
                "paddingBottom": 100,
                "paddingSide": 50
            },
            "Scraping": {
                "Imgur": {
                    "Authorization": "key-here"
                },
                "Reddit": {
                    "Id": "id-here",
                    "Secret": "secret-here",
                    "userAgent": "Serialized's Cloud Tool",
                    "TimeSpan": "Day"
                }
            },
            "AutoPosting": {
                "Credentials": 'path-here',
                "YouTube-Api-Version": "v3",
                "YouTube-Api-Service-Name": "youtube",
                "subReddits": ["memes", "dankmemes"],
                "shortsAmount": 5
            }
        }

        with open(config_file, "w") as f:
            f.write(toml.dumps(default_config))
        
check_config()
config_contents = toml.load(config_file)

background_paths = config_contents["Paths"]["backgroundPaths"]
music_paths = config_contents["Paths"]["musicPaths"]
output_path = config_contents["Paths"]["outputPath"]
memes_path = config_contents["Paths"]["memesPath"]
imgur_path = config_contents["Paths"]["imgurPath"]
reddit_path = config_contents["Paths"]["redditPath"]
clip_fps = config_contents["Settings"]["clipFps"]
clip_duration = config_contents["Settings"]["clipDuration"]
padding_top = config_contents["Display"]["paddingTop"]
padding_bottom = config_contents["Display"]["paddingBottom"]
padding_side = config_contents["Display"]["paddingSide"]
imgur_auth = config_contents["Scraping"]["Imgur"]["Authorization"]
reddit_id = config_contents["Scraping"]["Reddit"]["Id"]
reddit_secret = config_contents["Scraping"]["Reddit"]["Secret"]
reddit_time_span = config_contents["Scraping"]["Reddit"]["TimeSpan"]
reddit_user_agent = config_contents["Scraping"]["Reddit"]["userAgent"]
autopost_credentials = config_contents["AutoPosting"]["Credentials"]
youtube_api_version = config_contents["AutoPosting"]["YouTube-Api-Version"]
youtube_api_service_name = config_contents["AutoPosting"]["YouTube-Api-Service-Name"]
subreddits = config_contents["AutoPosting"]["subReddits"]
shorts_amount = config_contents["AutoPosting"]["shortsAmount"]


        