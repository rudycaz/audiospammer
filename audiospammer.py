import pygame
import os
import random
import tkinter as tk
from PIL import Image, ImageTk

# Initialize pygame mixer for audio playback
pygame.mixer.init()

# Set the path to your audio file (Update this to your actual file path)
audio_file = 'path to your mp3 file'

# Load the audio file
pygame.mixer.music.load(audio_file)

# Set system volume to max using AppleScript
def set_volume_max():
    os.system("osascript -e 'set volume output volume 100'")  # 100% volume

# Function to play the audio in a loop
def play_audio():
    # Ensure volume is max before playing
    set_volume_max()
    pygame.mixer.music.play(-1)  # Play indefinitely

# Folder containing images (Update this path to your images folder)
image_folder = 'path to a folder of images you wish to display'  # Change to your folder
image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Function to randomly display an image in a pop-up window
def show_random_image(window):
    random_image = random.choice(image_files)
    img = Image.open(random_image)

    # Convert the image to a format that Tkinter can display
    img = img.resize((300, 300))  # Resize image if needed
    tk_img = ImageTk.PhotoImage(img)

    # Create a label in the window and add the image to it
    label = tk.Label(window, image=tk_img)
    label.image = tk_img  # Keep a reference to avoid garbage collection
    label.pack()

    # Randomize the window's position on the screen
    window.geometry(f"+{random.randint(100, 500)}+{random.randint(100, 500)}")

# Function to check password and reset volume periodically
def check_password_and_volume(root):
    set_volume_max()
    user_input = input("Enter password to stop the audio and pop-ups: ")
    
    if user_input == "dick":  # Change this to your desired password
        pygame.mixer.music.stop()
        root.quit()  # Close the Tkinter window and stop the program
    else:
        root.after(1000, check_password_and_volume, root)  # Check again after 1 second

# Main function to run the Tkinter window and audio
def main():
    # Start audio playback
    play_audio()

    # Create the Tkinter window (this must run on the main thread)
    root = tk.Tk()
    root.title("Random Image Pop-up")

    # Schedule image pop-ups to occur every few seconds
    def show_images_loop():
        show_random_image(root)  # Show a random image
        root.after(3000, show_images_loop)  # Repeat every 3 seconds

    root.after(1000, show_images_loop)  # Start showing images after 1 second
    root.after(1000, check_password_and_volume, root)  # Start checking for password

    # Run the Tkinter main loop (keeps the GUI running)
    root.mainloop()

if __name__ == "__main__":
    main()
