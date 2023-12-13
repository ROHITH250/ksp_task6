print("Hello world ")# this is print statement

num = 10 #int
char = "rohith" # char
var = 53.6 #float

print(num)
print(char)
print(var)

if (num <= 20):
    print("the num ber is small")
else:
    print("the number is big")

#operators 
# Arthemetic

a=20
b=40

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

# Assignment
x = 5
x += 3
print(x)
x -= 3
print(x)
x*=3
print(x)
x/=3
print(x)

#comparision
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#Bitwise
print(a&b)
print(a|b)
print(a^b)

#logical
print(x>3 and x<10)
print(x<5 or x<4)

#while loop
i = 1
while i < 6:
  print(i)
  i += 1

#for loop
for x in range(6):
  print(x)
else:
  print("finished!")


#functions
def my_function():
  print("HI this is my function")

my_function()