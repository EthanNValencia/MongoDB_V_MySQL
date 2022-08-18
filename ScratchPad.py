from random import seed
from random import random

my_input = ['Engineering', 'Medical'] 
input1 = [40, 30, 20, 10] 
my_input.extend(input1) 
# print(my_input)


values = [dict(zip([1],[x])) for x in range(1,100)] # This is kind of an interesting one liner. 
# print(values)

values = []

document1 = {"first_name":"Fred", "last_name":"Polk"}
document2 = {"first_name":"Alfred", "last_name":"Polk"}

for x in range(10):
	doc = {"place":x,'num':random(),"first_name":"Fred", "last_name":"Polk"}
	values.append(doc)

# print(values)


firstNames = ['George','John','Thomas','James','John','Andrew','Zachary','Millard','Franklin','Abraham']
lastNames = ['Washington','Adams','Jefferson','Madison','Monroe','Jackson','Tyler','Polk','Taylor','Fillmore']

print(len(firstNames))
print(len(lastNames))

rand = random() * 10;
print(firstNames[int(rand)])
print(lastNames[int(rand)])