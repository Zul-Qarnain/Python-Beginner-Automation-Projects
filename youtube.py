from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        if streams:
            highest_res_stream = streams.first()  # Get the first stream
            highest_res_stream.download(output_path=save_path)
            print("Video downloaded successfully!")
        else:
            print("No progressive MP4 streams available.")
    except Exception as e:
        print(f"An error occurred: {e}")
def open_file_dialog():
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory()
    root.destroy()  # Close the tkinter window after directory selection
    if folder:
        print(f"Selected folder: {folder}")
    return folder
if __name__ == "__main__":
    video_url = input("Please enter a YouTube URL: ").strip()
    save_dir = open_file_dialog()
    if save_dir:
        print("Started download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")
