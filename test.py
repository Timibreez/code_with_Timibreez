"""Conditional Statements Practice"""
points = 174

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)


'''
You decide you want to play a game where you are hiding
a number from someone.  Store this number in a variable
called 'answer'.  Another user provides a number called
'guess'.  By comparing guess to answer, you inform the user
if their guess is too high or too low.

Fill in the conditionals below to inform the user about how
their guess compares to the answer.
'''
answer = 12
guess = 13

if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
    result = "Oops!  Your guess was too high."
elif guess == answer:
    result = "Nice!  Your guess matched the answer!"

print(result)


'''
Depending on where an individual is from we need to tax them
appropriately.  The states of CA, MN, and
NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
Use this information to take the amount of a purchase and
the corresponding state to assure that they are taxed by the right
amount.
'''
state = 'CA'
purchase_amount = 25000

if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(
        state,
        total_cost)

elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(
        state,
        total_cost)

elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(
        state,
        total_cost)

print(result)

'''
Using the truth values to solve the
conditional statements practice above
'''
points = 250  # use this as input for your submission

# establish the default prize value to None
prize = None


# use the points value to assign prizes to the correct prize names
if points <= 50:
    prize = 'wooden rabbit'
elif points <= 150:
    prize = prize
elif points <= 180:
    prize = 'wafer-thin mint'
else:
    prize = 'penguin'


# use the truth value of prize to assign result to the correct prize
if prize:
    result = 'Congratulations! You won a {}!'.format(prize)
else:
    result = 'Oh dear, no prize this time.'


print(result)

'''
Iterating through dictionaries
'''

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

print("Iterating through keys:")
for key in cast:
    print(key)

print("\nIterating through keys and values:")
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list): 
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The sum of the odd numbers added is: {}".format(list_sum))
