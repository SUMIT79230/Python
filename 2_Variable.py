# # Concept 1 -> Integer
# x  = input("what is value of x ? ")
# y  = input("what is value of y ? ")
# z = x + y
# print(z) 

# # use int before x and y
# z = int(x) + int(y)
# print(z)

# # it is also written in this way also
# x  = int(input("what is value of x ? "))
# y  = int(input("what is value of y ? "))
# z = x + y
# print(z)


#Concept -> 2 (Float)
x  = float(input("what is value of x ? "))
y  = float(input("what is value of y ? "))

# z = round(x+y)
# print(z)
# print(f"{z:,}")

z = x/y
print(z)
print(round(z))
print(round(z,2))
print(f"{z:.2f}")