#main.pyw
#Program main of the PipBoy project
#
#11.07.2018 Bastien Piguet

import os
import time
import radioRTL
from tkinter import *
from tkinter import ttk

green = '#0f0'

def styles():
    style = ttk.Style()
    style.theme_create(
        "PipBoy",
        parent="alt",
        settings={
            "TNotebook":{
                "configure":{
                    "background": 'black',
                    "tabmargins": [0, 0, 0, 0],
                    "borderwidth": 1,
                }
            },
            "TNotebook.Tab": {
                "configure": {
                    "padding": [10, 5],
                    "background": 'black',
                    "foreground": '#0f0',
                    "font": 'Poetsen\ One -25',
                    "borderwidth": 1
                },
                "map": {
                    "background": [("selected", '#050')],
                    "font": [("selected", 'Poetsen\ One -25')]
                }
            }
        }
    )
    style.theme_use("PipBoy")

def main():
    myRadio = radioRTL.Radio()
    
    def sethour():
        hour.set(time.strftime('%H:%M / %d.%m.%Y'))
        dihour.after(9995, sethour)

    def updateTK():
        frequence.set('%sMhz'%myRadio.frequence)
        if myRadio.runRadio:
            pause.config(image=imgpause)
        else:
            pause.config(image=imgplay)
            radioSelect.set(100)
        
    myRadio.config(command=updateTK)

####    
    Window = Tk()
    styles()
    #Window.config(cursor='none')
    #Window.attributes('-fullscreen', True)
    #Window.resizable(False, False)
    Window.geometry('800x480')
    Window.title('PipBoy 5000')
    Window.configure(bg='black')
###-
    hour = StringVar()
    dihour = Label(Window, textvariable=hour, bg='black', foreground=green, font='Poetsen\ One -25')
    dihour.grid(column=0, row=0, sticky='w')
    sethour()
###-
    imgpara = PhotoImage(file='asset/gear32.png')
    settingsButton = Button(Window,
                            bg='black',
                            fg=green,
                            activebackground='black',
                            image=imgpara,
                            text='Settings',
                            font='Poetsen\ One -20',
                            bd=0,
                            command=Window.destroy)
    settingsButton.grid(column=1, row=0, sticky='e', padx=5)


####
    View = ttk.Notebook(Window, width=800, height=394)

###-    
    Radio = Frame(View, bg='black')
##--  
    List = Frame(Radio, bg='black', height=390)
    #listframe = Frame(List, bg='black')
    radioSelect = IntVar()
    radioSelect.set(100)
    for x in range(len(myRadio.radioList)):
        Radiobutton(List,
                    text=myRadio.radioList[x][0],
                    variable=radioSelect, value=x,
                    command=lambda:myRadio.play(radioSelect.get()+1),
                    indicatoron=False,
                    font='Poetsen\ One -22',
                    bg='black',
                    fg=green,
                    activebackground='black',
                    activeforeground=green,
                    selectcolor='#050',
                    width=20,
                    offrelief='flat',
                    bd=0).pack(anchor='w')
    List.grid(row=0, column=0, sticky='nw')
##--    
    '''scrollradio = Scrollbar(Radio, orient='vertical', command=List.yview,
                            activebackground='black',
                            bg='black',
                            highlightbackground='black',
                            highlightcolor='black',
                            troughcolor='black')
    scrollradio.grid(row=0, column=1, sticky='ns')
    List.configure(yscrollcommand=scrollradio.set)'''

###-
    Setting = Frame(Radio, bg='black')

    fmbutton = Button(Setting, command=lambda:myRadio.config(modulation='wbfm'), text='FM', font='Poetsen\ One 20', bg='black', fg=green, relief='flat')
    fmbutton.grid(row=0, column=1)
    ambutton = Button(Setting, command=lambda:myRadio.config(modulation='am'), text='AM', font='Poetsen\ One 20', bg='black', fg=green, relief='flat')
    ambutton.grid(row=0, column=3)
    
    frequence = StringVar()
    frequence.set('87.5Mhz')
    
    freq = Label(Setting, font='Poetsen\ one -80', textvariable=frequence, bg='black', fg=green, bd=10, relief='sunken', width=10, justify='center')
    freq.grid(row=1, column=0, columnspan=5, sticky='e', ipady=30, padx=20, pady=5)
    
    imgprev = PhotoImage(file='asset/prev.png')
    imgprev = imgprev.subsample(3)
    prev = Button(Setting, command=myRadio.previous, text='|<', image=imgprev, font='Poetsen\ One -20 ', bg='black', fg=green, bd=0, activebackground='black', activeforeground=green)
    prev.grid(row=2, column=0, columnspan=2)
    
    imgpause = PhotoImage(file='asset/pause.png')
    imgpause = imgpause.subsample(3)
    imgplay = PhotoImage(file='asset/play.png')
    imgplay = imgplay.subsample(3)
    pause = Button(Setting, command=myRadio.play, text='>', image=imgplay, font='Poetsen\ One -20 ', bg='black', fg=green, bd=0, activebackground='black', activeforeground=green)
    pause.grid(row=2, column=2)
    
    imgnext = PhotoImage(file='asset/prev.png')
    imgnext = imgnext.subsample(-3)
    _next = Button(Setting, command=myRadio.next, text='>|', image=imgnext, font='Poetsen\ One -20 ', bg='black', fg=green, bd=0, activebackground='black', activeforeground=green)
    _next.grid(row=2, column=3, columnspan=2)
    
    imgshiftL = PhotoImage(file='asset/shift.png')
    imgshiftL = imgshiftL.subsample(3)
    shiftL = Button(Setting, command=myRadio.shiftL, text='|<<', image=imgshiftL, font='Poetsen\ One -20 ', bg='black', fg=green, bd=0, activebackground='black', activeforeground=green)
    shiftL.grid(row=3, column=0, columnspan=2, sticky='e')
    
    imgshiftR = PhotoImage(file='asset/shift.png')
    imgshiftR = imgshiftR.subsample(-3)
    shiftR = Button(Setting, command=myRadio.shiftR, text='>>|', image=imgshiftR, font='Poetsen\ One -20 ', bg='black', fg=green, bd=0, activebackground='black', activeforeground=green)
    shiftR.grid(row=3, column=3, columnspan=2, sticky='w')

    saveButton = Button(Setting, command=myRadio.saveRadio, text='Save Radio', font='Poetsen\ One -25 ', bg='black', fg=green, bd=0, activebackground='black', activeforeground=green)
    saveButton.grid(row=4, column=0, columnspan=2, sticky='e')
    
    removeButton = Button(Setting, command=lambda:myRadio.removeSave(radioSelect.get()), text='Delete Radio', font='Poetsen\ One -25 ', bg='black', fg=green, bd=0, activebackground='black', activeforeground=green)
    removeButton.grid(row=4, column=3, columnspan=2, sticky='w')
    
    Setting.grid(row=0, column=1, sticky='news')

####
    Map = Frame(View, background='black')
###-
    View.add(Radio, text='Radio')
    View.add(Map, text='Map')
    View.grid(column=0, row=1, columnspan=2)

    Window.mainloop()

main()
