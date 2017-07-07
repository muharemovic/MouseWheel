#!/usr/bin/python3
# Author: Ramiz Muharemovic
# https://github.com/muharemovic
#adjust the mouse scroll speed ubuntu
import apt
import os
import tkinter as tk

def scroll_speed(val):
    a = '''".*"
None,      Up,   Button4, {}
None,      Down, Button5, {}
Control_L, Up,   Control_L|Button4
Control_L, Down, Control_L|Button5
Shift_L,   Up,   Shift_L|Button4
Shift_L,   Down, Shift_L|Button5'''.format(val,val)
    with open(os.path.expanduser('~/.imwheelrc'), 'w') as f:
        f.write(a)
        f.close()

def get_info_scroll():
    with open(os.path.expanduser('~/.imwheelrc')) as f:
        lista = [line.split() for line in f]
        return lista [2][3]


def gui():
    root = tk.Tk()
    scale = tk.Scale(orient='horizontal', from_=0, to=20, font=("Ubuntu Bold",18),command = scroll_speed)
    scale.pack()
    scale.set(get_info_scroll())
    text = tk.Label( text="Mouse scroll speed",font=("Ubuntu",12))
    text.pack()
    root.resizable(False, False)
    root.geometry("200x100")
    root.title("Scrolling mouse")
    root.mainloop()
    scroll_speed
    startup()
    os.system("x-terminal-emulator -e imwheel -kill")

def startup():
    a = '''[Desktop Entry]
Type=Application
Exec=imwheel
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_US]=imwheel
Name=imwheel
Comment[en_US]=
Comment='''
    with open(os.path.expanduser('~/.config/autostart/imwheel.desktop'), 'w') as f:
        f.write(a)
        f.close()


gui()









