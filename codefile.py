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
    "date", "eggplant", "fig", "grape", "grapefruit", "greenbean",
    "kiwi", "lemon", "lettuce", "lime", "mango", "nectarine", "onion",
    "orange", "papaya", "peach", "pear", "peas", "pineapple", "plum",
    "pomegranate", "potato", "pumpkin", "raspberry",
    "spinach", "squash", "strawberry", "tomato", "watermelon","pizza","burger",
    "chips","juice","bread","puff","fries","tacos","biscuits","paratha","paneer",
    "chaap","kebab","pasta","macroni","sphagetti","maggi","noodles"
]

list1=[]
list2=[]
dead=1
while True:
    num=random.randrange(0,len(food_items))
    guess0=food_items[num]
    guess01=guess0.upper()
    guess=list(guess01)
    if guess not in list1:
        list1.append(guess)
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
    abc=""
    if display2 == "":
        print("You did not enter anything")
        break
    elif display2 not in list2:
        if display2.upper() in guess:
            c=guess01.index(display2.upper())
            b[c]=display2.upper()
            for i in b:
                abc=abc+str(i)
            d=" ".join(abc)
        else:
            display1=display1+" "+display2.upper()
            print(Death[dead])
            dead=dead+1
            if dead<len(Death):
                print(display1)
                print(d)
                continue
            elif dead==len(Death):
                print("You ran out of chances")
                print("The correct word was",guess01)
                break
            
    elif display2 in list2:
        print("You have already entered the letter")
        print(d)
        continue

    list2.append(display2)
    print(display1)
    if d=="":
        print(" ".join(display3))
    elif abc!=guess01:
        print(d)
    elif abc==guess01:
        print(d)
        print("Congratulations!! You Won")
        break