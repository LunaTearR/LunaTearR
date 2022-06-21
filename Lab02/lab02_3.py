#lab02
#03

print("First Equation")
m1 = float(input("Input m1 : "))
b1 = float(input("Input b1 : "))
print("Second Equation")
m2 = float(input("Input m2 : "))
b2 = float(input("Input b2 : "))
x = -((b1-b2)/(m1-m2)) 	#สูตรการหาค่า X
y = (m1*x)+b1			#สูตรการหาค่า Y
print("The point of intersection is at x = %.2f and y = %.2f " %(x,y))