import tkinter as tk
window = tk.Tk()

nun = None
# schijf hier tussen je code
def Switch():
    background = window.cget('bg') #window.cget is basically een checklist
    if background == 'yellow':
        nun.configure(text = 'Lightswitch is off')

    

# schijf hier tussen je code

button = tk.Button(text='Press', bg="white==", fg="black")
button.pack(pady = 20, padx = 20)


window.mainloop()