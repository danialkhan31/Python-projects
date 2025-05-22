import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

i = random.randint(0,2)

j = int(input("What you choose? Type 0 for rock ,1 for paper ,2 for scissors.\n"))
if j == 0:
    print(rock)
    print(f"computer choose{i}")
    if i == 0:
        print(rock)
        print("DRaw")
    elif i == 1:
        print(paper)
        print("You lose")
    else:
        print(scissors)
        print("you win")

elif j == 1:
    print(paper)
    print(f"computer choose {i}")
    if i == 0:
        print(rock)
        print("you win")
    elif i == 1:
        print(paper)
        print("Draw")
    else:
        print(scissors)
        print("you lose")

elif j == 2:
    print(scissors)
    print(f"computer choose {i}")
    if i == 0:
        print(rock)
        print("you lose")
    elif i == 1:
        print(paper)
        print("you win")
    else:
        print(scissors)
        print("Draw")

else:
    print("invalid")
