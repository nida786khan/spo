import random  

words = ["python", "programming", "developer", "hangman"]  
word = random.choice(words)  
guesses = ""  
chances = 6  

while chances > 0:  
    display = "".join([letter if letter in guesses else "_" for letter in word])  
    print(display)  

    if "_" not in display:  
        print("🎉 You won!")  
        break  

    guess = input("Guess a letter: ").lower()  
    if guess in word:  
        guesses += guess  
    else:  
        chances -= 1  
        print(f"Wrong! {chances} chances left.")  

if "_" in display:  
    print(f"💀 Game over! The word was: {word}")  
