import random # Importing the random module to generate random numbers
print('Welcome to the dice simulator!')
x = 'y'  # Initializing x with 'y' to start the loop
while x == 'y': # Starting a loop that runs as long as the user wants to roll the dice
 num=random.randint(1,6)  # Generating a random number between 1 and 6
 # Printing the appropriate dice face based on the generated number
 if num == 1:
    print('---------')
    print('|       |')
    print('|   0   |')
    print('|       |')
    print('---------')
 if num == 2:
    print('---------')
    print('|       |')
    print('| 0   0 |')
    print('|       |')
    print('---------')
 if num == 3:
    print('---------')
    print('|   0   |')
    print('|   0   |')
    print('|   0   |')
    print('---------')
 if num == 4:
    print('---------')
    print('| 0   0 |')
    print('|       |')
    print('| 0   0 |')
    print('---------')
 if num == 5:
    print('---------')
    print('| 0   0 |')
    print('|   0   |')
    print('| 0   0 |')
    print('---------')
 if num == 6:
    print('---------')
    print('| 0   0 |')
    print('| 0   0 |')
    print('| 0   0 |')
    print('---------')
   
 x = input('press y to roll again') # Prompt the user to roll again by pressing 'y'