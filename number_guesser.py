import random


def guess(y):
    random_number =random.randint(1,y)
    guess=0
    
    while guess!= random_number:
        guess =int(input(f'Guess a random number from 1 to {y} \n'))
        if guess<random_number:
            print("too low")    
        elif guess>random_number:
            print("too high")
        
        
    print(f'yay u guessed {random_number}')
    
    
    
def computer_guess(x):
    low=1
    high=x
    feedback=''
    
    while feedback!="c":
        if low!= high:
            
            guess=random.randint(low, high)
        else:
            guess=low
             
        feedback=input(f'is {guess} too high (h), too low (l), or correct (c)? ').lower()
        if feedback =="h":
            high=guess -1
        elif feedback=="l":
            low=guess+1
    print(f"yay the computer guessed {guess}")
    
    
initprompt= input("Would you like to guess a random number or would you like the computer to guess a number? (me,computer) ").lower()

range= int(input(" What is the range of the number? 1-? "))

if initprompt =="me":
    guess(range)
    
else:
    computer_guess(range)