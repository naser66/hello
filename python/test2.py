from tkinter import *
import tkinter as tkp
import pygame

s=0
t=0
#window
player = Tk()
player.title("Music")
player.geometry('500x500')

#pygame
pygame.init()
pygame.mixer.init()

mxstate=0
file="1.mp3"



#play
def play():

    global mxstate
    if mxstate == 0:
         pygame.mixer.music.load(file)
         pygame.mixer.music.play()

         return


    else:
        pygame.mixer.music.unpause()

#pause
def pause():
    global mxstate
    pygame.mixer.music.pause()
    mxstate =  1
    return



#stop
def stop():
    global mxstate
    pygame.mixer.music.stop()
    mxstate =  0
    return

#unpause
def unpause():
    pygame.mixer.music.unpause()


def changevolume():
    a = volume.get()
    pygame.mixer.music.set_volume(a)


#button
btnplay=tkp.Button(player, width="5", height="3",text="PLAY", bg="green", command=play)
btnpause= tkp.Button(player,width="5", height="3", text="PAUSE", bg="pink", command=pause)
btnunpause= tkp.Button(player, width="5", height="3", text="UnPause",bg="yellow", command=unpause)
btnstop= tkp.Button(player,width="5",height="3", text="STOP",bg="red", command=stop)



#pack
btnplay.pack(fill="x")
btnpause.pack(fill="x")
btnunpause.pack(fill="x")
btnstop.pack(fill="x")








player.mainloop()
