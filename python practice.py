#!/usr/bin/env python
# coding: utf-8

# # python practice

# In[1]:


print("kishan dongare")


# # variable & data Type

# In[3]:


character_name = "john"
characte_age  = "35"
print("There once was a man named "+character_name + ",")
print("he was "+character_name+" year old,")
print("he rally liked the name "+character_name + ",")
print("but din not like being"+characte_age+".")


# In[4]:


character_name = "tom"
characte_age  = "25"
print("There once was a man named "+character_name + ",")
print("he was "+character_name+" year old,")
print("he rally liked the name "+character_name + ",")
print("but din not like being"+characte_age+".")


# In[6]:


character_name = "john"
characte_age  = "35"# string
print("There once was a man named "+character_name + ",")
character_name = "Mike"
print("he was "+character_name+" year old,")
print("he rally liked the name "+character_name + ",")
print("but din not like being"+characte_age+".")


# In[10]:


character_name = "john"
characte_age  = 35.56547 # number
is_male = False
print("There once was a man named "+character_name + ",")
character_name = "Mike"
print("he was "+character_name+" year old,")
print("he rally liked the name "+character_name + ",")
print("but din not like being",characte_age)


# # working with string

# In[11]:


print("working with \n string")


# In[12]:


print("working with \" string")


# In[13]:


print("working with \ string")


# In[15]:


phrase = "working with string"
print(phrase+" is cool")


# In[16]:


phrase = "working with string"
print(phrase.lower())


# In[17]:


phrase = "working with string"
print(phrase.upper())


# In[18]:


phrase = "working with string"
print(phrase.isupper())


# In[19]:


phrase = "working with string"
print(phrase.upper().isupper())  


# In[20]:


phrase = "working with string"
print(len(phrase))


# In[21]:


phrase = "working with string"
print(phrase[5])


# In[22]:


phrase = "working with string"
print(phrase.index("i"))


# In[23]:


phrase = "working with string"
print(phrase.index("z"))


# In[24]:


phrase = "working with string"
print(phrase.replace("working","work"))


# # working with number

# In[25]:


print(34)


# In[26]:


print(-4238)


# In[27]:


print(34+23)


# In[28]:


print(34-45)


# In[29]:


print(34*(23-34)%3)


# In[32]:


my_num = 5
print(my_num)


# In[33]:


my_num = 5
print(str(my_num)+" my favorate number")


# In[36]:


my_num = -5
print(abs(my_num))


# In[37]:


my_num = 5
print(pow(my_num,2))


# In[39]:


my_num = 5
print(my_num)


# In[41]:


my_num = 5
print(max(my_num,5,7,9))


# In[42]:


my_num = 5
print(min(my_num,5,7,9))


# In[40]:


my_num = 5.765
print(round(my_num))


# In[43]:


from math import*
my_num = 5.765
print(floor(my_num))


# In[44]:


from math import*
my_num = 5.765
print(ceil(my_num))


# In[45]:


from math import*
my_num = 5.765
print(sqrt(my_num))


# # getting input from users

# In[3]:


name = input("Enter your name ")
print("hello "+name+ ".")


# In[4]:


name = input("Enter your name ")
age = input("Enter your age")
print("hello "+name+ ".your are "+age+" ")


# # building a basic calculator

# In[1]:


num1 = input("Enter a number ")
num2 = input("Enter another number ")
result = num1+num2 #it is work like string
print(result)


# In[2]:


num1 = input("Enter a number ")
num2 = input("Enter another number ")
result = int(num1)+int(num2) 
print(result)


# In[3]:


num1 = input("Enter a number ")
num2 = input("Enter another number ")
result = float(num1)+float(num2) 
print(result)


# # mad lib game
# 

# In[4]:


print("Rosees are red ")
print("Violet are blue")
print("I love you")


# In[6]:


color = input("Enter your color: ")
plural_noun =  input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are "+color)
print(plural_noun +" are blue")
print("I love you "+celebrity)


