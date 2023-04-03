print("Welcome to my random quiz")

playing = input("would you like to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! lets play")
score = 0 

answer = input("what biological order do frogs belong to? ")
if answer.lower() == "amphibians":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")
answer = input("Pickles start out as which vegetable? ")
if answer.lower() == "cucumber":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")
answer = input("If you tipped 20% on a $15 bill, how much would the tip be? ")
if answer.lower() == "$3.00":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")
answer = input("What month was Julius Caesar stabbed in? ")
if answer.lower() == "march":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")
answer = input("Banksy is an artist known for working with which medium? ")
if answer.lower() == "graffiti":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!" )
print("You got " + str(score/5 * 100) + "%. " )
print("Thanks for playing")
