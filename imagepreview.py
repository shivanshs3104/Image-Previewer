from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()
root.title("Image Viewer")
root.configure(background="#f0f0f0")

image_folder = "images"
image_files = [file for file in os.listdir(image_folder)]
image_list = []
for file in image_files:
    image = ImageTk.PhotoImage(Image.open(os.path.join(image_folder, file)).resize((600,350)))
    image_list.append(image)

counter = 0

def next():
    global counter
    if counter < len(image_list) - 1:
        counter += 1
    else:
        counter = 0
    imageLabel.config(image=image_list[counter])

def previous():
    global counter
    counter -= 1
    if counter < 0:
        counter = len(image_list) - 1
    imageLabel.config(image=image_list[counter])

imageLabel = Label(root, image=image_list[0], bg="#f0f0f0")
imageLabel.pack(pady=10)

button_frame = Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

button1 = Button(button_frame, text="Previous", width=15, height=2, command=previous, bg="#4CAF50", fg="white")
button1.grid(row=0, column=0, padx=10)

button2 = Button(button_frame, text="Next", width=15, height=2, command=next, bg="#4CAF50", fg="white")
button2.grid(row=0, column=1, padx=10)

root.mainloop()
