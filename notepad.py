from  tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file=None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file= askopenfilename(defaultextension=".txt", filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])

    if file=="":
        file=None

    else:
        root.title(os.path.basename(file)+ " - Notepad")
        TextArea.delete(1.0, END)
        f=open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad By Dev")


if __name__=='__main__':
    root=Tk()
    root.title("Untitled - Notepad")

    # NOT SURE Y THIS IS NOT WORKING
    #root.iconbitmap(1.jpg.jpg)
    p1=PhotoImage(file = "1.ico")
    root.iconphoto(False, p1)
    root.geometry("644x788")

    #adding text area
    TextArea= Text(root, font='Arial 16')
    file=None

    #for dynamic resizing
    TextArea.pack(expand=True, fill=BOTH)

    #Creating a menubar

    MenuBar=Menu(root)
    FileMenu=Menu(MenuBar, tearoff=0)

    ## HERE FILE MENU STARTS

    #to open new file
    FileMenu.add_command(label="New", command=newFile)

    #to open existing file
    FileMenu.add_command(label="Open", command=openFile)
    
    #to save current file
    FileMenu.add_command(label="Save", command=saveFile)

    #puts a line seperator
    FileMenu.add_separator()

    #to exit file
    FileMenu.add_command(label="Exit", command=quitApp)

    MenuBar.add_cascade(label="File", menu=FileMenu)

    #File Menu Ends

    #Edit Menu Starts
    EditMenu=Menu(MenuBar, tearoff=0)

    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    #Edit Menu ENDS

    #Help Menu Starts
    HelpMenu=Menu(MenuBar, tearoff=0)

    HelpMenu.add_command(label="About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    #Help Menu ENDS

    root.config(menu=MenuBar)

    #Adding Scrollbar
    ScrollBar= Scrollbar(TextArea)
    ScrollBar.pack(side=RIGHT, fill=Y)
    ScrollBar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=ScrollBar.set)

    root.mainloop()

    
    


'''
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()


def about():
    showinfo("Notepad", "Notepad by Code With Harry")

'''