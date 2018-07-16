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
                    "tabmargins": [0, 0, 0, 0]
                }
            },
            "TNotebook.Tab": {
                "configure": {
                    "padding": [10, 5],
                    "background": 'black',
                    "foreground": '#0f0',
                    "font": 'Poetsen\ One -25 bold',
                },
                "map": {
                    "background": [("selected", '#050')],
                    "font": [("selected", 'Poetsen\ One -25 bold')]
                }
            }
        }
    )
    style.theme_use("PipBoy")

radiolist = [['91.0Mhz - RTS', 91.0],
             ['91.6Mhz - COULEUR3', 91.6],
             ['102.4Mhz - ROUGE FM', 102.4]]

selradio = 100
def main():
    def LaunchRadio():
        global selradio
        if radio.get() != selradio:
            selradio = radio.get()
            print('rtl_fm -M wbfm -r 24000 -f %s | aplay -r 24000 -f S16_LE' %int(radiolist[selradio][1]*1000000))
            frequence.set('%sMhz'%radiolist[selradio][1])
        else:
            print('stop process')
            selradio = 100
            radio.set(100)

    
    Window = Tk()
    styles()
    Window.config(cursor='none')
    Window.attributes('-fullscreen', True)
    Window.geometry('800x480')
    Window.title('PipBoy 5000')
    Window.configure(bg='black')

    hour = time.strftime('%d.%m.%Y  %H:%M:%S')
    dihour = Label(Window, text=hour, bg='black', foreground=green, font='Poetsen\ One -20 bold')
    dihour.grid(column=0, row=0, sticky='w')

    settingsButton = Button(Window, bg='black', fg=green, text='Settings', font='Poetsen\ One -20 bold', command=Window.destroy)
    settingsButton.grid(column=1, row=0, sticky='e')

    View = ttk.Notebook(Window, padding=10)

    
    Radio = Frame(View, bg='black')
    
    List = Frame(Radio, bg='black')
    radio = IntVar()
    radio.set(100)
    for x in range(len(radiolist)):
        Radiobutton(List,
                    text=radiolist[x][0],
                    variable=radio, value=x,
                    command=LaunchRadio,
                    indicatoron=False,
                    font='Poetsen\ One -25 bold',
                    bg='black',
                    fg=green,
                    activebackground=green,
                    activeforeground='black',
                    selectcolor='#050',
                    width=18,
                    offrelief='flat').pack(anchor='w')
    List.pack(anchor='nw', side='left')

    Setting = Frame(Radio, bg='black')
    frequence = StringVar()
    frequence.set('88.0Mhz')
    freq = Label(Setting, font='Poetsen\ one -75 bold', textvariable=frequence, bg='black', fg=green, width=8)
    freq.pack(anchor='center', pady=15, padx=32)
    prev = Button(Setting, text='<', font='Poetsen\ One -20 bold', bg='black', fg=green)
    prev.pack(anchor='w')
    Setting.pack(fill='both')

    
    Map = Frame(View, background='black')
    
    View.add(Radio, text='Radio')
    View.add(Map, text='Map')
    View.grid(column=0, row=1, columnspan=2)

    Window.mainloop()

main()
