# Import Modules Here



# Function goes in here.
def L_Search(arr,item):
    
    N = -1
    i = 0
    #Loop Through all the elements of array 
    for e in arr:
        if item == e:
            N = i
        i = i + 1
    
    #Return Pos on item Array
    return N

# Start of the program 
# Create Input Prompt for user
print("Enter Size of array:", end = " ")
size = int(input())
arr=[]
print("Enter elements of array:", end = " ")

#Loop to get all the elements of array from user
for i in range(size):
    arr.append(int(input()))
print("Enter Item to search:", end=" ")
item = int(input())

Pos = L_Search(arr, item)
if Pos == -1:
    print("Item " + str(item) + " Doesn't Exist in the array " + str(arr))
else :
    print("Item " + str(item) + " Exist at the index " + str(Pos) + " in the array " + str(arr))

