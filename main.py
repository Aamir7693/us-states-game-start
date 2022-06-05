import pandas as pd
import turtle
screen=turtle.Screen()
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
data=pd.read_csv("50_states.csv")
state_list=[]
xcord=[]
ycord=[]
input="true"
guessed_list=[]
for i in range(len(data)):
    state_list.append(data["state"][i])
    xcord.append(data["x"][i])
    ycord.append((data["y"][i]))
def actual():
    while True:
        idx,input=guessword()
        if input.lower()=="exit":
            screen.exitonclick()
            break
        else:
            if idx:
                tim=turtle.Turtle()
                tim.penup()
                tim.hideturtle()
                word=state_list[idx]
                x,y=xcord[idx],ycord[idx]
                tim.goto(x,y)
                tim.write(word)
                guessed_list.append(word)



def guessword():
    state_name = screen.textinput(title="Prompt",prompt="Enter the name of the state")
    word = state_name.title()
    if word in state_list:
        idx=state_list.index(word)
        return idx,word
    else:
        return None,word
def main():
    actual()
    print("Words to remember\n")
    for i in range(len(state_list)):
        if state_list[i] in guessed_list:
            continue
        else:
            print(state_list[i]+", ",end="\n")
    print(f"Total words guessed {len(guessed_list)}")
    print(f"Total words to learn {len(state_list)-len(guessed_list)}")


if __name__=="__main__":
    main()
screen.mainloop()





