a = 1
b = 12
c = 14
d = 145
e = 15
f = 124
g = 1245
h = 125
i = 24
j = 245
k = 13
l = 123
m = 134
n = 1345
o = 135
p = 1234
q = 12345
r = 1235
s = 234
t = 2345
u = 136
v = 1236
w = 2456
x = 1346
y = 13456
z = 1356

word = []
n = int(input("Enter number of letters: "))
print("spell out your word")
# iterating for the range 
for i in range(0, n): 
    letter = input()

    word.append(letter) # adding the element 
    if letter == "a":
        print("o \n  \n  ")
        word[i] = a
    if letter == "b":
        print("o \no \n  ")
        word[i] = b
    if letter == "c":
        print("oo\n  \n  ")
        word[i] = c
    if letter == "d":
        print("oo\n o\n  ")
        word[i] = d
    if letter == "e":
        print("o \n o\n  ")
        word[i] = e
    if letter == "f":
        print("oo\no \n  ")
        word[i] = f
    if letter == "g":
        print("oo\noo\n  ")
        word[i] = g
    if letter == "h":
        print("o \noo\n  ")
        word[i] = h
    if letter == "i":
        print(" o\no \n  ")
        word[i] = i
    if letter == "j":
        print(" o\noo\n  ")
        word[i] = j
    if letter == "k":
        print("o \n  \no ")
        word[i] = k
    if letter == "l":
        print("o \no \no ")
        word[i] = l
    if letter == "m":
        print("oo\n  \no ")
        word[i] = m
    if letter == "n":
        print("oo\n o\no ")
        word[i] = n
    if letter == "o":
        print("o \n o\no ")
        word[i] = o
    if letter == "p":
        print("oo\no \no ")
        word[i] = p
    if letter == "q":
        print("oo\noo\no ")
        word[i] = q
    if letter == "r":
        print("o \noo\no")
        word[i] = r
    if letter == "s":
        print(" o\no \no ")
        word[i] = s
    if letter == "t":
        print(" o\noo\no ")
        word[i] = t
    if letter == "u":
        print("o \n \noo")
        word[i] = u
    if letter == "v":
        print("o \no \noo")
        word[i] = v
    if letter == "w":
        print(" o\noo\n o")
        word[i] = w
    if letter == "x":
        print("oo\n  \noo")
        word[i] = x
    if letter == "y":
        print("oo\n o\noo")
        word[i] = y
    if letter == "z":
        print("o \n o\noo")
        word[i] = z
print(word) 