# # Lists

# In[7]:


friends = ["kishan","sahil","jim"] #squre bracket related values
print(friends)


# In[8]:


friends = ["kishan","sahil","jim"] #squre bracket related values
print(friends[2])


# In[10]:


friends = ["kishan","sahil","jim"] #squre bracket related values
print(friends[-2])


# In[11]:


friends = ["kishan","sahil","jim"] #squre bracket related values
print(friends[1:])


# In[13]:


friends = ["kishan","sahil","jim","arush","rakesh"] #squre bracket related values
print(friends[:3])


# In[15]:


friends = ["kishan","sahil","jim","arush","rakesh"] #squre bracket related values
friends[2] = "mike" 
print(friends[2])
print(friends)


# # List Functions

# In[19]:



friends = ["kishan","sahil","jim","arush","rakesh"]
friends.append("abhi")
print(friends)


# In[20]:



friends = ["kishan","sahil","jim","arush","rakesh"]
friends.insert(1,"abhi")
print(friends)


# In[21]:


friends = ["kishan","sahil","jim","arush","rakesh"]
friends.remove("kishan")
print(friends)


# In[22]:


friends = ["kishan","sahil","jim","arush","rakesh"]
friends.clear()
print(friends)


# In[23]:


friends = ["kishan","sahil","jim","arush","rakesh"]
friends.pop()
print(friends)


# In[25]:


friends = ["kishan","sahil","jim","arush","rakesh"]

print(friends.index("jim"))


# In[26]:


friends = ["kishan","sahil","jim","jim","jim","arush","rakesh"]

print(friends.count("jim"))


# In[27]:


friends = ["kishan","sahil","jim","arush","rakesh"]
friends.sort()
print(friends)


# In[29]:


lucky_number = [56,76,87,32,98,18]
lucky_number.sort()
print(lucky_number)


# In[30]:


lucky_number = [56,76,87,32,98,18]
lucky_number.reverse()
print(lucky_number)


# In[32]:


lucky_number = [56,76,87,32,98,18]
lucky_number2 = lucky_number.copy()
print(lucky_number2)


# # Tuples

# In[34]:


coordinates = (4,5)
print(coordinates[1])


# In[36]:


coordinates = (4,5)
coordinates[1]= 10
print(coordinates)


# In[38]:


coordinates = [(4,5),(2,8),(2,9)]
coordinates[1]= 10,7
print(coordinates)


# # list vs Tuples
# 1	Lists are mutable	                                  Tuples are immutable
# 2	Implication of iterations is Time-consuming	          The implication of iterations is comparatively Faster
# 3	The list is better for performing operations          Tuple data type is appropriate for accessing the elements
#     such as insertion and deletion.	                 
# 4	Lists consume more memory	                          Tuple consume less memory as compared to the list
# 5	Lists have several built-in methods                   Tuple does not have many built-in methods.
# 6	The unexpected changes and errors are more            In tuple, it is hard to take place.
#    likely to occur   

# # function

# In[39]:


def say_hi():
    print("Hello User")


# In[40]:


def say_hi():          #call function
    print("Hello User")
print("top")
say_hi()
print("bottom")


# In[41]:


def say_hi(name):         
    print("Hello User "+name)
    
say_hi("kishan")
say_hi("arush")


# In[42]:


def say_hi(name,age):         
    print("Hello User "+name+","+age)
    
say_hi("kishan",25)
say_hi("arush",30)


# In[43]:


def say_hi(name,age):         
    print("Hello User "+name+","+str(age))
    
say_hi("kishan",25)
say_hi("arush",30)


# # Return staement

# In[44]:


def cube(num):
    num*num*num
print(cube(3))


# In[45]:


def cube(num):
   return num*num*num
print(cube(3))


# In[46]:


def cube(num):
    return num*num*num
result = cube(3)
print(result)


# # if statement

# In[47]:


is_male =  True
if is_male:
    print("You are a male")
