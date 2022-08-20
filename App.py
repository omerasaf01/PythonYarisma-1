from tkinter import *
from Calculator import *

App = Tk()
App.title("Calculator")
App.geometry("289x230")
App.resizable(width=FALSE, height=FALSE)

TextInput = Entry(width=36)
TextInput.pack()

AppEvents = Clicks(TextInput)

Button(text = "1", command = AppEvents.onClick_ButtonOne, width = 6, height = 2, background = "#F2F3F5").place(x = 14, y = 25)
Button(text = "2", command = AppEvents.onClick_ButtonTwo, width = 6, height = 2, background = "#F2F3F5").place(x = 74, y = 25)
Button(text = "3", command = AppEvents.onClick_ButtonThree, width = 6, height = 2, background = "#F2F3F5").place(x = 138, y = 25)
Button(text = "4", command = AppEvents.onClick_ButtonFour, width = 6, height = 2, background = "#F2F3F5").place(x = 14, y = 75)
Button(text = "5", command = AppEvents.onClick_ButtonFive, width = 6, height = 2, background = "#F2F3F5").place(x = 74, y = 75)
Button(text = "6", command = AppEvents.onClick_ButtonSix, width = 6, height = 2, background = "#F2F3F5").place(x = 138, y =75)
Button(text = "7", command = AppEvents.onClick_ButtonSeven, width = 6, height = 2, background = "#F2F3F5").place(x = 14, y = 125)
Button(text = "8", command = AppEvents.onClick_ButtonEight, width = 6, height = 2, background = "#F2F3F5").place(x = 74, y = 125)
Button(text = "9", command = AppEvents.onClick_ButtonNine, width = 6, height = 2, background = "#F2F3F5").place(x = 138, y = 125)
Button(text = "0", command = AppEvents.onClick_ButtonZero, width = 6, height = 2, background = "#F2F3F5").place(x = 14, y = 175)
Button(text = "x", command = AppEvents.onClick_ButtonPartiton, width = 6, height = 2 , background = "#DBDCE0").place(x = 202, y = 25)
Button(text = "+", command = AppEvents.onClick_ButtonCollection, width = 6, height = 2, background = "#DBDCE0").place(x = 202, y = 75)
Button(text = "-", command = AppEvents.onClick_ButtonExtraction, width = 6, height = 2, background = "#DBDCE0").place(x = 202, y = 125)
Button(text = "/", command = AppEvents.onClick_ButtonMultiplication, width = 6, height = 2, background = "#DBDCE0").place(x = 202, y = 175)
Button(text = "=", command = AppEvents.onClick_ButtonResult, width = 6, height = 2, background = "#4286F5").place(x = 138, y = 175)
Button(text = "c", command = AppEvents.onClick_ButtonDelete, width = 6, height = 2, background = "#4286F5").place(x = 74, y = 175)

if __name__ == "__main__":
    App.mainloop();

else:
    exit()