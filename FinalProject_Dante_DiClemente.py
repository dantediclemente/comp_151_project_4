#Dante DiClemente, 5-4-14, Hangman, Comp 151, Prof. Black

import urllib.request
import random
import tkinter

#The writing below until the next comment writes the code for the intial canvas

window = tkinter.Tk()
window.title("Hangman")
canvas = tkinter.Canvas(window,width=800,height=450)
canvas.pack()

canvas.create_line(25,300,125,300,fill="black")
canvas.create_line(50,300,50,100,fill="black")
canvas.create_line(50,100,100,100,fill="black")
canvas.create_line(100,100,100,125,fill="black")

wordpage=urllib.request.urlopen("http://web.mit.edu/freebsd/head/share/dict/web2").read()
wordpage=str(wordpage).replace("\\n","\n").split() 

numberOfWords = len(wordpage)
randomNumber = round(random.random()*numberOfWords)
myWord = wordpage[randomNumber]
myWord = list(myWord)
reveal = []
for i in range(len(myWord)):
    reveal.append(False)
print(myWord)
print(reveal)

x1 = 25
x2 = 50
for i in range(len(myWord)):
    if (reveal[i] == False):
        canvas.create_line(x1,400,x2,400,fill="black")
        
    x1 += 50
    x2 += 50

#The loop that keeps going until you have guessed more than six letters wrong

badguesses = 0

while(badguesses < 6):
    foundLetter = False 
    userGuess = input("What letter would you like to guess? ")
    for i in range(len(myWord)):
        if (userGuess == myWord[i]):
            reveal[i] = True
            foundLetter = True

#prints the letter if you got it correct           
            x1 = 25
            x2 = 50
            for i in range(len(myWord)):
                if (reveal[i] == False):
                    canvas.create_line(x1,400,x2,400,fill="black")
                if (reveal[i] == True):
                    canvas.create_text(x1 + 12.5,393, text=myWord[i])
                x1 += 50
                x2 += 50

#how the game knows if you won and ends the game and also tells you you won
                all = True
            for i in range(len(reveal)):
                if reveal[i] == False:
                    all = False
            if all == True:
                print("You Win!")
                badguesses = 7 
            canvas.update()

# Below is how I drew the body for the hangman
                
    if (foundLetter == False):
        badguesses += 1
    if badguesses == 1:
        coord = 75, 125, 125, 175
        canvas.create_arc(coord, start=0, extent=359)
        canvas.update()
    if badguesses == 2:
        canvas.create_line(100,200,100,250,fill="black")
        canvas.update()
    if badguesses == 3:
        canvas.create_line(100,185,75,225,fill="black")
        canvas.update()
    if badguesses == 4:
        canvas.create_line(100,250,75,275,fill="black")
        canvas.update()
    if badguesses == 5:
        canvas.create_line(100,185,125,225,fill="black")
        canvas.update()
    if badguesses == 6:
        canvas.create_line(100,250,125,275,fill="black")
        canvas.update()
        print("Game Over")

        
    


    
    
