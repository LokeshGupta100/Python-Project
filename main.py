import pyttsx3
import random
engine=pyttsx3.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',rate-50)
engine.say("it is a game of rock paper and scissors in which you have to enter your move to play with computer so please write from rock paper and scissors and dive into this amazing game ")
engine.runAndWait()
list=["Rock","paper","Scissors"]
move=random.choice(list)
while True:
    yourturn=input("Enter your move:")
    if(move=="Rock"and yourturn=="Rock"):
        print("DRAW")
        engine.say("draw")
        engine.runAndWait()
    elif(move=="Rock"and yourturn=="Paper"):
        print("YOU WIN")
        engine.say("you win and game over")
        engine.runAndWait()
        print("-------GAME OVER----------")
        break     
    elif(move=="Rock"and yourturn=="Scissors"):
        print("YOU LOSE")
        engine.say("you lose")
        engine.runAndWait()
    elif(move=="Paper"and yourturn=="Rock"):
        print("YOU LOSE")
        engine.say("you lose")
        engine.runAndWait()
    elif(move=="Paper"and yourturn=="Paper"):
        print("DRAW")
        engine.say("draw")
        engine.runAndWait()
    elif(move=="Paper"and yourturn=="Scissors"):
        print("YOU WIN")
        engine.say("you win and game over")
        engine.runAndWait()
        print("-------GAME OVER----------")
        break
    elif(move=="Scissors"and yourturn=="Rock"):
        print("YOU WIN")
        engine.say("you win and game over")
        engine.runAndWait()
        print("-------GAME OVER----------")
        break
    elif(move=="Scissors"and yourturn=="Paper"):
        print("YOU LOSE")
        engine.say("you lose")
        engine.runAndWait()
    elif(move=="Scissors"and yourturn=="Scissors"):
        print("DRAW")
        engine.say("draw")
        engine.runAndWait()
print("-------GAME OVER----------")
