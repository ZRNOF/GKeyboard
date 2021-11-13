from tkinter import *
import pygame
from PIL import Image, ImageTk

pygame.mixer.init()

def change(path):
    image=path
    img = ImageTk.PhotoImage(Image.open(image))
    chang.config(image=img)
    chang.Image = img

def up(event):
    change("1.png")

def down(event):
    change("2.png")

def pitch(p):
    pygame.mixer.music.load(f"{p}.mp3")
    pygame.mixer.music.play()

def key_pitch(event):
    change("2.png")
    try:
        pygame.mixer.music.load(f"{pitch_dic[event.keysym]}.mp3")
        pygame.mixer.music.play()
    except:
        pass

pitch_dic = {"1":"C", "2":"D", "3":"E", "4":"F", "5":"G", "6":"A", "7":"B", "8":"HC", "9":"HD", "0":"HE"}
pitch_lst = ["C", "D", "E", "F", "G", "A", "B", "HC", "HD", "HE"]

root = Tk()
root.geometry("400x300")
root.resizable(False, False)
root.title("國樂")
root.bind("<Button-1>", down)
root.bind("<ButtonRelease-1>", up)
root.bind("<Key>", key_pitch)
root.bind("<KeyRelease>", up)

image="1.png"
img = ImageTk.PhotoImage(Image.open(image))
chang = Label(root, image=img)
chang.pack()

for i in range(10):
    button = Button(root, text=pitch_lst[i], width=4, command=lambda i=i:pitch(pitch_lst[i]))
    button.pack(padx=1, side=LEFT)

root.mainloop()
