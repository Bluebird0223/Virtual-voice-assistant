import tkinter as tk
from PIL import Image

root = tk.Tk()
file = "voice_wave.gif"

info = Image.open(file)

frames = info.n_frames

im = [tk.PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None


def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(50, lambda: animation(count))


def stop_animation():
    root.after_cancel(anim)


gif_label = tk.Label(root, image="")
gif_label.pack()

start = tk.Button(root, text="start", command=lambda: animation(count))
start.pack()

stop = tk.Button(root, text="stop", command=stop_animation)
stop.pack()

root.mainloop()
