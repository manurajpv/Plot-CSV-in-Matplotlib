from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#from tkinter import filedialog
import csv
import tkinter
import PIL
from PIL import ImageTk
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.defchararray import index
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo



root = Tk()
root.title('Datalogger')
#root.iconbitmap("/home/manuraj/Documents/Proj/Ploting/line-graph.ico")
root.geometry("400x400")
icon = tkinter.PhotoImage("/home/manuraj/Documents/Proj/Ploting/line-graph.ico")
#label = tkinter.Label(root, image = icon)
#label.pack()

def UploadAction():
    UploadAction.filename = fd.askopenfilename()
    print('Selected:', UploadAction.filename)
    messagebox.showinfo('File selected',str(UploadAction.filename))

import_button = Button(root, text='Open CSV',fg='green', command=UploadAction)
import_button.pack(expand=True)

def Graph():
    df = pd.read_csv(UploadAction.filename)
    time = np.arange(start=1, stop= len(df['Acceleration: X [raw] '])+1,step=1)
    print(df['Acceleration: X [raw] '])
    
    plt.style.use('ggplot')
    plt.subplot(1, 2, 1)
    plt.xlabel('Time')
    plt.ylabel('Magnitude')
    plt.plot(df[' Cycle time [s] '], df['Acceleration: X [raw] '].astype(int), 'r',label='AccX') # plotting t, a separately 
    plt.plot(df[' Cycle time [s] '], df[' Acceleration: Y [raw] '], 'b',label='AccY') # plotting t, b separately 
    plt.plot(df[' Cycle time [s] '], df[' Acceleration: Z [raw] '], 'g',label='AccZ') # plotting t, c separately 
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.xlabel('Time')
    plt.ylabel('Magnitude')
    plt.plot(df[' Cycle time [s] '], df[' Pressure [raw] '], 'r',label='Press')
    plt.plot(df[' Cycle time [s] '], df[' Temperature [raw] '], 'r',label='Temp')
    plt.legend()
    plt.show()
    


Plot_Button = Button(root,text="Graph it", command=Graph)
Plot_Button.pack()

root.mainloop()
