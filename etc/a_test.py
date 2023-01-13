import aboutPython_Class
import random

# ab = aboutPython_Class

# car = ab.Car4("기아","k7","블랙","사천만원")

# car.carInfoShow()

print(dir(random))
for _ in range(2000):
    rd = random.randint(1,199)
    print(rd)
    if rd == 100:
        break