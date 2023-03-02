# # IMMUITAVLE
m="mughal"
t=m.title()
print(t)
# # MUTABLE
Name=['rashid','ali','noor']
Name.append("NOOR")
print("Name")

# for loop
Name=['rashid','ali','noor']
for nam in Name:
    print(nam)

# while loop in list
i=0
while i<len(Name):
    print(Name[i])
    i+=1

# list in side lest
matrix=[['rashid','ali','noor'],['naman','nadeem','arshad'],['rahman','raheem','rashid']]
print(Name[2])

for sublist in matrix:
    for i in sublist:
        print(i)

print(matrix[1][1])

#TYPE FUNCTION
S="string"
print(type(S))

#MOR ABOUT LIST
number=list(range(1,21))
print(number)

number.pop()
print(number)

# print(number.index(4))  # are used to any velue posiction 

def negitive_list(l):
    negitive=[]
    for i in l:
        negitive.append(-i)
    return negitive
print(negitive_list(number))


def squrie_list(l):
  squrae=[]
  for i in l:
    squrae.append(i**2)
    return squrae
numbers=list(range(1,11))
print(squrie_list(numbers))

def return_lest(l):
    r_list=[]
    for i in range(len(l)):
        poped=l.pop()
        r_list.append(poped)
        return r_list
    number=[1,2,3,4,5,6,7,8,9] #sesho
    print(return_lest(number))

def retrn_lest(l):
    p_lest=[]
    for i in l:
        p_lest.append(i[::-1])
        return p_lest

name=["rashid,naeem,ali,mahmood"]
print(retrn_lest(name))