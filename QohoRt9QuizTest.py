# This is a recreation of the QohoRt 9 buzzfeed quiz originally made by Kaylyn


# The following lists are used to store names of each member and their scores:
Members = ['Aravinth', 'Daniel', 'Kaylyn', 'Lance', 'Roy', 'Sam']
QuestionAnswers = []

# Import counter for determining who the user is most like and for determining likeness percentages

from collections import Counter

# Question 1

Q1Input = input('Question 1: Choose a time by typing one of the following letter options: \n a) 0:00  b) 1:23:21  c) 11:11  d) 3:33  e) 10:05 f) 12:00    ')

if Q1Input == 'b':
    QuestionAnswers.append(0)
elif Q1Input == 'd':
    QuestionAnswers.append(3)
elif Q1Input == 'a':
    QuestionAnswers.append(5)
elif Q1Input == 'c':
    QuestionAnswers.append(1)
elif Q1Input == 'e':
    QuestionAnswers.append(2)
elif Q1Input == 'f':
    QuestionAnswers.append(4)

# Question 2

Q2Input = input('\n Question 2: Select your ideal travel destination by typing one of the following letter options: \n a) Australia  b) Japan  c) Singapore  d) Oregon  e) Hawaii  f) Thailand    ')

if Q2Input == 'a':
    QuestionAnswers.append(0)
elif Q2Input == 'b':
    QuestionAnswers.append(1)
elif Q2Input == 'c':
    QuestionAnswers.append(2)
elif Q2Input == 'd':
    QuestionAnswers.append(3)
elif Q2Input == 'e':
    QuestionAnswers.append(4)
elif Q2Input == 'f':
    QuestionAnswers.append(5)

# Question 3

Q3Input = input('\n Question 3: Pick a pet by typing one of the following letter options: \n a) Quetzalcoatl   b) Orange Cat   c) Snoopy   d) Alligator   e) Fish   f) Hedgehog     ')

if Q3Input == 'a':
    QuestionAnswers.append(0)
elif Q3Input == 'b':
    QuestionAnswers.append(1)
elif Q3Input == 'c':
    QuestionAnswers.append(2)
elif Q3Input == 'd':
    QuestionAnswers.append(3)
elif Q3Input == 'e':
    QuestionAnswers.append(4)
elif Q3Input == 'f':
    QuestionAnswers.append(5)

# Question 4

Q4Input = input('\n Question 4: Select your ideal superpower by typing one of the following letter options: \n a) Omnipotence   b) Teleportation   c) Shapeshifting   d) Create food from thin air  e) Jobu Tupaki Powers    ')

if Q4Input == 'a':
    QuestionAnswers.append(0)
elif Q4Input == 'b':
    QuestionAnswers.append(1)
    QuestionAnswers.append(3)
elif Q4Input == 'c':
    QuestionAnswers.append(2)
elif Q4Input == 'd':
    QuestionAnswers.append(4)
elif Q4Input == 'e':
    QuestionAnswers.append(5)

# Question 5

Q5Input = input('\n Question 5: Pick a boba order by typing one of the following letter options: \n a) Black milk tea, boba, less sugar, less ice  b) Jasmine milk tea  c) Wintermelon milk tea, pudding, less ice  d) Thai tea  e) Water    ')

if Q5Input == 'a':
    QuestionAnswers.append(0)
elif Q5Input == 'b':
    QuestionAnswers.append(1)
elif Q5Input == 'c':
    QuestionAnswers.append(2)
elif Q5Input == 'd':
    QuestionAnswers.append(3)
    QuestionAnswers.append(5)
elif Q5Input == 'e':
    QuestionAnswers.append(4)


# Question 6

Q6Input = input('\n Question 6: Select Apple or Android by typing one of the following letter options: \n a) Apple   b) Android    ')

if Q6Input == 'b':
    QuestionAnswers.append(0)
    QuestionAnswers.append(1)

elif Q6Input == 'a':
    QuestionAnswers.append(2)
    QuestionAnswers.append(3)
    QuestionAnswers.append(4)
    QuestionAnswers.append(5)

