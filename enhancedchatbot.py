print("greetings of the day what is your name")
name = input("enter your name: ")

while True:
    
    mood = input("how are you feeling: ")

    if mood == "good":
        print("very good to hear")
    elif mood == "bad":
        print("sorry to hear")
    else:
        print("ok thanks for sharing")

    hobbies = input("what are your hobbies: ")

    
    choice = input("do you want to continue: ")
    
    if choice != "yes":
        break  

print("thanks have a good day.")