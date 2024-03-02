# Import Modules Here



# Function goes in here.
def Arr_rev(arr):
    
    # Get Size of array using len Function
    N = len(arr)
    
    # Declare New Rev Array
    arrRev = []
    
    #Loop Through all the elements of array in reverse and append in element in new array
    for i in range(N,0,-1):
        arrRev.append(arr[i-1])
    
    #Return Reverse Array
    return arrRev

# Start of the program 
# Create Input Prompt for user
print("Enter Size of array:", end = " ")
size = int(input())
arr=[]
print("Enter elements of array:", end = " ")

#Lop to get all the elements of array from user
for i in range(size):
    arr.append(int(input()))

print(Arr_rev(arr))
