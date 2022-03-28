import tkinter as tk
window = tk.Tk()


# schijf hier tussen je code
def toggle():
    if button.config('text')[-1] == 'Pressed':
        button.config(text = 'Press')
        window.config(bg = 'black')
        print('lightswitch is press')
    else:
        button.config(text = 'Pressed')
        window.config(bg = 'yellow')
        print('lightswitch is pressed')
    

# schijf hier tussen je code

button = tk.Button(text='Press', width = 10, command = toggle)
button.pack(pady = 20, padx = 20)


window.mainloop()