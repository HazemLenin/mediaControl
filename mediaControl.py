import sys
import pynput
from tkinter import Tk
from tkinter.ttk import *

current = set()
keyboard = pynput.keyboard.Controller()

PLAY_PAUSE = [
    {pynput.keyboard.Key.ctrl_r, pynput.keyboard.Key.space},
]

PREVIOUS = [
    {pynput.keyboard.Key.ctrl_r, pynput.keyboard.Key.left},
]

NEXT = [
    {pynput.keyboard.Key.ctrl_r, pynput.keyboard.Key.right},
]

VOLUME_UP = [
    {pynput.keyboard.Key.ctrl_r, pynput.keyboard.Key.up},
]

VOLUME_DOWN = [
    {pynput.keyboard.Key.ctrl_r, pynput.keyboard.Key.down},
]

VOLUME_MUTE = [
    {pynput.keyboard.Key.ctrl_r, pynput.keyboard.KeyCode(char='M')},
    {pynput.keyboard.Key.ctrl_r, pynput.keyboard.KeyCode(char='m')},
]

state = False

def on_press(key):
    global state
    if state:
        if any([key in KEY for KEY in PLAY_PAUSE]):
            current.add(key)
            if any(all(k in current for k in KEY) for KEY in PLAY_PAUSE):
                keyboard.press(pynput.keyboard.Key.media_play_pause)
                print('play/pause')

        if any([key in KEY for KEY in PREVIOUS]):
            current.add(key)
            if any(all(k in current for k in KEY) for KEY in PREVIOUS):
                keyboard.press(pynput.keyboard.Key.media_previous)
                print('previous')

        if any([key in KEY for KEY in NEXT]):
            current.add(key)
            if any(all(k in current for k in KEY) for KEY in NEXT):
                keyboard.press(pynput.keyboard.Key.media_next)
                print('next')

        if any([key in KEY for KEY in VOLUME_UP]):
            current.add(key)
            if any(all(k in current for k in KEY) for KEY in VOLUME_UP):
                keyboard.press(pynput.keyboard.Key.media_volume_up)
                print('volume up')

        if any([key in KEY for KEY in VOLUME_DOWN]):
            current.add(key)
            if any(all(k in current for k in KEY) for KEY in VOLUME_DOWN):
                keyboard.press(pynput.keyboard.Key.media_volume_down)
                print('volume down')

        if any([key in KEY for KEY in VOLUME_MUTE]):
            current.add(key)
            if any(all(k in current for k in KEY) for KEY in VOLUME_MUTE):
                keyboard.press(pynput.keyboard.Key.media_volume_mute)
                print('volume mute')
        
    

def on_release(key):
    if state:
        if any([key in KEY for KEY in PLAY_PAUSE + PREVIOUS + NEXT + VOLUME_UP + VOLUME_DOWN + VOLUME_MUTE]):
            try:
                current.remove(key)
            except KeyError:
                current.clear()


with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as l:
    root = Tk()
    root.geometry('300x300')
    root.title('mediaControl')

    title = Label(text='media control')
    title.pack()

    def onClick():
        global state, button
        state = not(state)
        button.config(text='ON' if state else 'OFF')
        print('ON' if state else 'OFF')

    button = Button(text='ON' if state else 'OFF', command=onClick)
    button.pack()

    vol_up = Label(text='ctrl r + up = volume up', width=27, justify='left')
    vol_up.pack()
    vol_down = Label(text='ctrl r + down = volume down', width=27, justify='left')
    vol_down.pack()
    play_pause = Label(text='ctrl r + space = play/pause', width=27, justify='left')
    play_pause.pack()
    nxt = Label(text='ctrl r + right = next', width=27, justify='left')
    nxt.pack()
    previous = Label(text='ctrl r + left = previous', width=27, justify='left')
    previous.pack()

    root.mainloop()
    sys.exit()
    l.join()
