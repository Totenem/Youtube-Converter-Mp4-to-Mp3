import os
from pytube import YouTube

def download_youtube_video(video_url, output_folder):
    try: 
        # Create output folder if it its not there
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Download the video
        yt = YouTube(video_url)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(output_folder)
        
        # Rename the downloaded file
        default_filename = stream.default_filename
        title = yt.title
        new_filename = f"{title}.mp3"
        os.rename(os.path.join(output_folder, default_filename), os.path.join(output_folder, new_filename))

        print(f"Downloaded and converted {video_url} successfully.")
        
    except Exception as ex:
        print(f"An error occurred: {ex}")

if __name__ == "__main__":
    video_url = input("Enter the Link of the YouTube video: ")
    output_folder = input("Enter the output folder path (not name): ")
    download_youtube_video(video_url, output_folder)
