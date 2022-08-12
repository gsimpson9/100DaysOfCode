import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
file = '50_states.csv'
screen.addshape(image)
turtle.shape(image)

correct_answers = []

data = pd.read_csv(file)
all_states = data.state.to_list()


game_is_on = True
guessed_states = []
score = 0

while len(guessed_states) < 50:
    answer = screen.textinput(title=f'Guess the state {score}/50', prompt="What's another stat name?").title()
    if answer == 'Exit':
        states_to_learn = list(set(all_states) - set(guessed_states))
        df = pd.DataFrame(states_to_learn, columns=['States'])
        df.to_csv('states_to_learn.csv', index=False)
        break
    if answer in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data['state'] == answer]
        t.goto(x=int(state_data.x), y=int(state_data.y))
        t.write(state_data.state.item())
        guessed_states.append(state_data.state.item())
        score += 1



