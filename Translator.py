from cgitb import text
from tkinter import *
from tkinter import font
from googletrans import Translator
from gtts import gTTS

def translation():
    n1 = entry_main.get()
    n2 = Translator()
    n3 = drop_down.get()
    
    if n3 == "Hindi":
        change = "hi"
    
    elif n3 == "English":
        change = "en"
    
    elif n3 == "Spanish":
        change = "es"
        
    elif n3 == "German":
        change = "de"
        
    elif n3 == "French":
        change = "fr"
        
    text_translate = n2.translate(n1, dest = change)
    text_translate = text_translate.text
    n4 = gTTS(text = text_translate, slow=False,lang = change)
    two_label.config(text = text_translate)

lang_option = [
    "Hindi",
    "English",
    "Spanish",
    "German",
    "French"
]

main = Tk()
main.geometry("800x300")
main.config(background="#d0deec")
main.resizable(False,False)
main.title("Translator")
main.iconbitmap("C:\\Users\\HP\\OneDrive\\Desktop\\py\\Translator\\Tr.ico")

entry_main = Entry(main, bg="white",font=("Arial",20,"bold"))
entry_main.place(x=20,y=40)

leb_entry = Label(main, text= "Enter text : ", fg= "black",font =("Arial",10,font.BOLD,font.ITALIC))
leb_entry.place(x=20,y=10)
leb_entry.config(background="#d0deec")

drop_down = StringVar()
drop_down.set("Select Language")

list_lang = OptionMenu(main, drop_down, *lang_option)
list_lang.configure(bg="yellow",fg="black",font=("Arial",16,font.ITALIC))
list_lang.place(x=400,y=40)

two_label = Label(main, text ="\t\t\t\t\t\t",bg="white", fg="red",font=("Arial",40,"bold"))
two_label.place(x=0,y=120)

two_label = Label(main,text="Translation", bg="white",fg="red",font=("Arial",40,font.BOLD))
two_label.place(x=250,y=120)

b = Button(main, text = "Translate !", bg="green", fg="white", font=("Arial",26,"bold"),borderwidth=0, command=translation)
b.place(x=300,y= 220)

main.mainloop()