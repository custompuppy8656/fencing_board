import tkinter
from tkinter import *
from tkinter import messagebox
import time

window = tkinter.Tk()

window.title("FENCING BOARD")

expression = ""#μια μεταβλητη για να γραψω στο gui μετα ο interpreter το υπολογιζει

####
####
####
#CORE CODE

def calculate(value):

    global expression
    expression += value
    result = ""
    if expression != "":
        try:
            result = eval(expression)

        except:
            result = "error"
            expression = ""
    # print in label_result
    label_point.config(text=result)
    expression = str(result)

def calculate1(value):

    global expression
    expression += value
    result = ""
    if expression != "":
        try:
            result = eval(expression)

        except:
            result = "error"
            expression = ""
    # print in label_result
    label_point1.config(text=result)
    expression = str(result)

####
####
####

#creating the gui
frame = tkinter.LabelFrame(window, width=50, bg='green', padx=15, pady=20)##Δημιουργια του frame
#στη πανω γραμμη τα padx και pady

frame.pack(padx=115, pady=110)#θεσεις του frame

#creating the gui
frame1 = tkinter.LabelFrame(window, width=50, bg='red', padx=15, pady=20)##Δημιουργια του frame

frame1.pack(padx=115, pady=15)#θεσεις του frame

#Ακολουθει frame για καρτες:κιτρινη,κοκκινη,μαυρη
frame_cards = tkinter.LabelFrame(window, width=50, bg='white', padx=15, pady=20)
frame_cards.pack(padx=115, pady=15)

minute = StringVar()
second = StringVar()

# setting the default value as 0

minute.set("00")
second.set("00")

# Use of Entry class to take input from the user

minuteEntry = Entry(window, width=3, font=("Arial", 18, ""),
                    textvariable=minute)
minuteEntry.place(x=130, y=20)

secondEntry = Entry(window, width=3, font=("Arial", 18, ""),
                    textvariable=second)
secondEntry.place(x=180, y=20)


def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(minute.get()) * 60 + int(second.get())
    except:
        print("Please input the right value")
    while temp > -1:

        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins, secs = divmod(temp, 60)

        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours = 0
        if mins > 60:
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)

        # using format () method to store the value up to
        # two decimal places
        #hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        # updating the GUI window after decrementing the
        # temp value every time
        window.update()
        time.sleep(1)

        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")

        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1


# button widget
btn = Button(window, text='S T A R T', bd='5',
             command=submit,bg='#00ff00')
btn.place(x=140, y=70)



###points label here must be two of them
#green team#####################################
label_point = tkinter.Label(frame, text="0", font=10, width=5, height=2)
label_point.grid(row=0, column=0)

##########Κουμπι για προσθεση ποντων
button_add = tkinter.Button(frame, text="+", font=10, width=2, height=1, bg='#00cc00' , command=lambda: calculate("+1"))
button_add.grid(row=1, column=0)

##########Κουμπι για αφαιρεση ποντων
button_minus = tkinter.Button(frame, text="-", font=10, width=2, height=1, bg='#00cc00' , command=lambda: calculate("-1"))
button_minus.grid(row=1, column=1)



#red team#######################################
label_point1 = tkinter.Label(frame1, text="0", font=10, width=5, height=2)
label_point1.grid(row=0, column=0)

##########Κουμπι για προσθεση ποντων
button_add = tkinter.Button(frame1, text="+", font=10, width=2, height=1, bg='#00cc00' , command=lambda: calculate1("+1"))
button_add.grid(row=1, column=0)

##########Κουμπι για αφαιρεση ποντων
button_minus = tkinter.Button(frame1, text="-", font=10, width=2, height=1, bg='#00cc00' , command=lambda: calculate1("-1"))
button_minus.grid(row=1, column=1)

#buttons inside frame_cards (3)
button_yellow_card = tkinter.Button(frame_cards,text = "Yellow card", font=10, width=5, height=2, bg="yellow")
button_yellow_card.grid(row=0, column=0)

button_red_card = tkinter.Button(frame_cards,text = "Red card", font=10, width=5, height=2, bg="red")
button_red_card.grid(row=0, column=1)

button_black_card = tkinter.Button(frame_cards,text = "Black card", font=10, width=5, height=2, bg="Black")
button_black_card.grid(row=0, column=2)


#main gui loop
window.mainloop()