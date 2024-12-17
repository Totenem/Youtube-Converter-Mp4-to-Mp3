from pathlib import Path
import os
import sys
import yt_dlp
from tkinter import Tk, Canvas, Entry, Button, messagebox, Label, filedialog

# Set the output path and assets path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets")

def relative_to_assets(path: str) -> Path:
    if getattr(sys, 'frozen', False):
        # If the application is running as a bundled executable
        base_path = sys._MEIPASS
    else:
        # If the application is running in a normal Python environment
        base_path = ASSETS_PATH
    return Path(base_path) / Path(path)

def download_youtube_video(video_url, output_folder):
    try: 
        # Create output folder if it is not there
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Set options for yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),  # Output file template
        }

        # Show loading message
        loading_label.config(text="Downloading... Please wait.", fg="blue")
        loading_label.place(x=100, y=325)  # Position the loading label
        window.update_idletasks()  # Update the GUI

        # Download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        print(f"Downloaded and converted {video_url} successfully.")
        messagebox.showinfo("Conversion Successful", "The conversion process has been completed successfully!")
        
    except Exception as ex:
        print(f"An error occurred: {ex}")
        messagebox.showerror("Error", f"An error occurred: {ex}")
    finally:
        # Hide loading message
        loading_label.place_forget()  # Hide the loading label

def download_button_clicked():
    video_url = entry_1.get()
    output_folder = entry_output_path.get()  # Get the output folder from the input field
    
    if not output_folder:
        # If no output folder is specified, default to Downloads
        output_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    
    # Disable the download button while processing
    download_button.config(state="disabled")
    download_youtube_video(video_url, output_folder)
    download_button.config(state="normal")  

def browse_output_folder():
    folder_selected = filedialog.askdirectory() 
    if folder_selected:
        entry_output_path.delete(0, 'end') 
        entry_output_path.insert(0, folder_selected)  


window = Tk()
window.geometry("700x400") 
window.configure(bg="#FA7070")
canvas = Canvas(
    window,
    bg="#FA7070",
    height=400,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

title_label = Label(
    window,
    text="MP4 TO MP3 YOUTUBE CONVERTER BY TOTEMN",
    bg="#FA7070",
    fg="#000000",
    font=("JetBrainsMonoRoman", 16)
)
title_label.place(x=100, y=13)

entry_1 = Entry(
    window,
    bd=2,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=1,
    font=("JetBrainsMonoRoman", 14)
)
entry_1.place(x=109.0, y=113.0, width=482.0, height=45.0
)

input_label = Label(
    window,
    text="Enter YouTube Link:",
    bg="#FA7070",
    fg="#FEFDED",
    font=("JetBrainsMonoRoman", 14)
)
input_label.place(x=96.0, y=92.0)

entry_output_path = Entry(
    window,
    bd=2,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=1,
    font=("JetBrainsMonoRoman", 14)
)
entry_output_path.place(x=109.0, y=180.0, width=382.0, height=45.0)

output_label = Label(
    window,
    text="Output Path:",
    bg="#FA7070",
    fg="#FEFDED",
    font=("JetBrainsMonoRoman", 14)
)
output_label.place(x=96.0, y=160.0)

browse_button = Button(
    window,
    text="Browse",
    bg="#FEFDED",
    fg="#000000",
    font=("JetBrainsMonoRoman", 14),
    command=browse_output_folder,
    relief="raised",
    bd=2
)
browse_button.place(x=500.0, y=180.0, width=90.0, height=45.0)

download_button = Button(
    window,
    text="Download MP3",
    bg="#FEFDED",
    fg="#000000",
    font=("JetBrainsMonoRoman", 14),
    command=download_button_clicked,
    relief="raised",
    bd=2
)
download_button.place(x=243.0, y=271.0, width=214.0, height=52.0)

loading_label = Label(
    window,
    bg="#FA7070",
    fg="#000000",
    font=("JetBrainsMonoRoman", 14)
)

window.resizable(False, False)
window.mainloop()