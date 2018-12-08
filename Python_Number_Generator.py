import random

def generate():
    print("Number_Generator")
    print("----------------")

    inp = int(input("Maximum amount of the Number: "))
    inp2 = int(input("How many Numbers do you want to generate? "))
    print("----------------")

    for i in range(inp2):
        print(random.randint(0, inp))
    print("----------------")
    x = input("again or exit? ")
    
    if x == "again":
        generate()
    elif x == "exit":
        exit()
generate()


