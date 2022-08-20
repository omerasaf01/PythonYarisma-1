
from tkinter import *

class calculatorEvents:
    def __init__(self, TextInput):
        self.TextInput = TextInput
    def Add(self, item : str):
        self.TextInput.insert(END, item);
    def Result(self):
        try:
            result = str(self.TextInput.get())
            if result == "":
                pass
            else:
                result = eval(result)
                self.TextInput.delete(0, END)
                self.TextInput.insert(0, result)
        except:
            messagebox.showerror("Hata", "Hatalı işlem")

    def Delete(self):
        self.TextInput.delete(0, END)

class Clicks:
    def __init__(self, TextInput):
        self.events = calculatorEvents(TextInput)
    def onClick_ButtonZero(self):
        self.events.Add("0")
    def onClick_ButtonOne(self):
        self.events.Add("1")
    def onClick_ButtonTwo(self):
        self.events.Add("2")
    def onClick_ButtonThree(self):
        self.events.Add("3")
    def onClick_ButtonFour(self):
        self.events.Add("4")
    def onClick_ButtonFive(self):
        self.events.Add("5")
    def onClick_ButtonSix(self):
        self.events.Add("6")
    def onClick_ButtonSeven(self):
        self.events.Add("7")
    def onClick_ButtonEight(self):
        self.events.Add("8")
    def onClick_ButtonNine(self):
        self.events.Add("9")
    def onClick_ButtonResult(self):
        self.events.Result()
    def onClick_ButtonPartiton(self): #Çarpma
        self.events.Add("*")
    def onClick_ButtonMultiplication(self): # Bölme
        self.events.Add("/")
    def onClick_ButtonCollection(self): # Toplama
        self.events.Add("+")
    def onClick_ButtonExtraction(self): #Çıkarma
        self.events.Add("-")
    def onClick_ButtonDelete(self):
        self.events.Delete() #Del

if __name__ == "__main__":
    exit()