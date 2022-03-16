# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 04:42:17 2020

@author: zain Rasheed
"""
import tkinter as tk
import time

window = tk.Tk()
window.title("track mouse")

def motion(event):
    time.sleep(0.1)
    x, y = event.x, event.y
    print(x, y)
    
window.bind('<Motion>', motion)
window.mainloop()