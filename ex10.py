tabby_cat="\t i'm tabbed in."
#\t inserts a tab

persian_cat="i'm split\non a line."
#\n goes to a new line

backslash_cat="i'm \\a \\cat."
#\\ prints a single\

fat_cat='''
i'll do a list:
\t* cat food
\t* fishies
\t* catnip\n\t* grass
'''
 
formatter='%s '

print  formatter %tabby_cat
print persian_cat
print backslash_cat
print fat_cat
#use %r as a formatter will only print the exact word
#use %s as a formatter will print the real format