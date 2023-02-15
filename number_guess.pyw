import random
import tkinter
from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
import os



root=Tk()
root.title("Guessing Game")
root.iconbitmap("guess_icon.ico")

correct_num=random.randint(1,100) #defining random integer

#to create number string on entry widget
def num_enter(button_num):
    current_num=myInput.get()
    myInput.delete(0,END)
    myInput.insert(0,str(current_num)+str(button_num))
    return


li_click=[] #to count for submit button click

#checking input number and correct number after clicking submit button
def button_click(number):
    
    li_click.append(number)
    
    if(len(li_click)==1 and number==correct_num):
        status3=Label(root,text="Score: 5",relief=SUNKEN,anchor=E,padx=10,pady=10)
        status3.grid(row=12,column=0,columnspan=3,sticky=W+E)
        
        
        
    status1=Label(root,text="Guess used "+str(len(li_click))+" of 5",relief=SUNKEN,anchor=E,padx=10,pady=10)
    status1.grid(row=11,column=0,columnspan=3,sticky=W+E)
    status2=Label(root,text="Score: "+str(5-len(li_click)),relief=SUNKEN,anchor=E,padx=10,pady=10)
    status2.grid(row=12,column=0,columnspan=3,sticky=W+E)
    if(len(li_click)==5 and number!=correct_num):
        response=messagebox.askyesno("You Lost","Number was "+str(correct_num)+". Your score: 0. \nDo you wish to play again?")
        if response==1:
            root.quit()
            os.startfile("number_guess.pyw")
        else:
            root.quit()
        
    if(number==correct_num):
        status2=Label(root,text="Score: "+str(6-len(li_click)),relief=SUNKEN,anchor=E,padx=10,pady=10)
        status2.grid(row=12,column=0,columnspan=3,sticky=W+E)
        response1=messagebox.askyesno("You Win","Your score: "+str(6-len(li_click))+" \nYour are high on luck today.Go buy a lottery. \nDo you wish to play again?")
        if response1==1:
            root.quit()
            os.startfile("number_guess.pyw")
        else:
            root.quit()

    else:
        
        i=0
        while(i<len(li_click)):
            if(i==0):
                if(correct_num%2==0):
                    myLabel=Label(root,text="Wrong Guess! Hint: Number is Divisible by two")
                    myLabel.grid(row=3,column=0,columnspan=3)
                elif(correct_num%3==0):
                    myLabel=Label(root,text="Wrong Guess! Hint: Number is Divisible by three")
                    myLabel.grid(row=3,column=0,columnspan=3)
                elif(correct_num%5==0):
                    myLabel=Label(root,text="Wrong Guess! Hint: Number is Divisible by five")
                    myLabel.grid(row=3,column=0,columnspan=3)
                elif(correct_num%7==0):
                    myLabel=Label(root,text="Wrong Guess! Hint: Number is Divisible by seven")
                    myLabel.grid(row=3,column=0,columnspan=3)
                else:
                    for j in range(2,correct_num):
                        if(correct_num%j!=0):
                            myLabel=Label(root,text="Wrong Guess! Hint: Number is prime")
                            myLabel.grid(row=3,column=0,columnspan=3)
            elif(i==1):
                if(correct_num>=50):
                    myLabel=Label(root,text="Wrong Guess! Hint: Number is >=50")
                    myLabel.grid(row=4,column=0,columnspan=3)
                elif(correct_num<=50):
                    myLabel=Label(root,text="Wrong Guess! Hint: Number is <=50")
                    myLabel.grid(row=4,column=0,columnspan=3)
            elif(i==2):
                myLabel=Label(root,text="Wrong Guess! Hint: Number is between "+str(correct_num-10)+" and "+str(correct_num+12))
                myLabel.grid(row=5,column=0,columnspan=3)
            elif(i==3):
                myLabel=Label(root,text="Wrong Guess! Hint: Number is between"+str(correct_num-5)+" and "+str(correct_num+6))
                myLabel.grid(row=6,column=0,columnspan=3)
            i+=1
    
                
                
    return
    
#code for clear button            
def clear():
    myInput.delete(0,END)
    return

#Defining Buttons, entry field, labels
label1=Label(root,text="Guess the number between 1 to 100")
label2=Label(root,text="You have 5 guesses, Try your luck ;)")
myInput=Entry(root,width=50)
numButton_seven=Button(root,text="7",padx=50,pady=20,command=lambda:num_enter(7))
numButton_eight=Button(root,text="8",padx=50,pady=20,command=lambda:num_enter(8))
numButton_nine=Button(root,text="9",padx=50,pady=20,command=lambda:num_enter(9))
numButton_four=Button(root,text="4",padx=50,pady=20,command=lambda:num_enter(4))
numButton_five=Button(root,text="5",padx=50,pady=20,command=lambda:num_enter(5))
numButton_six=Button(root,text="6",padx=50,pady=20,command=lambda:num_enter(6))
numButton_one=Button(root,text="1",padx=50,pady=20,command=lambda:num_enter(1))
numButton_two=Button(root,text="2",padx=50,pady=20,command=lambda:num_enter(2))
numButton_three=Button(root,text="3",padx=50,pady=20,command=lambda:num_enter(3))
numButton_zero=Button(root,text="0",padx=50,pady=20,command=lambda:num_enter(0))
submit_Button=Button(root,text="Submit",command=lambda:button_click(int(myInput.get())),padx=34,pady=20)
clearButton=Button(root,text="Clear",padx=40,pady=20,command=clear)
status1=Label(root,text="Guess used 0 of "+str(5),relief=SUNKEN,anchor=E,padx=10,pady=10)
status2=Label(root,text="Score: "+str(5),relief=SUNKEN,anchor=E,padx=10,pady=10)



#Grid for widgets
label1.grid(row=0,column=0,columnspan=3)
label2.grid(row=1,column=0,columnspan=3)
myInput.grid(row=2,column=0,columnspan=3,pady=10)
numButton_seven.grid(row=7,column=0)
numButton_eight.grid(row=7,column=1)
numButton_nine.grid(row=7,column=2)
numButton_four.grid(row=8,column=0)
numButton_five.grid(row=8,column=1)
numButton_six.grid(row=8,column=2)
numButton_one.grid(row=9,column=0)
numButton_two.grid(row=9,column=1)
numButton_three.grid(row=9,column=2)
numButton_zero.grid(row=10,column=0)
submit_Button.grid(row=10,column=1)
clearButton.grid(row=10,column=2)
status1.grid(row=11,column=0,columnspan=3,sticky=W+E)
status2.grid(row=12,column=0,columnspan=3,sticky=W+E)


root.resizable(False,False)

root.mainloop()
