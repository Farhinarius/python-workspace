# find min max integer

# %%
# version 1
smallest = 100000
largest = -100000
while True:
    x = input("Enter a number: ")
    if x == "done" : break 
    try: 
       x = int(x)
    except: 
       print("invalid input")
    if (type(x) == int):
      if x < smallest: smallest = x
      if x > largest: largest = x

minimum = "Minimum is {}"
print(minimum.format(smallest))

maximum = "Maximum is {}"
print(maximum.format(largest))

# %%
# version 2
array = []
while True:
    x = input("Enter a number: ")
    if x == "done": break
    try:
       x = int(x)
    except:
       print("invalid input")
    if(type(x) == int):
       array.append(x)

# inputed_arr.copy(array) # if you want to copy inputed array
array.sort()
minimum = "Minimum is {}"
print(minimum.format(array[0]))

array.reverse()
maximum = "Maximum is {}"
print(maximum.format(array[0]))



