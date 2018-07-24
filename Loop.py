'''

today = datetime.now()

print('Today\'s date is:',today)

# example of if-loop
n = input()
n = int(n)

if n%2==0:
    print('The number is Even')
if n%2==1:
    print('the number is odd')

#example of else

n = input()
n = int(n)

if n%2 == 0 :
    print('The number is Even')
else:
    print('The number is Odd')

# example of elif
n = input()
n = int(n)

if n>=1 and n<=10:
    print('too low')
elif n>=11 and n<=20:
    print('Medium')
elif n>21 and n<=30:
    print('large')
else:
    print('Too large')

#Example of For loop

word = 'anaconda'

for i in word:
    print(i)

#Example of for loop using list
words = ['banana','apple','orange','raspberry','blackberry']
for i in words:
    print(i)

#Example of while loop
cnt =1

while cnt<7:
    print(cnt)
    print('This is inside loop')
    cnt+=1
else:
    print('##############################')
    print(cnt)
    print('This is outside loop')

#while for string

word = "Jthon"
pose = 0
while pose < len(word):
    print(word[pose])
    pose += 1

cnt = 1
while True :
     print(cnt)
     cnt +=2
     if cnt > 10:
         break;
         print(cnt)

#Example of list
words = ['shiv','raj','Exit','kadam']

for i  in words:

    if i == 'Exit':
        break;
    print(i)

#example of contineue
numbers = range(1,11)

for i in numbers:

    if i==7:
        print('7 is skipped')
        continue
        print('This statement not going to printed')
    print(i*2,'is the double of',i)


    #switch by using dictionaries
b = {
    'a' : 123,
    'b' : 124,
    'c' : 125,
    'd' : 126,
}
inp = input('Enter any character:')
print('The value is :',b.get(inp,-1))

# using dic for switch and case

def switch_function(value,x):
    return {
        'a': lambda x: x + 122,
        'b': lambda x: x * 2,
        'c': lambda x: x - 123,
        'd': lambda x: x / 2
    } .get(value)(x)

inp = input('Enter any character:')
x = int(input('Enter num'))
print('the result for inp is:',switch_function(inp,x))

# teranary operator example with if -else and  Tuple
is_fast = True
car = 'Ferrari' if is_fast else 'Sedan'
print('the fast car is',car)
car = ('Sedan','Ferrari')[is_fast]
print('The fast car from Tuple is',car)
#############################################
#Example of pass

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for i in numbers:
    if i%2==0:
        pass
    else:
        print('The number is odd',i)

#Example of fibonocci sequence
nterm = int(input('How many terms ?\n'))

n1 =0
n2 =1
count =0

if nterm<=0:
    print('Enter positive number')
elif nterm==1:
    print('The fibinocci sequence upto nturm',nterm)
    print(n1)
else:
    print('The fibonocci sequence upto nterm',nterm)
    while count<nterm :
        print(n1,end=",")
        nth = n1+n2
        n1 = n2
        n2 = nth
        count +=1

# if loop example of leap year

year = int(input('Enter year:'))

if year%4==0:
    if year%100==0:
        if year%400:
            print("The year is leap",year)
        else:
            print('The year is not leap',year)
    else:
        print('{0} The year is Leap year'.format(year))
else:
    print('The year is not leap year',year)

#Example of complete loop

def testifcondition():
    age = int (input('Enter your age ..!'))
    if age<=0:
        print('Enter valid age')
    elif age<20:
        print('You are Teenager..!')
    elif age<50:
        print('you are Adult...!')
    else:
        print('You are Older..Take care!!')

num = int(input('No of times you what to ask..'))
for i in range(0,num):
    print('steps'+ str(i))
    testifcondition()
#example of class/objects/attribute
class Shark:
    def __init__(self,name):
        self.name = name
        print('This is constructor method')
    def swim(self):
        print('The '+self.name+ ' is swimming')
    def be_awesome(self):
        print('The '+self.name+' is awesome')
def main():
    sammy = Shark("sammy")
    stieve =Shark("stieve")
    stieve.swim()
    sammy.swim()
    sammy.be_awesome()
if __name__ == "__main__":
    main()

import this
print(this.s.decode('rot13'))


def greet(name,age):

    print("Very nice" + str(name))

greet('shiv',29)
#Example
l =[10,40,30]
l.sort()

print(1)
'''
d ={1:'a',2:'b',3:'c'}
d.pop(2)
print(d)
d ={1:'a',2:'b',3:'c'}
d.popitem()
print(d)














