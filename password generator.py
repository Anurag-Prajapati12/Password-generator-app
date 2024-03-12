#Passwors generator in python
from tkinter import *
import string
import random
import pyperclip

root=Tk()
root.title("PASSWORD GENERATOR")
root.geometry("400x340")
root.configure(bg="#009999")

def generate():
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    numbers=string.digits
    character=string.punctuation
    all_=lower+upper+numbers+character
    med=lower+upper
    selection=choice.get()
    if selection==1:
        print("123")
        password=random.sample(lower,int(entry_length.get()))
        entry_password.insert(0,password)
        print(password)
    if selection==2:
        password=random.sample(med,int(entry_length.get()))
        entry_password.insert(0,password)
    if selection==3:
        password=random.sample(all_,int(entry_length.get()))
        entry_password.insert(0,password)

def copy():
    copy=entry_password.get()
    pyperclip.copy(copy)

def clear():
    print("f")
    choice.set(None)
    entry_length.delete(0,END)
    entry_password.delete(0,END)

    
choice=IntVar()

frame=LabelFrame(root)

#creating wigdets
label_title=Label(root,text="PASSWORD GENERATOR",padx=50,pady=10,font=(16),relief="solid",bg="#FF6666" )
label_weakRB=Radiobutton(frame,text="Weak",variable=choice,value=1,bg="#CCFF99")
label_mediumRB=Radiobutton(frame,text="Medium",variable=choice,value=2,bg="#CCFF99")
label_hardRB=Radiobutton(frame,text="Hard",variable=choice,value=3,bg="#CCFF99")
choice.set(None)
label_length=Label(root,text="Length",bg="#CCFF99")
entry_length=Entry(root,bg="#C0C0C0")
button_password=Button(root,text="Generate",command=generate,bg="#66B2FF")
entry_password=Entry(root,bg="#C0C0C0")
button_copy=Button(root,text="Copy",command=copy,bg="#66B2FF")
button_clear=Button(root,text="Clear",command=clear,bg="#66B2FF")

#placing widgets
label_title.pack(pady=20)
frame.pack(pady=10)
label_weakRB.grid(row=0,column=0)
label_mediumRB.grid(row=0,column=1)
label_hardRB.grid(row=0,column=2)
label_length.pack()
entry_length.pack(pady=10)
button_password.pack()
entry_password.pack(pady=10)
button_copy.pack()
button_clear.pack(pady=10)

root.mainloop()