# Question 7

Q7Input = input('\n Question 7: Pick a movie by typing one of the following letter options: \n a) How to Train Your Dragon   b) Ratatouille  c) Scooby-Doo (2002)  d) Marcel the Shell with Shoes On  e) Peter Pan  f) Baby Driver    ')

if Q7Input == 'a':
    QuestionAnswers.append(0)
elif Q7Input == 'b':
    QuestionAnswers.append(1)
elif Q7Input == 'c':
    QuestionAnswers.append(2)
elif Q7Input == 'd':
    QuestionAnswers.append(3)
elif Q7Input == 'e':
    QuestionAnswers.append(4)
elif Q7Input == 'f':
    QuestionAnswers.append(5)

# Question 8

Q8Input = input('\n Question 8: Choose an element to bend by typing one of the following letter options: \n a) Water  b) Air  c) Earth  d) Fire    ')

if Q8Input == 'a':
    QuestionAnswers.append(0)
elif Q8Input == 'b':
    QuestionAnswers.append(1)
    QuestionAnswers.append(2)
    QuestionAnswers.append(5)
elif Q8Input == 'c':
    QuestionAnswers.append(3)
elif Q8Input == 'e':
    QuestionAnswers.append(4)

# Question 9

Q9Input = input('\n Question 9: Choose an album artwork by typing one of the following letter options: \n a) AJR  b) Bootleg  c) Landmark  d) King Gizzard  e) Cigarettes After Sex f) Choose Your Weapon    ')

if Q9Input == 'a':
    QuestionAnswers.append(0)
elif Q9Input == 'b':
    QuestionAnswers.append(1)
elif Q9Input == 'c':
    QuestionAnswers.append(2)
elif Q9Input == 'd':
    QuestionAnswers.append(3)
elif Q9Input == 'e':
    QuestionAnswers.append(4)
elif Q9Input == 'f':
    QuestionAnswers.append(5)

# Question 10

Q10Input = input('\n Question 10: Choose what you would prefer to do on a typical weekend by typing one of the following letter options: \n a) Stay in and play video games with friends  b) Play boardgames with friends  c) Go on an adventure with friends  d) Drown your sorrows e) Engage in some sort of athletic activity  f) Road trip to a place where you can climb some rocks    ')

if Q10Input == 'a':
    QuestionAnswers.append(0)
elif Q10Input == 'b':
    QuestionAnswers.append(1)
elif Q10Input == 'c':
    QuestionAnswers.append(2)
elif Q10Input == 'd':
    QuestionAnswers.append(3)
elif Q10Input == 'e':
    QuestionAnswers.append(4)
elif Q10Input == 'f':
    QuestionAnswers.append(5)


# Check who has the highest score and tell the user who they are most like
def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]

if most_frequent(QuestionAnswers) == 0:
    print('\n You are most like Aravinth!')
elif most_frequent(QuestionAnswers) == 1:
    print('\n You are most like Daniel!')
elif most_frequent(QuestionAnswers) == 2:
    print('\n You are most like Kaylyn!')
elif most_frequent(QuestionAnswers) == 3:
    print('\n You are most like Lance!')
elif most_frequent(QuestionAnswers) == 4:
    print('\n You are most like Roy!')
elif most_frequent(QuestionAnswers) == 5:
    print('\n You are most like Sam!')

# Percentages

d = Counter(QuestionAnswers)

x = 0
dAr = d[x]*10
print('\n You are {}% Aravinth.'.format(dAr))

x = 1
dDa = d[x]*10
print('\n You are {}% Daniel.'.format(dDa))

x = 2
dKa = d[x]*10
print('\n You are {}% Kaylyn.'.format(dKa))

x = 3
dLa = d[x]*10
print('\n You are {}% Lance.'.format(dLa))

x = 4
dRo = d[x]*10
print('\n You are {}% Roy.'.format(dRo))

x = 5
dSa = d[x]*10
print('\n You are {}% Sam.'.format(dSa))