else:
    print("you are not male")


# In[48]:


is_male =  False
if is_male:
    print("You are a male")
else:
    print("you are not male")


# In[49]:


is_male =  True
is_tall = True
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("you neither male nor tall")


# In[50]:


is_male =  False
is_tall = True
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("you neither male nor tall")


# In[51]:


is_male =  True
is_tall = True
if is_male and is_tall:
    print("You are a tall male")
else:
    print("you are either male or not tall or both")


# In[52]:


is_male =  True
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
else:
    print("you are either male or not tall or both")


# In[55]:


is_male =  True
is_tall = True
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male ")
elif  not is_male and (is_tall):
    print("you are not a male but are tall ")     
else:
    print("you are either male or not tall or both")


# In[56]:


is_male =  False
is_tall = True
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male ")
elif  not is_male and (is_tall):
    print("you are not a male but are tall ")     
else:
    print("you are either male or not tall or both")


# In[57]:


is_male =  True
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male ")
elif  not is_male and (is_tall):
    print("you are not a male but are tall ")     
else:
    print("you are either male or not tall or both")


# In[58]:


is_male =  False
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male ")
elif  not is_male and (is_tall):
    print("you are not a male but are tall ")     
else:
    print("you are either male or not tall or both")


# # if statement and Comparisons

# In[61]:


def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(3,4,5))
 #check comparison operator   
    
    


# # Building a better Calculator

# In[64]:


num1 = float(input("Enter first number: "))
op = (input("Enter operator:"))
num2 = float(input("Enter first second: "))
if op =="+":
    print(num1+num2)
elif op =="-":
    print(num1-num2)
elif op =="/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("invalid operator")
    


# # dictionaries

# In[67]:


monthConversions = {"jan": "january",
                   "Feb": "February",
                   "Mar":"March",
                   "Apr":"April",
                   "May":"May",
                   "Jun":"June",
                   "Jul":"July",
                   "Aug":"August",
                   "Sep":"September",
                   "Oct":"October",
                   "Nov":"November",
                   "Dec":"December",
}
print(monthConversions["Mar"])


# In[68]:


monthConversions = {"jan": "january",
                   "Feb": "February",
                   "Mar":"March",
                   "Apr":"April",
                   "May":"May",
                   "Jun":"June",
                   "Jul":"July",
                   "Aug":"August",
                   "Sep":"September",
                   "Oct":"October",
                   "Nov":"November",
                   "Dec":"December",
}
print(monthConversions.get("Luv","Not a valid key"))


# # While loop

# In[69]:


i= 1 #initialize
while i<=10: #condition
    print(i)
    i=i+1 #i+=1 #increment or decrement
print("done with loop")


# # Building a Guessing Game

# In[70]:


secret_word ="giraffe"
guess = ""
while guess!=secret_word:
    guess=input("Enter guess")
print("you win")


# In[1]:


secret_word ="giraffe"
guess = ""
guess_count =0
guess_limit = 3
out_of_guesses= False
while guess!=secret_word:
    if guess_count<guess_limit:
        guess=input("Enter guess: ")
        guess_count+=1
    else:
        out_of_guesses =True
        
if out_of_guesses:
    print("Out of guesses,You LOSE!")
else:
    print("you win")


# # For Loop

# In[2]:


for letter in "kishan dongare":

    print(letter)


# In[4]:


friends = ["jim","arush","sahil"]
for name in friends:
    print(name)


# In[5]:


for index in range(10):
    print(index)


# In[6]:


for index in range(3,10):
    print(index)


# In[8]:


friends = ["jim","arush","sahil"]
for index in range(len(friends)):
    print(friends[index])


# # Exponent Function

# In[9]:


print(2**3)


# In[12]:


def raise_to_power(base_num,pow_num):
    result=1
    for index in range(pow_num):
        result = result*base_num
    return result
print(raise_to_power(2,3))


# # 2D List &Nested Loops

# In[13]:


number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]   
]
print(number_grid[1][1])


