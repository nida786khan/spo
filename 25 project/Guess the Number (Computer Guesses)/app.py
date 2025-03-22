import random  

low, high = 1, 100  
feedback = ""  

while feedback != "c":  
    guess = random.randint(low, high)  
    feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()  
    if feedback == "h":  
        high = guess - 1  
    elif feedback == "l":  
        low = guess + 1  

print("🎉 Computer guessed it!")
