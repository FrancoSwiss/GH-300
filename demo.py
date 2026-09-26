# function to calculate the area of a circle
def area_of_circle(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return area

area = area_of_circle(5)
print(area)