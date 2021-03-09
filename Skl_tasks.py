#Program for storing Roll no., name and percentage of 5 students
#Let's Begin

#Declaring empty list
ROLL = list() #for Roll number
NAME = list() #for name
PER = list() #for percentage

n = 0 #this is counter

while n<5:
    #Taking the inputs
    a = input("Enter Roll No.: ")
    b = input("Enter Name: ")
    c = input("Enter Percentage: ")
    print("**********************")

    #Adding Elements to List
    ROLL.append(a)
    NAME.append(b)
    PER.append(c)
    
    n +=1 #increment of counter

#Converting list into Tuple  
tuple(ROLL)
tuple(NAME)
tuple(PER)

#Fetching results from Tuples
while True:
    rn = input("Search Roll: ") #Input of roll number that you want to search
    ind = ROLL.index(rn) #Index of the Roll Number in the Tuple
    out = NAME[ind] #Searching for the name with the required index  
    print("NAME ->", out) #Printing the Result