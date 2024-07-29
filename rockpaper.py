from tkinter import *
import random

#MAIN FRAME
main_frame=Tk()
main_frame.geometry('500x450+500+200')
main_frame.title("ROCK-PAPER-SCISSOR")
main_frame.configure(background="#232F34")
main_text=Label(main_frame,text="ROCK-PAPER-SCISSOR",font=('Areial',18,'bold'),bg='#232F34',fg='#F9AA33')
main_text.pack()

#BUTTON FRAME 1
button_frame1=Frame(main_frame,bg="#232F34")
button_frame1.place(x=50,y=100)
Button(button_frame1,text="Rock",font=('Areial',18,'bold'),bg='#F9AA33',command=lambda:click('Rock')).pack(padx=20)

#BUTTON FRAME 2
button_frame2=Frame(main_frame,bg="#232F34")
button_frame2.place(x=150,y=100)
Button(button_frame2,text="Paper",font=('Areial',18,'bold'),bg='#F9AA33',command=lambda:click('Paper')).pack(padx=20)

#BUTTON FRAME 3
button_frame3=Frame(main_frame,bg="#232F34")
button_frame3.place(x=250,y=100)
Button(button_frame3,text="Scissor",font=('Areial',18,'bold'),bg='#F9AA33',command=lambda:click('Scissor')).pack(padx=20)

#Label For User Choice
user_label=Label(text=" ",font=("Areial",14,'bold'),bg="#232F34",fg='#F9AA33')
user_label.place(x=50,y=200)

#Label For Bot Choice
computer_label=Label(text=" ",font=("Areial",14,'bold'),bg="#232F34",fg='#F9AA33')
computer_label.place(x=290,y=200)

#Label for Result
res=Label(main_frame,text=" ",font=("Areial",18),bg="#232F34",fg='#F9AA33')
res.place(x=100,y=250)

#functiom for game
def click(choice):
    res.config(text="")
    user_label.config(text=f"your choice is:{choice}")
    choices = ['Rock', 'Paper', 'Scissor']
    computer_choice = random.choice(choices)
    computer_label.config(text=f"Bot choice is:{computer_choice}")
    def choice_res():
        if choice == computer_choice:
            result = "It's a tie!"
        elif (choice == 'Rock' and computer_choice == 'Scissors') or (choice == 'Paper' and computer_choice == 'Rock') or (choice == 'Scissors' and computer_choice == 'Paper'):
            result = f"You win! Bot chose  { computer_choice}."
        else:
            result = f"You Lost!! Bot chose  { computer_choice}."
        res.config(text=result)
    #Delay for the result in milliseconds
    main_frame.after(2000,choice_res) 
main_frame.mainloop()

