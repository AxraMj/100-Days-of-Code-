import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "C:/Users/HP/100-Days-of-Code-/Day25/005 us-states-game-start/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data_path="C:/Users/HP/100-Days-of-Code-/Day25/005 us-states-game-start/us-states-game-start/50_states.csv"
data = pandas.read_csv(data_path)
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        path="C:/Users/HP/100-Days-of-Code-/Day25/005 us-states-game-start/us-states-game-start/states_to_learn.csv"
        new_data.to_csv(path)
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
