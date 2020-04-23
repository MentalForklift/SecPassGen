#This Python project will generate a secure password for you based on your raw input.
import random
import string
print "This Secure Password Generator will create a secure password for you."
#Line 4 will take a passphrase input from the user.
phrase = raw_input("Please enter a phrase consisting of five to eight words: ")
#This will check to see if the phrase is at least 20 characters long and no more than 35.
if len(phrase) > 35:
    print "Please keep your phrase under 35 characters. You currently have %d characters." % (len(phrase))
elif len(phrase) < 20:
    print "Please enter at least 20 characters. You currently have %d characters." % (len(phrase))
else:
    print "Thanks!"
#This conditional check the input to see if it contains only alpha characters and spaces.
if len(phrase) > 0 and phrase.isalpha() or phrase.replace(' ','').isalpha():
    passphrase = phrase.lower()
#This command converts the entire phrase to lowercase and prints it to the console.
    print passphrase
else:
    print "Error! Please enter only letters."

# Commented out original defined function. Basically the problem was in the for loop and the method used to 'join' to the created password. The object 'choice' in the random module selects only *one* character in the given sequence. Your function was telling Python to pick a single letter from the given string, then the for loop was randomly choosing *from that single letter* and adding it to the passphrase, so you end up with a password that is the same character 8 times over.

###### Original function #####
# def random_phrase(passlength = 8):
#     letters = random.choice(passphrase)
#     return ''.join(random.choice(letters) for i in range(passlength))


# This modification to your function works. Set the password as a blank string, then use the for loop to iterate 8 times through that password and choose a random character, appending that to the empty string.

###### Working Modified Function #######
def random_phrase(passlength = 8):
    password = ""
    for i in range(passlength):
        password = random.choice(passphrase)
    return password

# Made a small enhancement to the function, uncomment this one and comment out the other one to test it.
# This works similar to the other, the letters variable converts the entered passphrase to a list of characters, then during each iteration the choice is made, added to the password string, and most importantly *removed* from the options during the next go-around of the loop. This way it limits the chances of the same character being chosen twice in a row. 

####### Enhanced Modified Function #######
# def random_phrase(passlength = 8):
#     letters = [char for char in passphrase]
#     password = ""
#     for i in range(passlength):
#         choice = random.choice(letters)
#         password += choice
#         letters.remove(choice)
#     return password

print "Your password is:", random_phrase()

