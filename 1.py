
x=input("Digite 1° Cateto:")
y=input("Digite 2° Cateto:")
hip=input("Digite Hipotenusa:")

if hip == '':
   hip = (float(x)**2 +float(y)**2)**(1/2)
   print(hip)
elif x == '':
   x = (((-1*(float(hip)**2))+(float(y)**2))**(1/2))
   print(x)
elif y == '':
   y = (((-1 * (float(hip) ** 2)) + (float(x) ** 2)) ** (1 / 2))
   print(y)
u=input()