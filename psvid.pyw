#! /usr/bin/env python3
#-*- coding: UTF-8 -*-
# PSvid Version 3.0
# App to convert videos for PS brand consoles using ffmpeg
changelog = """
1.0 Initial release
2.0 Changed name to PSvid
    Added support for PS2, PS3 and PS VITA
2.0b    fixed bug with folders having spaces in their names
    the output video is now in the same folder as PSvid
    updated the readme file
3.0 redesigned the GUI
    added more formats under "OTHERS"
        iPhone, iPad, iPod Classic and Android
3.1 no more need for a CLI window to be opened
    added overwrite option if output file exists
    small change to output file name
4.0 Python3 port by Krazynez
"""

import os, tkinter, subprocess, sys, re
from tkinter import IntVar
from tkinter import filedialog
from tkinter import Label 
from tkinter import Toplevel 

# Detect OS
if sys.platform.startswith("linux") == True:
    shell = "xterm"
elif sys.platform.startswith("win") == True:
    shell = "cmd"
elif sys.platform.startswith("darwin") == True:
    shell = "zsh" # I have no fucking idea about this one ( I do ;-) )

def credits():
    newWindow = Toplevel()

    newWindow.title("Credits")
    newWindow.geometry("200x80")
    Label(newWindow, text="Version 4.0\nAcid_Snake\nKrazynez").pack()

def close():
    sys.exit()
    

def work():
    video_output, origext = os.path.splitext(video_input.replace("*", " "))
    video_output = os.path.basename(video_output)
    def run():
        if subprocess.call(f"ffmpeg -i \"{video_input}\" {ffcommand} \"{video_output}{ext}\"", shell=True) == 0:
            def reapear():
                gui2.destroy()
                maingui()
            gui2 = tkinter.Tk(className="done")
            gui2.geometry("80x80")
            done_text = tkinter.Message(gui2, text="DONE")
            done_text.pack()
            done_close = tkinter.Button(gui2, text="Close", command=reapear)
            done_close.pack()
            gui2.mainloop()
    if os.path.exists(video_output+ext) == True:
        def overwrite():
            warn_gui.destroy()
            os.remove(video_output+ext)
            run()
        def cancel():
            warn_gui.destroy()
            maingui()
        warn_gui = tkinter.Tk()
        warn_label = tkinter.Label(warn_gui, text="Output file exists")
        warn_go = tkinter.Button(warn_gui, text="Overwrite", command=overwrite)
        warn_cancel = tkinter.Button(warn_gui, text="Cancel", command=cancel)
        warn_label.pack()
        warn_go.pack()
        warn_cancel.pack()
        warn_gui.mainloop()
    else: 
        try:
            run()
        except KeyboardInterrupt:
            print("Quitting\n")
            sys.exit()

def browse_file():
    filename = filedialog.askopenfilename(**filedialog.file_opt)
    video_input_entry.insert(0, filename)
