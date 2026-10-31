capitals = {
    "Georgia": "Tbilisi",
    "Hungary": "Budapest",
    "Germany": "Berlin",
}

score = 0

for country, capital in capitals.items():
    guess = input(f"What's capital of {country}? ").lower()
    
    if guess != capital.lower():
        print("Wrong")
    else:
        print("Correct!")
        score += 1
    
    print(f"Score: {score}")