# define variables
shopList = []

# list function to print out list
def listFunc(shopList, n):
  for n in range(len(shopList)):
    print(shopList[n])

# Input number of fruits to go into the list
numberOfFruits = int(input("Enter number of elements in the list : "))

# enter your list of fruits one by one
for i in range(0, numberOfFruits):
  item = input("Enter your Item to the List: ")
  shopList.append(item) # adding the element

# call your list function!
listFunc(shopList, numberOfFruits)
