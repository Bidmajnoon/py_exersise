from time import strftime
import tkinter as tk
def digit_clock():
    curent_time = strftime('%H:%M:%S')
    label.config(text = curent_time)
    label.after(1000, digit_clock)
    
window = tk.Tk()
window.title("digital clock")
label = tk.Label(window, font=('Davat', 100) ,fg ='blue',bg='yellow')
label.pack(pady=200)
digit_clock()
window.mainloop()
