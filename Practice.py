print("Hello world")
my_string = "Hi this is a way of writting a string in python\n"
another_string  = 'This is another way\n'
a_long_string = ''' This is 
an example of
multiline string'''
print(my_string, another_string, a_long_string)
print("I'm working on something")
print('As the name suggest "Python" is a name of snake')
print(my_string.upper())
#print(dir(my_string))
var = "cookies"
another_string1 = "I like %s and %s" % ("Python", var)
print(another_string1)

#LIST
list1 = [10,45,23,46,11,9,43,2]
list1.sort()
print(list1[0:])

#TUPLE
# main difference is that a tuple is immutable while the list is mutable.
my_tuple=(1,3,4,9,20,65,55,5,12)
#we cannot sort tupple 
print(my_tuple[0:3]) #we can slice tupple
another_tuple = tuple([1,6,88,45,23,21])
print(another_tuple)

#DICTIONARY
#A Python dictionary is basically a hash table
my_dict = {"name":"Mike", "address":"123 Happy Way"}
print(my_dict["name"])
print("name" in my_dict) #check whether a key belongs to dict or not
print("state" in my_dict)
print(my_dict.keys()) #check list of all the keys in a dictionary 
print(my_dict)
my_other_dict = {"one":1, "two":2, "three":3}
print(my_other_dict)


#The if statement
if 2<1:
    print("This is a true statement")
else:
    print("This is false statement")

#value = input("How much is that doggy in the window? ")
#value = int(value)
value1 = 15
if value1 < 10:
    print("That's a great deal!")
elif 10 <= value1 <= 20:
    print("I'd still pay that...")
else:
    print("Wow! That's too much!")

x = 11
y=20
if x>y and y >15:
    print("x is greater than y")
elif x>=10 and y>15:
    print("X is greater than 10 and Y is greater than 15")
else:
    print("What' up")

my_list = [1, 2, 3, 4]
x = 10
if x not in my_list:
    print("'x' is not in the list, so this is true")


empty_list = []
empty_tuple = ()
empty_string = ""
nothing = None

if empty_list == []:
    print("It's an empty list!")

if empty_tuple:
    print("It's not an empty tuple!")

if not empty_string:
    print("This is an empty string!")

if not nothing:
    print("Then it's nothing!")

#Looping

for number in range(0,5):
       print(number)

a_dict = {"one":1, "two":2, "three":3}
for key in a_dict:
       print(key)

i = 8
if i in my_list:
    print("item found")
else:
    print("item not found")


#Exception 
my_dict3 = {"a":1, "b":2, "c":3}
try:
    value = my_dict3["d"]
except IndexError:
    print("This index does not exist!")
except KeyError:
    print("This key is not in the dictionary!")
except:
    print("Some other error occurred!")

#File Handling

#handle = open(r"C:\Users\asing\Desktop\test.txt", "r")
'''handle = open("test.txt", "r")
data = handle.read()  #handle.readline() will read only one line at a time
#handle.readlines() will read all the lines and store as a list

print(data)
handle.close()
'''
#For reading a file in pieces we use loop
'''handle = open("test.txt", "r")

for line in handle:
    print(line)
handle.close()

#Reading data using while loop
handle = open("test.txt", "r")

while True:
    data = handle.read(1024) #we use Python’s while loop to read a kilobyte of the file at a time.
    print(data)
    if not data:
        break
handle = open("Python Book.pdf", "rb")
while True:
    data = handle.read()
    print(data)
    if not data:
        break


#Writing to a file 
handle = open("test.txt", "w")
handle.write("This is a test!!!")
handle.close()
#We can use WITH and File_Handler to close the file automaticaly 
with open("test.txt") as file_handler: 
    for line in file_handler:
        print(line)
print(3 >= 3)
'''


def gcd(a, b):
    while(b!=0):
        t=a
        a=b
        b=t%b
    
    return a

gcd(20,8)