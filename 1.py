a = float(input('Plz enter first side: '))  
b = float(input('Plz enter second side: '))  
c = float(input('Plz enter third side: '))  
  
# calculate the semi-perimeter  
s = (a + b + c) / 2  
  
# calculate the area  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is %0.2f:' %area)  

print("Hello world")