def maingui():
    def go():
        global ffcommand, ext, video_input
        video_input = video_input_entry.get()
        if Rvar.get() == 1:
            ffcommand = " -c:a aac -c:v libx264 -profile:v main -level:v 3.0 -x264opts ref=3:b-pyramid=none:weightp=1 -r 29.97 -s 480x272 -pix_fmt yuv420p -b:v 768k -ar 48000 -ab 192k "
            ext = "_psp.mp4"
            gui.withdraw()
            work()
        elif Rvar.get() == 2:
            ffcommand = " -c:a aac -f psp -r 29.97 -s 640x480 -b:v 768k -ar 44100 -ab 128k "  
            ext = "_psvita.mp4"
            gui.withdraw()
            work()
        elif Rvar.get() == 3:
            ffcommand = " -vcodec libx264 -s 1280x720 -level 41 -vpre normal -crf 24 -threads 0 -c:a aac -ab 151k -ac 2 -ar 44100 "
            ext = "_ps3.mp4"
            gui.withdraw()
            work()
        elif Rvar.get() == 4:
            gui.destroy()
            def go2():
                global ffcommand, ext
                print(others_var.get())
                if others_var.get() == 1:
                    ffcommand = " -f avi -vcodec msmpeg4 -s 640x480 "
                    ext = "_ps2.avi"
                    others_gui.destroy()
                    work()
                elif others_var.get() == 2:
                    ffcommand = " -r 25 -b:v 480K -f mp4 -s 480×320 -c:a aac -ar 22050 -ab 48k -ac 2 "
                    ext = "_iphone.mp4"
                    others_gui.destroy()
                    work()
                elif others_var.get() == 3:
                    ffcommand = " -c:a aac -ab 160000 -s 1024x768 -vcodec libx264 -vpre slow -f ipod640 -b:v 1200kb -threads 0 -f mp4 "
                    ext = "_ipad.mp4"
                    others_gui.destroy()
                    work()
                elif others_var.get() == 4:
                    ffcommand = " -c:a aac -ac 2 -ab 160k -s 480x320 -vcodec libx264 -vpre slow -f iPod640 -b:v 1200k -f mp4 -threads 0 "
                    ext = "_ipod.mp4"
                    others_gui.destroy()
                    work()
                elif others_var.get() == 5:
                    ffcommand = " -y -c:a aac -ac 2 -ab 160k -s 1024x800 -vcodec libx264 -f iPod640 -vpre slow -f mp4 -threads 0  "
                    ext = "_android_1024x800.mp4"
                    others_gui.destroy()
                    work()
                elif others_var.get() == 6:
                    ffcommand = " -y -c:a aac -ac 2 -ab 160k -s 854x480 -vcodec libx264 -f iPod640 -vpre slow -f mp4 -threads 0  "
                    ext = "_android_854x480.mp4"
                    others_gui.destroy()
                    work()
                elif others_var.get() == 7:
                    ffcommand = " -y -c:a aac -ac 2 -ab 160k -s 800x480 -vcodec libx264 -f iPod640 -vpre slow -f mp4 -threads 0 "
                    ext = "_android_800x480.mp4"
                    others_gui.destroy()
                    work()
                elif others_var.get() == 8:
                    ffcommand = " -y -c:a aac -f ipod640 -ac 2 -ab 160k -s 480x320 -vcodec libx264 -vpre slow -f mp4 -threads 0 "
                    ext = "_android_480x320.mp4"
                    others_gui.destroy()
                    work()
            others_gui = tkinter.Tk()
            warn = tkinter.Label(others_gui, text="Experimental")
            warn.pack()
            others_var = IntVar()
            others_R1 = tkinter.Radiobutton(others_gui, text="PS2", variable=others_var, value=1)
            others_R2 = tkinter.Radiobutton(others_gui, text="iPhone", variable=others_var, value=2)
            others_R3 = tkinter.Radiobutton(others_gui, text="iPad", variable=others_var, value=3)
            others_R4 = tkinter.Radiobutton(others_gui, text="iPod Classic", variable=others_var, value=4)
            others_R5 = tkinter.Radiobutton(others_gui, text="Android (1024x800)", variable=others_var, value=5)
            others_R6 = tkinter.Radiobutton(others_gui, text="Android (854×480)", variable=others_var, value=6)
            others_R7 = tkinter.Radiobutton(others_gui, text="Android (800×480)", variable=others_var, value=7)
            others_R8 = tkinter.Radiobutton(others_gui, text="Android (480×320)", variable=others_var, value=8)
            others_R1.pack(anchor="w")
            others_R2.pack(anchor="w")
            others_R3.pack(anchor="w")
            others_R4.pack(anchor="w")
            others_R5.pack(anchor="w")
            others_R6.pack(anchor="w")
            others_R7.pack(anchor="w")
            others_R8.pack(anchor="w")
            others_button = tkinter.Button(others_gui, text="Convert", command=go2)
            others_button.pack()
    global video_input_entry, gui
    filedialog.file_opt = options = {}
    options['filetypes'] = [("All Files", ".*")]
    options['title'] = "Select Video file"
    gui = tkinter.Tk(className=" PSVid v4.0")
    gui.geometry("400x200")
    file_frame = tkinter.Frame(gui)
    file_frame.pack(side="left", padx=(10, 0))
    video_input_name = tkinter.Message(file_frame, text="Input Video")
    video_input_name.pack()
    video_input_entry = tkinter.Entry(file_frame)
    video_input_entry.pack()
    video_input_browse = tkinter.Button(file_frame, text="Browse Video File", command=browse_file)
    video_input_browse.pack()
    convert = tkinter.Button(file_frame, text="Convert", command=go)
    convert.pack()
    credit = tkinter.Button(file_frame, text="Credits", command=credits) 
    credit.pack()
    _quit = tkinter.Button(file_frame, text="Close", command=close)
    _quit.pack(pady=(0, 10))
    select_frame = tkinter.Frame(gui)
    select_frame.pack(side="right", padx=(0, 10))
    Rvar = IntVar()
    R1 = tkinter.Radiobutton(select_frame, text="PSP/PSVITA/PS3", variable=Rvar, value=1)
    R2 = tkinter.Radiobutton(select_frame, text="PSVITA/PS3", variable=Rvar, value=2)
    R3 = tkinter.Radiobutton(select_frame, text="PS3", variable=Rvar, value=3)
    R4 = tkinter.Radiobutton(select_frame, text="OTHERS", variable=Rvar, value=4)
    R1.pack(anchor="w")
    R2.pack(anchor="w")
    R3.pack(anchor="w")
    R4.pack(anchor="w")
    gui.mainloop()
try:
    maingui()
except KeyboardInterrupt:
    print("Quitting")
    sys.exit(0)


#!xyz!#
