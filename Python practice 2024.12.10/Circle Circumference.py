import numpy as np

R = float(input("enter the radius in cm: "))
pi = np.pi

output1 = 2 * pi * R
output2 = pi * R**2
print(f"the circumference of this circle is {output1} cm, the area is {output2} cm^2")

