# Myers-Briggs Personality quiz
#All MBTI information courtesy of http://www.mindtools.com/pages/article/newCDV_51.htm

#Clears screen

import os
if os.name == "posix":

# Unix/Linux/MacOS/BSD/etc

	os.system('clear')
elif os.name in ("nt", "dos", "ce"):

# DOS/Windows

	os.system('CLS')
else:

# All other operating systems.

	print '\n' * numlines

#Creates prompting symbol

prompt = ' > '

#Prompts response from user

selection = "Please select the letter of the description that best fits you.\n"

#Initial program description

print "\nWelcome to the Myers-Briggs Personality Quiz!\n" 

#First quiz question

print "Question 1: (E)xtroversion or (I)ntroversion?\n"

print """
1. Extroverts are stimulated by events and people external to themselves. They show their feelings, learn by talking, and work well in groups.\n

2. Introverts prefer private reflection, self-examination, and self-discovery. They hide their feelings, prefer to work alone, and learn by watching.\n
"""
print selection

#Validates user response

while True:
	var_1 = raw_input(prompt)

#Next quiz question if validated

	if var_1 == "E" or var_1 == "I":
       		print "\nQuestion 2: (S)ensing or I(N)tuition?\n"
		break
	else:
		print "Sorry! Invalid user input. Please type E or I."


print """
1. Sensing people use their five physical senses (sight, hearing, touch, taste, and smell) to interpret the world. They like real-life examples, prefer practical exercises, and get the facts while possibly missing the main idea.\n

2. Intuitive people prefer to rely on instincts. They work based on hunches and feelings, use their imagination, and get the main idea while missing some of the facts.\n
""" 
print selection

#Validates user response

while True:
	var_2 = raw_input(prompt)

#Next quiz question if validated

	if var_2 == "S" or var_2 == "N":
	        print "\nQuestion 3: (T)hinking or (F)eeling?\n"
		break
	else:
	        print "Sorry! Invalid user input. Please type S or N."

print """
1. Thinking people use logic and objective criteria. They ask 'Why?' and enjoy debates.\n

2. Feeling people use their values and subjective ideas. They use lots of words, and they prefer harmony, agreement, and helping others.\n
"""
print selection

#Validates user response

while True:
	var_3 = raw_input(prompt)

#Next quiz question if validated

	if var_3 == "T" or var_3 == "F":
        	print "\nQuestion 4: (J)udging or (P)erceiving?\n"
		break
	else:
        	print "Sorry! Invalid user input. Please type T or F."

print """
1. Judging people are purposeful, and they like structure, plans, rules, and organization.\n
2. Perceiving people take a laid-back, relaxed approach. They're flexible, open to change, and like to explore.\n
"""
print selection

#Validates user response

while True:
	var_4 = raw_input(prompt)

	if var_4 == "J" or var_4 == "P":

#Creates seperation between questions and results

		print "."*20

#Displays quiz results

		print "\nCongratulations!\n"
		print "Your personality type is: %s%s%s%s" % (var_1, var_2, var_3, var_4)
		break
	else:
        	print "Sorry! Invalid user input. Please type J or P."



