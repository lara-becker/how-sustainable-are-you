#I am changing something so I can upload this changed version locally (midterm feedback)

total_emissions = 0
average_emissions = 72500000

def calculate_sustainability_score(total):
    """
    Calculate the sustainability score based on the user's total CO2 emissions.
    
    Argument:
        total (float): The total CO2 emissions.
    
    Returns:
        float: A score between 1 and 10, where 5 represents having the same amount of CO2 emissions as the average of an EU person.
    """
    score = max(1, min(10, 10 - ((total / average_emissions) * 5)))
    return score

class SustainabilityApp:
    def start_quiz(self):
        """
        Start the quiz and print the introductory message.
        """
        print("How Sustainable Are You?\nA questionnaire to determine your sustainability score!\n")
        self.load_question()
        
        
    def __init__(self):
        """
        Load the first question and the total emission starts as zero.
        """
        self.total_emissions = 0
        self.current_question = 0
        self.questions = [
            self.question1, self.question2, self.question3, self.question4, self.calculate_score
        ]
        self.start_quiz()

    
    def load_question(self):
        """
        Load the next question or calculate the final sustainability score if all questions are completed.
        """
        if self.current_question < len(self.questions):
            self.questions[self.current_question]()
        else:
            self.calculate_score()

    def question1(self):
        """
        Ask the user how many hours they fly in a plane each year and calculate the CO2 emissions with the amount of hours.
        """
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

    def question2(self):
        """
        Ask the user to select their diet type and calculate the CO2 emission from the diet.
        """
        question = ("2. What is your diet? (Choose the diet closest to yours)\n"
                    "1: Vegetarian\n"
                    "2: Vegan\n"
                    "3: Average\n"
                    "4: Meat lover\n"
                    "Enter your choice: ")
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

    def question3(self):
        """
        Ask the user how much gas they use per year (in kWh) and calculate the CO2 emission.
        """
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

    def question4(self):
        """
        Ask the user how many kilometers they travel by car each year and calculate the  CO2 emission
        """
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
        """
        Calculate the user's total CO2 emissions and display their sustainability score on a scale from 1 to 10.
        """
        sustainability_score = calculate_sustainability_score(self.total_emissions)
        print(f"\nQuiz Completed!\nYour total sustainability score (CO2 emissions) is: {self.total_emissions} grams of CO2.")
        print(f"Your sustainability score on a scale of 1 to 10 is: {sustainability_score:.2f}")

if __name__ == "__main__":
    app = SustainabilityApp()

    
    
    
#Testing - I am checking whether the sustainability score is calculated correctly 

def test_questionnaire():
    assert  calculate_sustainability_score(72500000) == 5 #Average emissions should be a sustainability score of 5
    assert  calculate_sustainability_score(0) == 10 #zero emissions should give a sustainability score of 10
    
if __name__ == "__main__":
    test_questionnaire()

