from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

from Utils import config, logger
from Mods import compiler as Compiler
from Mods import title as Title

credentials_path = config.autopost_credentials
youtube_api_service_name = config.youtube_api_service_name
youtube_api_version = config.youtube_api_version
upload_scope = ['https://www.googleapis.com/auth/youtube.upload']
description = "#memes #viral #funny"


def get_auth_service():
    """Authenticate the user and return the YouTube Data API service."""
    flow = InstalledAppFlow.from_client_secrets_file(credentials_path, upload_scope)
    credentials = flow.run_local_server()
    return build(youtube_api_service_name, youtube_api_version, credentials=credentials)


def upload_video(youtube, video_path, title, description, privacy_status='public'):
    try:
        body = {
            'snippet': {
                'title': title,
                'description': description,
                'tags': [],  # Add any tags you want for the video
                'categoryId': '23',  # Change the category ID if needed (see YouTube API documentation) (Memes = 23)
            },
            'status': {
                'privacyStatus': privacy_status,
            }
        }

        media = MediaFileUpload(video_path)

        video_resp = youtube.videos().insert(
            part='snippet,status',
            body=body,
            media_body=media
        ).execute()

        logger.prefix_stats(f"Video '{title}' uploaded successfully! Video ID: {video_resp['id']}")
    except HttpError as e:
        logger.prefix_stats(f"An HTTP error occurred: {e}")
    except Exception as e:
        logger.prefix_stats(f"An error occurred: {e}")


def auto_upload():
    youtube_service = get_auth_service()
    for video in range(len(Compiler.compiled_videos)):
        title = Title.title_maker()
        upload_video(youtube_service, Compiler.compiled_videos[video], title, description)
