import math
 
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
 
Discriminant = b ** 2 - 4 * a * c
print("Дискриминант равен -->",Discriminant)
 
if Discriminant > 0:
    x1 = (-b + math.sqrt(Discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(Discriminant)) / (2 * a)
    print("x1 -->", x1, "\n", "x2 --> ", x2    )
elif Discriminant == 0:
    x = -b / (2 * a)
    print("x = -->", Discriminant)
else:
    print("Уравнение корней не имеет  \n",
          "Ответ: ∅ ")