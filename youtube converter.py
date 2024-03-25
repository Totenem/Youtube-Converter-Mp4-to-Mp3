from pathlib import Path
import os
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from pytube import YouTube

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"Enter the path of the folder named assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

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
        messagebox.showinfo("Conversion Successful", "The conversion process has been completed successfully!")
        
    except Exception as ex:
        print(f"An error occurred: {ex}")
        messagebox.showerror("Error", f"An error occurred: {ex}")

def download_button_clicked():
    video_url = entry_1.get()
    output_folder = entry_2.get()
    download_youtube_video(video_url, output_folder)

window = Tk()

window.geometry("700x358")
window.configure(bg="#FA7070")

canvas = Canvas(
    window,
    bg="#FA7070",
    height=358,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    700.0,
    62.0,
    fill="#FEFDED",
    outline=""
)

canvas.create_text(
    71.0,
    13.0,
    anchor="nw",
    text="MP4 TO MP3 YOUTUBE CONVERTER BY TOTEMN",
    fill="#000000",
    font=("JetBrainsMonoRoman Regular", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    350.0,
    136.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=109.0,
    y=113.0,
    width=482.0,
    height=45.0
)

canvas.create_text(
    96.0,
    92.0,
    anchor="nw",
    text="Enter Youtube Link",
    fill="#FEFDED",
    font=("JetBrainsMonoRoman Regular", 14 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    350.0,
    223.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=109.0,
    y=200.0,
    width=482.0,
    height=45.0
)

canvas.create_text(
    96.0,
    179.0,
    anchor="nw",
    text="Enter The Output Path",
    fill="#FEFDED",
    font=("JetBrainsMonoRoman Regular", 14 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=download_button_clicked,
    relief="flat"
)
button_1.place(
    x=243.0,
    y=271.0,
    width=214.0,
    height=52.0
)
window.resizable(False, False)
window.mainloop()
