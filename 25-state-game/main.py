import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

data = pd.read_csv("50_states.csv")
state_len = len(data)

guessed_states = []

while len(guessed_states) < state_len:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{state_len}  Guess the State",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        all_states = data.state.to_list()
        missing_states = [
            state for state in all_states if state not in guessed_states]
        to_learn_df = pd.Series(missing_states)
        to_learn_df.to_csv("states_to_learn.csv")
        break
    get_state = data[data['state'] == answer_state]
    if not get_state.empty:
        guessed_states.append(answer_state)
        found_state = get_state.iloc[0]
        writer.goto(x=found_state['x'], y=found_state['y'])
        writer.write(answer_state, align="center")
