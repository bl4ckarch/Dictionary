from tkinter import *
from tkinter import font
from PyDictionary import PyDictionary 
dictionary = PyDictionary()
root = Tk()

root.geometry("400x400")

def dict():
    meaning.config(text=dictionary.meaning(word.get())['noun'][0])
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get()))


Label(root, text="Dictionary by evaristegw",font=("helvetica 20 bold"),fg="green").pack(pady=10)

frame = Frame(root)
Label(frame,text="saisir le mot",font=("helvetica 17 bold")).pack(side=LEFT)
word = Entry(frame,font=("helvetica 16 bold"))
word.pack()
frame.pack(pady=12)

frame1 =Frame(root)
Label(frame1, text="signification - ", font=("helvetica 11 bold")).pack(side=LEFT)
meaning = Label(frame1, text="", font=("helvetica 10"))
meaning.pack()
frame1.pack(pady=10)

frame2 =Frame(root)
Label(frame2, text="synonym - ", font=("helvetica 11 bold")).pack(side=LEFT)
meaning = Label(frame2, text="", font=("helvetica 10"))
meaning.pack()
frame2.pack(pady=10)

frame3 =Frame(root)
Label(frame3, text="signification - ", font=("helvetica 11 bold")).pack(side=LEFT)
meaning = Label(frame3, text="", font=("helvetica 10"))
meaning.pack()
frame3.pack(pady=10)

Button(root,text="valider", font=("helvetica 16 bold"),command=dict).pack()

root.mainloop()