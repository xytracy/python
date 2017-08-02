from sys import argv
#this is a "import" that adds function to python
#the fuctions consititute a "module" of code.
#(modules can also be callded :libraries."
#"argv" is the "argument variable"that holds


script,first,second,third=argv
#unpack the stuff inside argv

y=raw_input("Name?")
age=raw_input("how old are you?")
height=raw_input("how tall are you?")
weight=raw_input("how much do you weight?")

print "so ,you're %r old , %r tall,and %r heavy." %(age,height,weight)
print "the script is called:",script
print"your first variable is:",first
print"your second variable is:",second
print"your third variable is:",third