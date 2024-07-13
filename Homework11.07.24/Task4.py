# print all numbers from 10 to 20

for i in range (10,21):
    print (i, end=" ");

# print all numbers between 10 and 20 while skip every other number:
print() #seperate between the prints

for a in range (10,21,2):
    print (a, end=" ");

# get the gap of the numbers from the user
print()
num: int = int (input ("Enter the gap you wish the numbers to skip: "));
for b in range (10,21,num):
    print (b, end=" ");

# get the gap of the numbers from the user- shorter version
print()
for b in range (10,21,int (input ("Enter the gap you wish the numbers to skip: "))):
    print (b, end=" ");

#get the minimum number from the user, the maximum number, and the gap the user wish to skip during the counting.
print()
min: int = int (input ("Enter the first number you want to start the counting: "));
max: int = int (input ("Enter the last number you want to end the counting: "));
num: int = int (input ("Enter the gap you wish the numbers to skip: "));
for c in range (min,(max + 1),num):
    print (c, end=" ");
