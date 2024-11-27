import tkinter as tk

import ttkbootstrap as ttk

def convert(): 
    mile_input = entryInt.get()
    miles_to_km = mile_input * 1.61

    output_string.set(miles_to_km)



#window
window = ttk.Window(themename = 'darkly') #journal theme is red, darkly is black
window.title('Miles2Km') #
window.geometry('400x400') #width and height of window 


#title
title_label = ttk.Label(master= window, text='Miles to Km',font=' Calibri 24 bold' ) #label needs to be inside a container and the only container present is the main window atm
title_label.pack()

#input feild 
input_feild = ttk.Frame(master=window)
entryInt = tk.IntVar()
entry = ttk.Entry(master=input_feild, textvariable= entryInt)
button = ttk.Button(master=input_feild, text= 'Convert', command= convert)
entry.pack(side= 'left', padx= 10) 
button.pack(side='left')
input_feild.pack(pady= 10)

#output 
output_string = tk.StringVar()
output_label = ttk.Label(
    master= window, text= 'Output',
    font=' Calibri 24 ',
    textvariable= output_string)
output_label.pack(pady= 5)

#run: call main loop method
window.mainloop()