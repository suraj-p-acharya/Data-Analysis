# Import Modules Here



# Function goes in here.
def Arr_Sum(arr):
    
    SumArr = 0
    #Loop Through all the elements of array in reverse and append in element in new array
    for e in arr:
        SumArr = SumArr + e
    
    #Return Reverse Array
    return SumArr

# Start of the program 
# Create Input Prompt for user
print("Enter Size of array:", end = " ")
size = int(input())
arr=[]
print("Enter elements of array:", end = " ")

#Lop to get all the elements of array from user
for i in range(size):
    arr.append(int(input()))
print(Arr_Sum(arr))
