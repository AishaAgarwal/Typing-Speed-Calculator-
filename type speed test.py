from tkinter import *
from timeit import default_timer as timer
import random

window = Tk()
window.geometry("500x500")
window.configure(bg = "black")
hs_file = open('highscore.txt', 'r+')

x=0


def game():
    global x
    if x==0:
        window.destroy()
        x=x+1
    def check_result():
        if entry.get()==words[word]:
            end=timer()
            print(end-start)
        else:
            print("wrong spelling")
    words=['python','java','coding','oracle','typing','speed','test']
    word=random.randint(0,(len(words)-1))
    start=timer()
    windows=Tk()
    windows.geometry("550x500")
    x2 = Label(windows, text=words[word], bg = 'black', fg = 'white', font="time 20")
    x2.place(x=15,y=10)
    x3 = Label(windows,text="lets see how fast you can type",font="time 20")
    x3.place(x=40,y=120)
    entry=Entry(windows)
    entry.place(x=280,y=55)
    b2=Button(windows,text="submit",command=check_result,width=12,bg='#fc2828')
    b2.place(x=155,y=420)
    b3=Button(windows,text="try again!",command=game,width=12,bg='#ffc003')
    b3.place(x=265,y=420)
    windows.mainloop()

x1 = Label(window, text="lets start this game ...",bg = "black", fg = "white",font="time 20")
x1.place(x=100,y=50)

b1=Button(window,text="Go!",command=game,width=12,bg='#fcba03')
b1.place(x=150,y=120)

hs_text = Label(window, text = "Highscore", width = 12, bg = '#03fcf8', font = "times 35")
hs_text.place(x=90, y=240)

hs = int(hs_file.readline())
hs_val = Label(window, text = str(hs)+" WPM", width = 12, fg = "#03fcf8", bg = 'black', font="times 35")
hs_val.place(x=110, y=320)

window.mainloop()
