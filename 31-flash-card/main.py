import random
import tkinter as tk

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"


try:
    df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("./data/french_words.csv")
    df.to_csv("./data/words_to_learn.csv", index=False)

to_learn = df.to_dict(orient="records")


current_card = {}
flip_timer = None


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card.get("French"), fill="black")
    flip_timer = window.after(3000, flip_card)


def is_known():
    to_learn.remove(current_card)
    new_df = pd.DataFrame(to_learn)
    new_df.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word,
                      text=current_card.get("English"),
                      fill="white")


# ************************** UI ************************** #
window = tk.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_image = tk.PhotoImage(file="./images/card_front.png")
card_back_image = tk.PhotoImage(file="./images/card_back.png")

canvas = tk.Canvas(width=800, height=526,
                   bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(
    400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(
    400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = tk.PhotoImage(file="./images/right.png")
known_button = tk.Button(
    image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

wrong_image = tk.PhotoImage(file="./images/wrong.png")
unknown_button = tk.Button(
    image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

flip_timer = window.after(3000, func=flip_card)

next_card()


window.mainloop()
