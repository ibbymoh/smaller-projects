from tkinter import *
from random import randint,choice
import pandas as pandas

BACKGROUND_COLOR = "#B1DDC6"
#Window
window = Tk()
window.config(height=700, width=1000,bg=BACKGROUND_COLOR)
window.title("flashy")

#reading the dictionary values
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("Arabic flashcards - Sheet1.csv")
finally:
    data_dict = data.to_dict(orient="records")


def get_random_number():
    randomnum = randint(0, 5001)
    return randomnum


random_number = get_random_number()

def dont_know_word():
    my_img.config(file="images/card_front.png")
    global random_number
    random_number = get_random_number()
    flashcard.itemconfig(card_title, text="Arabic")
    new_arabic_word = data_dict[random_number]["arabic"]
    flashcard.itemconfig(card_text,text=new_arabic_word)
    window.after(4000, swap_side_english)


def know_word():
    global random_number
    #removing from the current dictionary and creating a new one if we know the word
    data_dict.remove(data_dict[random_number])
    words_to_learn = pandas.DataFrame(data_dict)
    words_to_learn.to_csv("words_to_learn.csv")

    my_img.config(file="images/card_front.png")
    random_number = get_random_number()
    flashcard.itemconfig(card_title, text="Arabic")
    new_arabic_word = data_dict[random_number]["arabic"]
    flashcard.itemconfig(card_text,text=new_arabic_word)
    window.after(4000, swap_side_english)

def swap_side_english():
    my_img.config(file="images/card_back.png")
    flashcard.itemconfig(card_title,text="English")
    flashcard.itemconfig(card_text,text=data_dict[random_number]["english "])




#flashcard
flashcard = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
#when importing an image  unto a canvas, be careful to note that the image is not the canvas which automatically goes in the centre of the screen

my_img = PhotoImage(file="images/card_front.png")
flashcard.create_image(400,263,image=my_img)
flashcard.grid(row=0, column=0, columnspan=2, padx=50, pady=50)

#buttons
correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image,highlightthickness=0,command=know_word)
correct_button.grid(row=1,column=1,pady=50)

incorrect_image = PhotoImage(file="images/wrong.png")
incorrect_button = Button(image=incorrect_image,highlightthickness=0,command=dont_know_word)
incorrect_button.grid(row=1,column=0,pady=50)

#text

card_title = flashcard.create_text(400,150,text="Arabic", font=("Ariel",40,"italic"))
card_text = flashcard.create_text(400,300,text=data_dict[random_number]["arabic"], font=("Ariel",60,"bold"))


window.after(4000, swap_side_english)

window.mainloop()

