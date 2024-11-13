import easygui

easygui.msgbox("Welcome to the Interactive Quiz! Let's get started.", title="Quiz Time")

question1 = easygui.enterbox("What is your name?", title="Question 1")

question2 = easygui.enterbox("How old are you?", title="Question 2")

question3 = easygui.enterbox("What is your favorite color?", title="Question 3")

question4 = easygui.enterbox("What is your favorite hobby?", title="Question 4")

question5 = easygui.enterbox("What is your favorite food?", title="Question 5")

answers = f"""
Here are your answers:
1. Name: {question1}
2. Age: {question2}
3. Favorite Color: {question3}
4. Favorite Hobby: {question4}
5. Favorite Food: {question5}
"""


easygui.msgbox(answers, title="Your Answers")


easygui.msgbox("Thank you for participating!", title="End of Quiz")
