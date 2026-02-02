print("Welcome to the Millionaire Game!")
print("You will be asekd a series of questions.")
print("Answer them correctly to win the game!")
print("Let's begin!\n")


#creating a list of list for the questions array
questions = [
    ["What is the capital of France?", "A] PARIS", "B] LONDON" , "C] BERLIN", "D] MADRID", "A"],
    ["What is the largest planet in our solar system?", "A] EARTH", "B] JUPITER", "C] SATURN", "D] MARS", "B"],
    ["What is the chemical symbol for gold?", "A] Au", "B] Ag", "C] Fe", "D] Pb", "A"],
    ["What is the smallest country in the world?", "A] VATICAN CITY", "B] MONACO", "C] SAN MARINO", "D] LIECHTENSTEIN", "A"],
    ["What is the largest mammal?", "A] ELEPHANT", "B] WHALE", "C] GIRAFFE", "D] HIPPOPOTAMUS", "B"],
    ["What is the capital of Japan?", "A] TOKYO", "B] SEOUL", "C] BEIJING", "D] TAIPEI", "A"],
    ["What is the currency of the United States?", "A] EURO", "B] DOLLAR", "C] POUND", "D] YEN", "B"],
    ["What is the largest ocean on Earth?", "A] ATLANTIC OCEAN ", "B] INDIAN OCEAN", "C] ARCTIC OCEAN", "D] PACIFIC OCEAN", "D"],
    ["What is the main ingredient in guacamole?", "A] TOMATO", "B] AVOCADO", "C] ONION", "D] PEPPER", "B"],
    ["What is the capital of Italy?", "A] ROME", "B] MILAN", "C] VENICE", "D] FLORENCE", "A"],
    ["What is the largest desert in the world?", "A] SAHARA", "B] ARCTIC", "C] ANTARCTIC", "D] GOBI", "A"],
    ["What is the chemical symbol for water?", "A] H2O", "B] CO2", "C] O2", "D] N2", "A"],
    ["What is the largest continent?", "A] AFRICA", "B] ASIA", "C] EUROPE", "D] NORTH AMERICA", "B"],
    ["What is the capital of Canada?", "A] OTTAWA", "B] TORONTO", "C] VANCOUVER", "D] MONTREAL", "A"],
    ["What is the main ingredient in hummus?", "A] CHICKPEAS", "B] LENTILS", "C] BEANS", "D] PEAS", "A"],
    ["What is the capital of Australia?", "A] SYDNEY", "B] CANBERRA", "C] MELBOURNE", "D] BRISBANE", "B"],
    ["What is the largest organ in the human body?", "A] HEART", "B] LIVER", "C] SKIN", "D] BRAIN", "C"],
    ["What is the capital of Germany?", "A] BERLIN", "B] MUNICH", "C] HAMBURG", "D] FRANKFURT", "A"],
    ["What is the main ingredient in pesto?", "A] BASIL", "B] PARSLEY", "C] CILANTRO", "D] OREGANO", "A"],
    ["What is the capital of Spain?", "A] MADRID", "B] BARCELONA", "C] SEVILLE", "D] VALENCIA", "A"]
]

score = 100000 # points per correct answer
sum = 0 
# fUNCTION TO ASK QUESTIONS AND RETURN THE ANSWER
for question in questions:
    
    print(question[0]) #print the question 
    print(question[1]) #print the first option
    print(question[2]) #print the second option
    print(question[3]) #print the third option
    print(question[4]) #print the fourth option

    answer = input("Enter your answer: (A/B/C/D): ").upper() # get the user input for the correct answer
    if answer == question[-1]: # matches the answer from user to the last element of list
        print("Correct answer!")
        sum += score
        print(f"You have earned {sum} points for this question.")

    else: 
        print("Oops! Incorrect Answer.")
        print(f"The Correct Answer is {question[-1]})")
        break # breaks the loop if the answer is incorrect
print(f"Your final score is {sum} points.\n")
print("Thank you for playing the Millionaire Game!")
print("Goodbye!\n")

