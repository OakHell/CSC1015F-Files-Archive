print("""Welcome to the Biology Expert
-----------------------------
Answer the following questions by selecting from among the options.""")

userInput= input("The skeleton is (internal/external)?\n")
if userInput=="external":
    animal="Arthropod"
else:
    userInput=input("The fertilisation of eggs occurs (within the body/outside the body)?\n")
    if userInput=="outside the body":
        userInput=input("It lives (in water/near water)?\n")
        if userInput=="in water":
            animal="Fish"
        else:
            animal="Amphibian"
    else:
        userInput=input("Young are produced by (waterproof eggs/live birth)?\n")
        if userInput=="live birth":
            animal="Mammal"
        else:
            userInput=input("The skin is covered by (scales/feathers)?\n")
            if userInput=="scales":
                animal="Reptile"
            else:
                animal="Bird"

print(f"Type of animal: {animal}")