# In[14]:


number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]   
]
print(number_grid[2][1])


# # Build a Translator

# In[5]:


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation+"g"
        else:
            translation = translation +letter
    return translation
print(translate(input("Entre a phrase :")))


# In[4]:


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation+"G"
            else:
                translation = translation+"g"
        else:
            translation = translation +letter
    return translation
print(translate(input("Entre a phrase :")))


# # COMMENTS

# In[6]:


'''
this program is cool
'''
#this program is cool

print("Comments are fun")


# # Try/Except

# In[8]:


number = int(input("Enter a number"))
print(number)


# In[9]:


try:
    number = int(input("Enter a number"))
    print(number)
except:
    print("Invalid Input")


# # Reading Files

# In[10]:


employee_file = open("employees.txt","r")
print(employee_file.read())
employee_file.close()


# In[ ]:


employee_file = open("employees.txt","r")
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())
employee_file.close()


# In[ ]:


employee_file = open("employees.txt","r")
for employee in employee_file.readline():
    print(employee)
employee_file.close()


# # Writing to Files

# In[ ]:


employee_file = open("employees.txt","a")
employee_file.write("\n Human Resource")
employee_file.close()


# # Classes &Object

# In[ ]:


class Student: #FIRST CREAT Student.py
    def __init__(self,name,major,gpa,is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on _probation = is_on_probation


# In[ ]:


from Student import Student #app.py
student1 = student("jim","Business",3.1,False)
student2 = student("kisha","Business",4.6,True)
print(Student1.name)
print(Student2.gpa)


# # Object Function

# In[ ]:


class Student: #FIRST CREAT Student.py
    def __init__(self,name,major,gpa,is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
    def on_honor_roll(self):
        if self.gpa>3.5:
            return True
        else:
            return False


# In[ ]:


from Student import Student #app.py
student1 = student("jim","Business",3.1)
student2 = student("kisha","Business",3.8)
print(student1.on_honor_roll())
print(student2.on_honor_roll())


# # Building a Multiple Choice Quiz

# In[ ]:


class Question: #Question.py
    def __init__(self,prompt,answer):
        self.prompt = prompt
        self.answer= answer


# In[ ]:


from Question import Question #app.py
question_prompt = [
    "what color are apples?\n(a)read/green\n(b)Purple\n(c)orange"
    
]
Question = [
    Question(question_prompt[0],"a")
]
def run_test(question):
    score = 0
    for question in question:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
    print("you got"+str(score)+"/"+str(len(question))+"correct")
run_test(question)


# # Inheritance

# In[ ]:


class Chef:        #Chef.py
    def make_chicken(self):
        print("the chef makes a chicken")
    def make_salad(self):
        print("the chef makes a salad")
    def make_special_dish(self):
        print("the chef mskes a biryani")
    


# In[ ]:


class ChineseChef: #ChineseChef.py
    def make_fried_rice(self):
        print("the chef makes fried rice")
    


# In[ ]:


from Chef import Chef #app.py
from ChineseChef import ChineseChef
mychef = chef()
mychef.make_special_dish()

myChineseChef = ChineChef()
myChineseChef.make_fried_rice()


# In[ ]:


#suppose we want to Chef() those make ChineseChef() also know how to make then we use inheritance


# In[4]:


class Chef:        #Chef.py
    def make_chicken(self):
        print("the chef makes a chicken")
    def make_salad(self):
        print("the chef makes a salad")
    def make_special_dish(self):
        print("the chef mskes a biryani")
    


# In[ ]:


from Chef import Chef #ChineseChef.py
class ChineseChef(Chef):
    def make_fried_rice(self):
        print("the chef makes fried rice")


# In[ ]:


from Chef import Chef #app.py
from ChineseChef import ChineseChef
mychef = chef()
mychef.make_special_dish()

myChineseChef = ChineChef()
myChineseChef.make_Chicken()


# In[ ]:


Try this in PyCharm IDE

