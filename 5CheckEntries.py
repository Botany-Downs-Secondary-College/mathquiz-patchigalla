#Creates GUI with classes, generates questions from Random 
#sprint4.py
#P.Patchigalla Feb 

from tkinter import *  #imports all modules of tool kit interface (Tkinter), * is called wildcard
from random import *

class MathQuiz: #OOP will have classes and funtions will be part of classes
    #Keep your widgets in instantiate (__init__) method, each instance (object) must have self. as prefix
    def __init__(self, parent): 

        """Widgets for frame 1"""
        self.frame1 = Frame(parent)
        self.frame1.grid(row = 0, column = 0)
        
        self.TitleLabel = Label(self.frame1, bg = "black", fg = "white", width = 30,  padx = 30, pady = 10,
                       text = "Welcome to Math Quiz", font=("Times", "16", "bold italic"))
        self.TitleLabel.grid(columnspan = 2)
        
        self.NameLabel = Label(self.frame1, text = "Name", width = 20, font=("Times", "14", "bold italic"))
        self.NameLabel.grid (row = 2, column = 0, sticky = W)
        
        """checking to see something entered"""
        self.name = StringVar()
        self.name.set("")
        self.NameEntry = Entry(self.frame1, textvariable = self.name, width = 20) #Text box
        self.NameEntry.grid(row = 2, column = 1, sticky = W)
        
        self.AgeLabel = Label(self.frame1, text = "Age", width = 20, font=("Times", "14", "bold italic"))        
        self.AgeLabel.grid (row = 3, column = 0, sticky = W)
        
        self.age = IntVar()
        self.age.set("")
        self.AgeEntry = Entry(self.frame1, width = 20, textvariable = self.age) #Text box
        self.AgeEntry.grid(row = 3, column = 1, sticky = W)  
        
        self.SelectLabel = Label(self.frame1, text = "Select difficulty", width = 20, font=("Times", "14", "bold italic"))
        self.SelectLabel.grid (row = 5, column = 0, sticky = W) 
        
        self.warning = Label(self.frame1, text = "")
        self.warning.grid(row = 4, column = 1, columnspan = 3)        
               
        
        #Create Radio buttons
        self.radio_var = StringVar()
        self.radio_var.set(1)
        
        self.rb1 = Radiobutton(self.frame1, width = 20, value = 1, variable = self.radio_var, text = "Easy", anchor = W)
        self.rb1.grid(row = 6, column =0)
        self.rb2 = Radiobutton(self.frame1, width = 20, value = 2, variable = self.radio_var, text = "Medium", anchor = W)
        self.rb2.grid(row = 7, column =0)
        self.rb3 = Radiobutton(self.frame1, width = 20, value = 3, variable = self.radio_var, text = "Hard",anchor = W)
        self.rb3.grid(row = 8, column =0)        
        
        self.button1 = Button(self.frame1, text = "Next" , anchor = W, command = self.show_frame2)
        self.button1.grid(row = 9, column = 1)
        
        """Widgets for frame 2"""
        self.frame2 = Frame(parent, height = "450", width = "400") #notice grid() method is missing here          
        
        self.questions = Label(self.frame2, bg = "black", fg = "white", width = 20,  padx = 30, pady = 10,
                               text = "Quiz Questions", font=("Times", "14", "bold italic"))
        self.questions.grid(columnspan = 2)
        
        self.QuestionLabel = Label(self.frame2, text ="", width =15, height = 3) #empty lable to print questions
        self.QuestionLabel.grid(row = 1, column = 0, sticky = W)        
        
        self.home = Button(self.frame2, text = "Home" , anchor = W, command = self.show_frame1)
        self.home.grid(row = 2, column = 0)   
        
        self.next_btn = Button(self.frame2, text = "Next", width = 5, command = self.next_problem, relief = RIDGE)
        self.next_btn.grid(row = 2, column = 1)             
      
    def show_frame2(self):
        try:
            
            #instance created to check if input data is correct for the variables
            if self.name.get() == "":
                self.warning.configure(text = "Please enter your name")
                self.NameEntry.focus()
            elif self.name.get().isalpha() == False:
                self.warning.configure(text = "Please enter text")
                self.NameEntry.delete(0, END)
                self.NameEntry.focus()            
            elif self.AgeEntry.get() == "" :
                self.warning.configure(text = "Please enter a number")
                self.AgeEntry.delete(0, END) 
            elif self.age.get() >= 12:
                self.warning.configure(text = "Your are too old to play this game!!!")
                self.AgeEntry.delete(0, END)
            elif self.age.get() <= 0:
                self.warning.configure(text = "Please enter a number greater than 0")
                self.AgeEntry.delete(0, END)
            elif self.age.get() <=7:
                self.warning.configure(text = "Oh No! Your too young to play this game!!")
        
            else:
                self.frame1.grid_remove()
                self.frame2.grid(row = 1, columnspan = 4)
                self.next_problem()
        
        except ValueError:
            self.warning.configure(text = "Please enter a number")
            self.AgeEntry.delete(0, END)
            self.AgeEntry.focus()
            

               
    def show_frame1(self):
        self.frame2.grid_remove() #removes frame 2
        self.frame1.grid()
        
    def next_problem(self):
        """ Creates a problem, stores the correct answer """
        x = randrange(10)
        y = randrange(10)
        self.answer = x + y
        
        problem_text = str(x) + "  +  " + str(y) + "  = "
        self.QuestionLabel.configure(text = problem_text)
       
    

#code in the main routine
if __name__ == "__main__": #checking to see class name is the main module
    root = Tk()  #root is a variable that calls the module to create GUI
    frames = MathQuiz(root)
    root.title("OOP") #Window title appears on top left
    root.mainloop()



