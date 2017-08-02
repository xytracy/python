from sys import argv

script,filename=argv

txt= open(filename)
#open is a command taht reaads our text file

print"here's your file %r:" %filename
print txt.read()
#the "." (dot) is to add a command

print"type the filename again:"
file_again=raw_input(">")

txt_again=open(file_again)

print txt_again.read()
txt.close()
txt_again.close()