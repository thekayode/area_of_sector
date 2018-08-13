'''
This programme is designed to help users calculate the area of sector of a circle.
The users are required to input the values of the radius, pi, angle.
'''
radius = float(input('Enter the radius: '))
pi =  float(input('Enter pi: '))
c = float(input('Enter central angle in degrees: '))
area = (pi) * radius**2 * (c/360)
print('The area is',(round(area,2)))
