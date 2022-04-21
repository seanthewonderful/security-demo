import tkinter
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {} 

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orig_data = (pandas.read_csv("data/french_words.csv"))
    to_learn = orig_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=f"{current_card['French']}", fill="black")
    canvas.itemconfig(card_bg, image=card_front)
    flip_timer = window.after(3000, flip_card)
    print(current_card)
        
def flip_card():
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=f"{current_card['English']}", fill="white")
    canvas.itemconfig(card_bg, image=card_back)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")
    new_word()

window = tkinter.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

card_front = tkinter.PhotoImage(file="images/card_front.png")
card_back = tkinter.PhotoImage(file="images/card_back.png")
right = tkinter.PhotoImage(file="images/right.png")
wrong = tkinter.PhotoImage(file="images/wrong.png")

canvas = tkinter.Canvas(width=800, height=526)
card_bg = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = tkinter.Button(image=wrong)
wrong_button.config(highlightthickness=0, border=0, command=new_word)
wrong_button.grid(row=1, column=0)

right_button = tkinter.Button(image=right)
right_button.config(highlightthickness=0, border=0, command=is_known)
right_button.grid(row=1, column=1)


new_word()

window.mainloop()
