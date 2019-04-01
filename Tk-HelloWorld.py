# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:48:19 2019

@author: 18pt16
"""
# 1 million th prime : 15485863 

import tkinter as tk
import tkMessageBox

def helloworld():
    tkMessagebox.showinfo("Hello world")
  
top = tk.Tk()

B = tk.Button(top,text="hello",command = helloworld)
B.pack()

top.mainloop()
