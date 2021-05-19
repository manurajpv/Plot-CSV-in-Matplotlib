from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
import tkinter
import PIL
from PIL import ImageTk
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import filedialog as fd


root = Tk()
root.title('Datalogger')
#root.iconbitmap("/home/manuraj/Documents/Proj/Ploting/line-graph.ico")
root.geometry("200x300")
icon = tkinter.PhotoImage("/home/manuraj/Documents/Proj/Ploting/line-graph.ico")
#label = tkinter.Label(root, image = icon)
#label.pack()

def Upload_Ref():
    Upload_Ref.filename = fd.askopenfilename()
    print('Selected:', Upload_Ref.filename)
    messagebox.showinfo('File selected',str(Upload_Ref.filename))

def Upload_Data():
    Upload_Data.filename = fd.askopenfilename()
    print('Selected:', Upload_Data.filename)
    messagebox.showinfo('File selected',str(Upload_Data.filename))

importRef_button = Button(root, text='Open Reference CSV',fg='green', command=Upload_Ref)
importRef_button.pack(expand=True)

importData_button = Button(root, text='Open Measured CSV',fg='blue', command=Upload_Data)
importData_button.pack(expand=True)

def Graph ():
    df = pd.read_csv(Upload_Ref.filename)
    #time = np.arange(start=1, stop= len(df['Acceleration: X [raw] '])+1,step=1)
    plt.figure()
    plt.style.use('ggplot')
    plt.subplot(1, 2, 1)
    plt.xlabel('Time')
    plt.ylabel('Magnitude')
    plt.plot(df[' Cycle time [s] '], df['Acceleration: X [raw] '].astype(int), 'r',label='AccX')
    plt.plot(df[' Cycle time [s] '], df[' Acceleration: Y [raw] '], 'b',label='AccY')  
    plt.plot(df[' Cycle time [s] '], df[' Acceleration: Z [raw] '], 'g',label='AccZ')  
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.xlabel('Time')
    plt.ylabel('Magnitude')
    plt.plot(df[' Cycle time [s] '], df[' Pressure [raw] '], 'r',label='Press')
    plt.plot(df[' Cycle time [s] '], df[' Temperature [raw] '], 'r',label='Temp')
    plt.legend()

    df = pd.read_csv(Upload_Data.filename)
    plt.figure()
    plt.style.use('ggplot')
    plt.subplot(1, 2, 1)
    plt.xlabel('Time')
    plt.ylabel('Magnitude')
    plt.plot(df[' Cycle time [s] '], df['Acceleration: X [raw] '].astype(int), 'r',label='AccX') 
    plt.plot(df[' Cycle time [s] '], df[' Acceleration: Y [raw] '], 'b',label='AccY') 
    plt.plot(df[' Cycle time [s] '], df[' Acceleration: Z [raw] '], 'g',label='AccZ') 
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.xlabel('Time')
    plt.ylabel('Magnitude')
    plt.plot(df[' Cycle time [s] '], df[' Pressure [raw] '], 'r',label='Press')
    plt.plot(df[' Cycle time [s] '], df[' Temperature [raw] '], 'r',label='Temp')
    plt.legend()
    plt.show()

PlotRef_Button = Button(root,text="Graph it", command=Graph)
PlotRef_Button.pack()


root.mainloop()
