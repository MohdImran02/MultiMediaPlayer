#Music Player...

from tkinter import *
from pygame import mixer      #mixer class is used to play audio
from tkinter import filedialog
import tkinter.messagebox
import sys
from tkinter import ttk
import time

root = Tk()

#Global variables...

root.playlist = []
root.songAdded = False
root.i = 0

mixer.init()    #Initializing the mixer

root.title("Music Player")
root.geometry("400x400")

root.iconbitmap(r'C:\Tkinter_GUI\player_icon\music_icon.ico')

text = Label(root, text='Mohd Imran')
text.grid(row=0, column=1, columnspan=2)

menubar = Menu(root)
root.configure(menu=menubar)

def about_us():
    tkinter.messagebox.showinfo('our title','This is the info we want')

#def addfile():

def start_progress():
    while(mixer.music.get_busy()):
        '''time.sleep(1)
        pos = mixer.music.get_pos()
        PBar['value'] = int(pos)
        root.update_idletasks()'''   

def file_open():
    global filename
    try:
        filename = filedialog.askopenfilename(initialdir="/Music/", title="Select A File",filetypes=(("mp3 files","*.mp3"),("all files","*.*")))
        root.songAdded = True
        root.playlist.append(filename)
        print(" Added " + filename)
        #root.screenMessage.set("Good! Now Press on the Play Button")
    except:
        tkinter.messagebox.showinfo('our title','Music File is not added')

def close_window():
    mixer.music.stop()
    root.destroy()

def play_music():
    try:
        if(root.songAdded == True):
            #mixer.music.load("musicsong.mp3")  #Add music file to be played
            mixer.music.load(filename)
            mixer.music.play()
            music_name.delete(0,END)
            music_name.insert(0,filename)
            #start_progress()
            
        else:
            tkinter.messagebox.showinfo('our title','Select a music file to play please')
    except:
        tkinter.messagebox.showinfo('our title','Select a music file to play')

def stop_music():
    global end_event
    #mixer.music.load("musicsong.mp3")  #Add music file to be played
    mixer.music.stop()

def forward_music():
    print('for')

def backward_music():
    print('back')

def rewind_music():
    #mixer.music.load(filename)
    mixer.music.rewind()

def queue_songs():
    global filename
    filename = filedialog.askopenfilename(initialdir="/Music/", title="Select A File",filetypes=(("mp3 files","*.mp3"),("all files","*.*")))
    #queued = []
    #queued.append(filename)
    mixer.music.queue(filename)
    while(mixer.music.get_busy()):
        pass
        #Keep looping here till current file being played
        
    play_music()
               

def set_vol(vol):
    volume = int(vol)/100  #Mixer takes valume 0.00-1.00
    mixer.music.set_volume(volume)
    #PBar['value'] = int(vol)
    #root.update_idletasks()

def prev_music():
    if(root.songAdded == False):
        tkinter.messagebox.showinfo('our title','add music first')
    else:
        try:
            global filename
            if(root.playlist[root.i - 1]):
                root.i -= 1
                filename = root.playlist[root.i]
                play_music()
                curr_song = root.playlist[root.i]
                #tkinter.messagebox.showinfo('our title',curr_song)
            else:
                tkinter.messagebox.showinfo('our title','No previous songs')
        except:
            stop_music()
            messagebox.showinfo('our title','No previous songs')

def next_music():
    if(root.songAdded == False):
        tkinter.messagebox.showinfo('our title','First add some Music Bitch!')
    else:
        try:
            global filename
            if(root.playlist[root.i]):
                root.i += 1
                filename = root.playlist[root.i]
                play_music()
                curr_song = root.playlist[root.i]
                #tkinter.messagebox.showinfo('our title',curr_song)
            else:
                root.i -= 1
        except:
            tkinter.messagebox.showinfo('our title','End of Playback, Please add more songs')

def set_fadeout_time():
        #fadeout_time.delete(0.0, "end")
        txtname = fadeout_time.get("0.0",END)
        time = int(txtname)
        time_sec = time*60*1000
        print('fadeout = ',time)
        print('fadeout = ',time_sec)
        mixer.music.fadeout(time_sec)

playPhoto = PhotoImage(file='play.png')
playBtn = Button(root, image = playPhoto, command = play_music)
playBtn.grid(row=1, column=1)

forwardPhoto = PhotoImage(file='forward.png')
forwardBtn = Button(root, image = forwardPhoto, command = forward_music)
forwardBtn.grid(row=2, column=2)

backwardPhoto = PhotoImage(file='backward.png')
backwardBtn = Button(root, image = backwardPhoto, command = backward_music)
backwardBtn.grid(row=2, column=0)

stopPhoto = PhotoImage(file='stop.png')
stopBtn = Button(root, image = stopPhoto, command = stop_music)
stopBtn.grid(row=2, column=1)

scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command = set_vol)
scale.set(40)
scale.grid(row=4, column=1)

button1 = Button(root, text="Previous", fg="red", command=prev_music) #Positioning Button as (<FrameName>,<Text to Appear>,<Text Color>)
button1.grid(row=5, column=0)

button4 = Button(root, text="Next",fg="blue", command=next_music)
button4.grid(row=5, column=2)

button5 = Button(root, text="Rewind",fg="blue", command=rewind_music)
button5.grid(row=6, column=2)

music_name = Entry(root, width=50, borderwidth = 5)
music_name.grid(row=9,column=1,columnspan=4,padx=10,pady=10)

fadeout_time = Text(root, height=1, width=5)
fadeout_time.grid(row=8,rowspan=1,padx=5,pady=20)

fadeout_Btn = Button(root, text = 'Set time', command=set_fadeout_time)
fadeout_Btn.grid(row=8,column=2)

fadeoutlabel = Label(root,text='Set Fadeout time (min)',fg='purple')
fadeoutlabel.grid(row=8,column=1)

PBar = ttk.Progressbar(
    root,
    orient = HORIZONTAL,
    length = 200,
    maximum = 100,
    value = 0,
    mode = 'determinate') 
#PBar = Progressbar(root,orient=HORIZONTAL,length=200)
PBar.grid(row=7,columnspan=4)


#Create sub-menu

#menubar = Menu(root)
#root.configure(menu=menubar)


subMenuFiles = Menu(menubar)
menubar.add_cascade(label = "Media", menu = subMenuFiles)
subMenuFiles.add_command(label = "Open Media Files", command = file_open)
subMenuFiles.add_command(label = "Media Library")
subMenuFiles.add_command(label = "Exit", command = close_window)

subMenuVideo = Menu(menubar)
menubar.add_cascade(label = "Video", menu = subMenuVideo)
subMenuVideo.add_command(label = "Add Video Track")
subMenuVideo.add_command(label = "Full Screen")
subMenuVideo.add_command(label = "Take Snapshot")

subMenuAudio = Menu(menubar)
menubar.add_cascade(label = "Audio", menu = subMenuAudio)
subMenuAudio.add_command(label = "Add Audio Track")

subMenuQueue = Menu(menubar)
menubar.add_cascade(label = "Queue", menu = subMenuQueue)
subMenuQueue.add_command(label = "Add Track to Queue", command = queue_songs)

subMenuContact = Menu(menubar)
menubar.add_cascade(label = "Contact", menu = subMenuContact)
subMenuContact.add_command(label = "About Us", command=about_us)
subMenuContact.add_command(label = "Phone/email")

root.mainloop()
mixer.music.stop()  #This command is used to stop the background music if window closed accidently without stopping music
