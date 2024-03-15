import random

Death = ['''
    +---+
         |
         |
         |
        ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

food_items = [
    "apple", "apricot", "avocado", "banana", "blackberry", "blueberry",
    "carrot", "cherry", "coconut", "corn", "cucumber",
    "date", "eggplant", "fig", "grape", "grapefruit", "green bean",
    "kiwi", "lemon", "lettuce", "lime", "mango", "nectarine", "onion",
    "orange", "papaya", "peach", "pear", "peas", "pineapple", "plum",
    "pomegranate", "potato", "pumpkin", "raspberry",
    "spinach", "squash", "strawberry", "tomato", "watermelon","pizza","burger"
    "chips","juice","bread","puff","fries","tacos","biscuits","paratha","paneer",
    "chaap","kebab","pasta","macroni","sphagetti","maggi","noodles"

]
list1=[]
#list2=[]
def Main():
    dead=1
    while True:
        list2=[]
        num=random.randrange(0,len(food_items))
        guess0=food_items[num]
        guess01=guess0.upper()
        guess011=" ".join(guess01)
        guess=list(guess01)
        if guess01 not in list1:
            print(guess01)
            list1.append(guess01)
            break
        else: 
            continue

    display1= "Wrong Guess:"
    display3="_"*len(guess)
    b=list(display3)
    print(" ".join(display3))
    d=""
    while True:
        display2= input("Guess a letter:")
        if len(display2)<=1 and display2.isalpha():
            if display2 == "":
                print("You did not enter anything")
                break
            elif display2 not in list2:
                if display2.upper() in guess:
                    for i in range(len(guess)):
                        if guess[i] == display2.upper():
                            guess[i] = "|"  
                            b[i] = display2.upper()  
                    d=" ".join(b)
                else:
                    display1=display1+" "+display2.upper()
                    print(Death[dead])
                    dead=dead+1
                    if dead<len(Death):
                        print(display1)
                    elif dead==len(Death):
                        print("You ran out of chances")
                        print("The correct word was",guess01)
                        break

            elif display2 in list2:
                print("You have already entered the letter")
                print(d)
                continue

            list2.append(display2)


            if d=="":
                print(" ".join(display3))
            elif d!=guess011:
                print(d)
            elif d==guess011:
                print(d)
                print("Congratulations!! You Won")
                break
        else:
            print("Enter single letter only!!")
            print(d)
    choice = input("Enter choice(y/n):")
    if choice.lower() == "y":
        Main()
    else:
        None

Main()