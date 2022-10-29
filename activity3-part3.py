# define variables
shopList = []

# list function to print out list
def listFunc(shopList, numberOfFruits):
  for numberOfFruits in range(len(shopList)):
    print(shopList[numberOfFruits])

def createList():
  # Input number of fruits to go into the list
  numberOfFruits = int(input("Enter number of elements in the list : "))

  # enter your list of fruits one by one
  for i in range(0, numberOfFruits):
    item = input("Enter your Item to the List: ")
    shopList.append(item) # adding the element

  # call your list function!
  listFunc(shopList, numberOfFruits)

createList()
# want to add more fruits to your list?
x = int(input("Want to add more fruits? 1 for yes 2 for no: "))

if x == 1:
  createList()
else:
  print("have a good day!")
