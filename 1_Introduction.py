# Concept -> 1
# Introduction
print("Hello , world")

# Concept -> 2
# taking input from user
name = input("What is your name ? ");

# Concept -> 3
# Say hello to User
print("hello,"+name)
print("hello,",name)

# Concept -> 4
# documentation part
#Say hello to User
print("hello,",end="???\n")
print("hello,",sep='')
print(name)


# Concept -> 5
# print a word under "word"
print("hello, \"Sumit\" ")
print("hello,{name}")
print(f"hello,{name}");

#remove whitespace from str
print("\nConcept 6 : ")
print("Before using  function ")
print(f"hello,{name}");

print("After using  function ")
# name = name.strip()
# name = name.capitalize()

#combine 2 different function , title only capitialize 1 character
name = name.strip().title() 

# Combine with while taking input 
# name = input("What is your name ?").strip().title()
print(f"Hello,{name}")


# Concept -> 7
# Split user first name and last name
name = input("\nWhat is your name ? ").strip().title()
first,last = name.split(" ")
print(f"hello,{first}")


