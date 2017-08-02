print "how old are you ?",
age=raw_input()
#the comma prevents a new line;that way
#the prompt for data shows up on the same line.
#note that you can put any kind of data in.
print"how tall are you ?",
height=raw_input()

print"how much do you weigh?",
weight=raw_input()

print # this inserts a blank line in the printout

print"so ,you're %r old, %r tall, and %r heavy"%( age,height,weight)
#by breaking the variable into a second line,
#the entire line doesn't go past 88 characters.
#which is considered as a good form.
