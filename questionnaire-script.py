#!/usr/bin/env python
# coding: utf-8

# In[ ]:


total_emissions = 0
average_emissions = 72500000

def calculate_sustainability_score(total):
    score = max(1, min(10, 10 - ((total / average_emissions) * 5)))
    return score

class SustainabilityApp:
    def __init__(self):
        self.total_emissions = 0
        self.current_question = 0
        self.questions = [
            self.question1, self.question2, self.question3, self.question4, self.calculate_score
        ]
        self.start_quiz()

    def start_quiz(self):
        """Start the quiz and load questions one by one."""
        print("How Sustainable Are You?\nA questionnaire to determine your sustainability score!\n")
        self.load_question()

    def load_question(self):
        """Load the next question or calculate the final score."""
        if self.current_question < len(self.questions):
            self.questions[self.current_question]()
        else:
            self.calculate_score()

# Question 1
    def question1(self):
        question = "1. How many hours a year do you fly in a plane? (Enter the amount of hours): "
        try:
            numeric_answer = float(input(question))
            points1 = numeric_answer * 90000
            self.total_emissions += points1
            print(f"You flew for {numeric_answer} hours and this emits on average {points1} grams of CO2.")
            self.current_question += 1
            self.load_question()
        except ValueError:
            print("Invalid input, please enter a valid number.")
            self.question1()

# Question 2
    def question2(self):
        question = "2. What is your diet? (Choose the diet closest to yours)\n1: Vegetarian\n2: Vegan\n3: Average\n4: Meat lover\nEnter your choice: "
        self.options = {
            '1': ("Vegetarian", 1700000),
            '2': ("Vegan", 1500000),
            '3': ("Average", 2500000),
            '4': ("Meat lover", 3300000)
        }
        answer = input(question)
        if answer in self.options:
            selected_option = self.options[answer]
            self.total_emissions += selected_option[1]
            print(f"Your diet ({selected_option[0]}) emits {selected_option[1]} grams of CO2 annually.")
            self.current_question += 1
            self.load_question()
        else:
            print("Invalid choice, please try again.")
            self.question2()

# Question 3
    def question3(self):
        question = "3. How much gas do you use a year? (in kWh): "
        try:
            numeric_answer = float(input(question))
            points3 = numeric_answer * 185
            self.total_emissions += points3
            print(f"You used {numeric_answer} kWh of gas this year, emitting {points3} grams of CO2.")
            self.current_question += 1
            self.load_question()
        except ValueError:
            print("Invalid input, please enter a valid number.")
            self.question3()

# Question 4
    def question4(self):
        question = "4. How many kilometers do you travel per car in a year? (Enter 0 if electric): "
        try:
            numeric_answer = float(input(question))
            points4 = numeric_answer * 95
            self.total_emissions += points4
            print(f"You drove {numeric_answer} kilometers, emitting {points4} grams of CO2.")
            self.current_question += 1
            self.load_question()
        except ValueError:
            print("Invalid input, please enter a valid number.")
            self.question4()

    def calculate_score(self):
        sustainability_score = calculate_sustainability_score(self.total_emissions)
        print(f"\nQuiz Completed!\nYour total sustainability score (CO2 emissions) is: {self.total_emissions} grams of CO2.")
        print(f"Your sustainability score on a scale of 1 to 10 is: {sustainability_score:.2f}")

if __name__ == "__main__":
    app = SustainabilityApp()


# In[ ]:




