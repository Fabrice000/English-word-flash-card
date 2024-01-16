from tkinter import *
from tkinter import messagebox
import pandas
import random
try:
    data = pandas.read_csv("/data/word_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("/data/english_word.csv")
    
data_list = data.to_dict(orient='records')
data_list1 = data_list.copy()
BACKGROUND_COLOR = "#B1DDC6" 
dictionary = {}
def add_new_word():
    if new_word.get() == "" or new_word_definition.get() == "":
        messagebox.showinfo(title="Oops",message="cna't not be a blank field")
    elif messagebox.askyesno(title="Save a new word",message=f"Save this word?\nWord:{new_word.get()}\nDefinition: {new_word_definition.get()}"):
        data_list1.append({"english":new_word.get(),"french":new_word_definition.get()})
        new_word.delete(0,END)
        new_word_definition.delete(0,END)
        data = pandas.DataFrame(data_list1)
        data.to_csv("/data/word_to_learn.csv",index=False)
    else:
        pass
def change_word():
    global dictionary, after_time
    window.after_cancel(after_time)
    # word_dict = { {row.english:row.french} for (index,row) in data.iterrows()}
    # print(word_dict)
    dictionary = random.choice(data_list1)
    canvas.itemconfig(canvas_image,image=image_background1)
    canvas.itemconfig(language,text="English",fill="black")
    canvas.itemconfig(word,text= dictionary["english"],fill="black")
    after_time = window.after(3000,func=translate)
    

    
def translate():
    
    canvas.itemconfig(canvas_image,image=image_background2)
    canvas.itemconfig(language,text="French",fill="white")
    canvas.itemconfig(word,text=dictionary["french"],fill="white")

def is_known():
    data_list1.remove(dictionary)
    change_word()
    data = pandas.DataFrame(data_list1)
    data.to_csv("/data/word_to_learn.csv",index=False)

    
        
window = Tk()

window.title("Flashy")

window.config(background=BACKGROUND_COLOR,padx=50,pady=50)

after_time = window.after(3000,func=translate)


image_background1 = PhotoImage(file= "/image/Background1.png")
image_background2 = PhotoImage(file="/image/background2.png")
canvas = Canvas(width=692,height=467,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas_image = canvas.create_image(346,234)
canvas.grid(column=1,row=1,columnspan=2,rowspan=2)
language = canvas.create_text(346,150,text="", font=("Ariel",40,"italic"))
word = canvas.create_text(346,234,text="", font=("Ariel",60,"bold"))
change_word()

# Entry
back_image = PhotoImage(file="/image/back.png")
canvas2 = Canvas(width=350,height=448,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas2.create_image(175,224,image=back_image)
canvas2.create_text(180,60,text="English word:",font=("Ariel",20,"italic"))
canvas2.grid(column=3,row=1,rowspan=2)
new_word = Entry(width=15,font=("Ariel",14,"italic"))
new_word.grid(column=3,row=1)
canvas2.create_text(180,300,text="French definition:",font=("Ariel",20,"italic"))
new_word_definition = Entry(width=15,font=("Ariel",14,"italic"))
new_word_definition.grid(column=3,row=2)
add_button = Button(text="Add",font=("Ariel",24,"bold"),command=add_new_word)
add_button.grid(column=3,row=3)


# button
cross_image = PhotoImage(file="/image/cross.png")
cross_button = Button(image=cross_image,highlightthickness=0,command=change_word)
cross_button.grid(column=1,row=3)
ok_image = PhotoImage(file="/image/ok.png")
ok_button = Button(image=ok_image,highlightthickness=0,command=is_known)
ok_button.grid(column=2,row=3)







window.mainloop()

