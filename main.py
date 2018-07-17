#main.pyw
#Program main of the PipBoy project
#
#11.07.2018 Bastien Piguet

import os
import time
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

radiolist = [['91.0Mhz - RTS', 91.0],
             ['91.6Mhz - COULEUR3', 91.6],
             ['102.4Mhz - ROUGE FM', 102.4],
             ['91.0Mhz - RTS', 91.0],
             ['91.6Mhz - COULEUR3', 91.6],
             ['102.4Mhz - ROUGE FM', 102.4],
             ['91.0Mhz - RTS', 91.0],
             ['91.6Mhz - COULEUR3', 91.6],
             ['102.4Mhz - ROUGE FM', 102.4],
             ['91.0Mhz - RTS', 91.0],
             ['91.6Mhz - COULEUR3', 91.6],
             ['102.4Mhz - ROUGE FM', 102.4]]

selradio = 100
def main():
    
    def sethour():
        hour.set(time.strftime('%H:%M / %d.%m.%Y'))
        dihour.after(9995, sethour)
        
    def LaunchRadio():
        def play():
            print('rtl_fm -M wbfm -r 24000 -f %s | aplay -r 24000 -f S16_LE' %int(freqvalue.get()*1000000))
        def previous():
            None
        def next():
            None
        def shiftL():
            None
        def shiftR():
            None
        global selradio
        if radio.get() != selradio:
            selradio = radio.get()
            print('rtl_fm -M wbfm -r 24000 -f %s | aplay -r 24000 -f S16_LE' %int(radiolist[selradio][1]*1000000))
            frequence.set('%sMhz'%radiolist[selradio][1])
        else:
            print('killall rtl_fm')
            selradio=100
            radio.set(100)

    
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
    settingsButton.grid(column=1, row=0, sticky='e')


####
    View = ttk.Notebook(Window, width=800, height=394)

###-    
    Radio = Frame(View, bg='black')
##--  
    List = Frame(Radio, bg='black', height=390)
    #listframe = Frame(List, bg='black')
    radio = IntVar()
    radio.set(100)
    for x in range(len(radiolist)):
        Radiobutton(List,
                    text=radiolist[x][0],
                    variable=radio, value=x,
                    command=LaunchRadio,
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
    
    freqvalue = DoubleVar()
    freqvalue.set(87.5)
    frequence = StringVar()
    frequence.set('%sMhz' %freqvalue.get())
    
    freq = Label(Setting, font='Poetsen\ one -80', textvariable=frequence, bg='black', fg=green, bd=10, relief='sunken', width=10, justify='center')
    freq.grid(row=0, column=0, columnspan=5, sticky='e', ipady=30, padx=20, pady=5)
    
    imgprev = PhotoImage(file='asset/prev.png')
    imgprev = imgprev.subsample(3)
    prev = Button(Setting, command=LaunchRadio.previous, text='|<', image=imgprev, font='Poetsen\ One -20 ', bg='black', fg=green, bd=0, activebackground='black', activeforeground=green)
    prev.grid(row=1, column=0, columnspan=2)
    
    imgpause = PhotoImage(file='asset/play.png')
    imgpause = imgpause.subsample(3)
    pause = Button(Setting, command=LaunchRadio.play, text='>', image=imgpause, font='Poetsen\ One -20 ', bg='black', fg=green, bd=0, activebackground='black', activeforeground=green)
    pause.grid(row=1, column=2)
    
    imgnext = PhotoImage(file='asset/prev.png')
    imgnext = imgnext.subsample(-3)
    _next = Button(Setting, command=LaunchRadio.next, text='>|', image=imgnext, font='Poetsen\ One -20 ', bg='black', fg=green, bd=0, activebackground='black', activeforeground=green)
    _next.grid(row=1, column=3, columnspan=2)
    
    imgshiftL = PhotoImage(file='asset/shift.png')
    imgshiftL = imgshiftL.subsample(3)
    shiftL = Button(Setting, command=LaunchRadio.shiftL, text='|<<', image=imgshiftL, font='Poetsen\ One -20 ', bg='black', fg=green, bd=0, activebackground='black', activeforeground=green)
    shiftL.grid(row=2, column=1, columnspan=2, sticky='w')
    
    imgshiftR = PhotoImage(file='asset/shift.png')
    imgshiftR = imgshiftR.subsample(-3)
    shiftR = Button(Setting, command=LaunchRadio.shiftR, text='>>|', image=imgshiftR, font='Poetsen\ One -20 ', bg='black', fg=green, bd=0, activebackground='black', activeforeground=green)
    shiftR.grid(row=2, column=3, columnspan=2, sticky='w')
    
    Setting.grid(row=0, column=1, sticky='news')

####
    Map = Frame(View, background='black')
###-
    View.add(Radio, text='Radio')
    View.add(Map, text='Map')
    View.grid(column=0, row=1, columnspan=2)

    Window.mainloop()

main()
