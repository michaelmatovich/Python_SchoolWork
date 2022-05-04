num1 = 42 # Variable declaration and initialization
num2 = 2.3 # Variable declaration and initialization
boolean = True # Variable declaration and initialization
string = 'Hello World' # Variable declaration and initialization
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # Tuple initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Tuple initalize
fruit = ('blueberry', 'strawberry', 'banana') #Typle initalize
print(type(fruit))  # log statement
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms') #tuple add value
print(person['name'])#log statement
person['name'] = 'George' #typle change value
person['eye_color'] = 'blue' 
print(fruit[2]) # log statement

if num1 > 45: # if
    print("It's greater") # log statement
else: # else
    print("It's lower") # logstatement

if len(string) < 5:# if 
    print("It's a short word!")#log statement
elif len(string) > 15:#else if
    print("It's a long word!")# log sattement
else:#else
    print("Just right!")#log statemenet

for x in range(5): #for start
    print(x) #log statement
for x in range(2,5):#for start
    print(x)#log satement
for x in range(2,10,3):#for start
    print(x)#log satement
x = 0
while(x < 5): #whilte start
    print(x)#log
    x += 1#increment

pizza_toppings.pop() #typle delete value
pizza_toppings.pop(1)#tuple delete value

print(person)#log
person.pop('eye_color')#tuple delete
print(person)#log

for topping in pizza_toppings: #for start
    if topping == 'Pepperoni':#if
        continue
    print('After 1st if statement')#log
    if topping == 'Olives':#if
        break

def print_hello_ten_times(): #function define
    for num in range(10):#for
        print('Hello')#log

print_hello_ten_times() #function call

def print_hello_x_times(x): #function fdefine with argument x
    for num in range(x):#for
        print('Hello')#log

print_hello_x_times(4) #function call with argument x

def print_hello_x_or_ten_times(x = 10): #function define with default argument
    for num in range(x):#for
        print('Hello')#log

print_hello_x_or_ten_times()#function call x = 10
print_hello_x_or_ten_times(4)#function call x = 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)