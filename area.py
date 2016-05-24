print('Area,Volume & Perimeter calculator')

width = int(input("Enter width : "))
height = int(input("Enter height : "))
depth = int(input("Enter depth : "))

area = width * height
volume = area * depth
perimeter = (width*2)+(height*2)
print("Area : ", area)
print("Volume : ",volume)
print("Perimeter :",perimeter)
