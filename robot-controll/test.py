

array1 = ["elephant", "frog"]
array2 = ["middle", "top"]
array3 = ["left", "right"]

selectedAnimal = "elephant"
ID = 0

for x in array1:
    
    if x == selectedAnimal:
        verticalPosition = array2[ID]
        horizontalPosition  = array3[ID]
        print(verticalPosition)
        print(horizontalPosition)
        break
    
    ID = ID + 1

    
