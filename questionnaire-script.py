#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#To do:
#More questions
#Better ending of the quiz


# In[ ]:





# In[1]:





# In[12]:





# In[2]:


import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  

total_emissions = 0
average_emissions = 72500000

def calculate_sustainability_score(total):
    score = max(1, min(10, 10 - ((total / average_emissions) * 5)))
    return score


class SustainabilityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sustainability Questionnaire")

        self.total_emissions = 0
        self.current_question = 0

        self.title_frame = tk.Frame(root)
        self.title_frame.pack()

        title_text = "How Sustainable Are You?"
        tk.Label(self.title_frame, text=title_text, font=("Arial", 18, "bold")).pack(pady=10)

        subtitle_text = "A questionnaire to determine your sustainability score!"
        tk.Label(self.title_frame, text=subtitle_text, font=("Arial", 12)).pack(pady=5)

        self.load_image("footprint.png") 

        self.start_button = tk.Button(self.title_frame, text="Start", font=("Arial", 14), command=self.start_quiz)
        self.start_button.pack(pady=20)

    def load_image(self, image_path):
        """Load and display the image on the screen."""
        try:
            img = Image.open(image_path)
            self.image = ImageTk.PhotoImage(img)
            if hasattr(self, 'image_label'):
                self.image_label.config(image=self.image)
            else:
                self.image_label = tk.Label(self.title_frame, image=self.image)
                self.image_label.pack(pady=10)
        except Exception as e:
            print(f"Error loading image: {e}")
            tk.Label(self.title_frame, text="(Image not available)", font=("Arial", 10, "italic")).pack(pady=10)

    def start_quiz(self):
        """Transition from the title screen to the first question."""
        self.title_frame.pack_forget()  
        self.quiz_frame = tk.Frame(self.root)  
        self.quiz_frame.pack(pady=20)

        self.question_frame = tk.Frame(self.quiz_frame)
        self.question_frame.pack(pady=20)

        self.answer_entry = tk.Entry(self.quiz_frame, font=("Arial", 14))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self.quiz_frame, text="Submit Answer", command=self.submit_answer, font=("Arial", 14))
        self.submit_button.pack(pady=10)

        self.progress_label = tk.Label(self.quiz_frame, text="", font=("Arial", 12))
        self.progress_label.pack(pady=10)

        self.feedback_label = tk.Label(self.quiz_frame, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=10)

        self.questions = [
            self.question1, self.question2, self.question3, self.question4, self.calculate_score
        ]

        self.load_question()

    def load_question(self):
        self.answer_entry.delete(0, 'end')  # Clear answer entry field
        if self.current_question < len(self.questions):
            self.questions[self.current_question]()
        else:
            self.calculate_score()

# Question 1
    def question1(self):
        question = "1. How many hours a year do you fly in a plane? (Enter the amount of hours)"
        self.display_question(question, "airplane.png")  # Image for question 1

    def submit_answer(self):
        answer = self.answer_entry.get()
        try:
            if self.current_question == 0:
                numeric_answer = float(answer)
                points1 = numeric_answer * 90000
                self.total_emissions += points1
                self.feedback_label.config(text=f"You flew for {numeric_answer} hours and this emits on average {points1} grams of CO2.")
            elif self.current_question == 1:
                self.process_question2(answer)
            elif self.current_question == 2:
                numeric_answer = float(answer)
                points3 = numeric_answer * 185
                self.total_emissions += points3
                self.feedback_label.config(text=f"You used {numeric_answer} kWh of gas this year, emitting {points3} grams of CO2.")
            elif self.current_question == 3:
                numeric_answer = float(answer)
                points4 = numeric_answer * 95
                self.total_emissions += points4
                self.feedback_label.config(text=f"You drove {numeric_answer} kilometers, emitting {points4} grams of CO2.")

            self.current_question += 1
            self.load_question()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")
    
# Question 2
    def question2(self):
        question = "2. What is your diet? (Choose the diet closest to yours)"
        self.display_question(question, "diet.png")  

        self.options = {
            '1': ("Vegetarian", 1700000),
            '2': ("Vegan", 1500000),
            '3': ("Average", 2500000),
            '4': ("Meat lover", 3300000)
        }

        self.diet_choice = tk.StringVar(value="1")
        for key, value in self.options.items():
            tk.Radiobutton(self.question_frame, text=f"{value[0]} (CO2: {value[1]}g)", variable=self.diet_choice, value=key, font=("Arial", 12)).pack(anchor="w")

    def process_question2(self, answer):
        if answer in self.options:
            selected_option = self.options[answer]
            self.total_emissions += selected_option[1]
            self.feedback_label.config(text=f"Your diet ({selected_option[0]}) emits {selected_option[1]} grams of CO2 annually.")
        else:
            messagebox.showerror("Invalid choice", "Please choose a valid diet option.")
            self.current_question -= 1  
    
# Question 3
    def question3(self):
        question = "3. How much gas do you use a year? (in kWh)"
        self.display_question(question, "......png")

# Question 4 (Car Travel)
    def question4(self):
        question = "4. How many kilometers do you travel per car in a year? (Enter 0 if electric)"
        self.display_question(question, "car.png")

    def display_question(self, question, image_path):
        for widget in self.question_frame.winfo_children():
            widget.destroy()
        self.question_label = tk.Label(self.question_frame, text=question, font=("Arial", 14))
        self.question_label.pack(anchor="w")

        try:
            img = Image.open(image_path)
            self.image = ImageTk.PhotoImage(img)
            img_label = tk.Label(self.question_frame, image=self.image)
            img_label.pack(pady=10)
        except Exception as e:
            print(f"Error loading image: {e}")
            tk.Label(self.question_frame, text="(Image not available)", font=("Arial", 10, "italic")).pack(pady=10)

    def calculate_score(self):
        sustainability_score = calculate_sustainability_score(self.total_emissions)
        messagebox.showinfo("Quiz Completed", f"Your total sustainability score (CO2 emissions) is: {self.total_emissions} grams of CO2.\nYour sustainability score on a scale of 1 to 10 is: {sustainability_score:.2f}")
        self.root.quit()

root = tk.Tk()
app = SustainabilityApp(root)

root.mainloop()


# In[ ]:




