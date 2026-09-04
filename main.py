from turtle import Screen, Turtle

import pandas

tim = Turtle()

screen = Screen()

image=r"State_Quiz/blank_states_img.gif"

screen.addshape(image)

tim.shape(image)


# def genrated_axis(x,y):

#     print(x,y)

# screen.onscreenclick(genrated_axis)

# screen.mainloop()

#the upper comment code gives the extact position of the state by clicking on it and get the coordinates

data=pandas.read_csv(r"C:\Users\shali\Desktop\GITHUB_PROJECTS\State_Quiz\50_states.csv")

data_list=data["state"].to_list()

tom = Turtle()

tom.hideturtle()

tom.penup()


guessed_state=[]

count=0


while len(guessed_state)<50:

    
    answer = screen.textinput(
    title=f"{count}/50 State Correct ",
    prompt="Enter your Guess state:").title()

    if answer in data_list:

        guessed_state.append(answer)
        
        state=data[data.state==answer]

        tom.goto(state.x.item(),state.y.item())

        tom.write(answer)

        count+=1

    if answer=="Exit":

        Left_State=[n for n in data_list if n not in guessed_state ]

        new_list=pandas.DataFrame(Left_State)

        new_list.to_csv(r"State_Quiz\State_to_learn.csv")




screen.exitonclick()