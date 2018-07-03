from tkinter import *
class abc:
    def path():
        global Ghanshyam
        string = Ghanshyam.get() 
        pathing = print ("r"+'"'+string+'"')
    
root = Tk()
root.title('Name')
Ghanshyam = Entry(root)
Ghanshyam.pack()
Ghanshyam.focus_set()
b = Button(root,text='okay',command=abc.path)
b.pack(side='bottom')
root.mainloop()
