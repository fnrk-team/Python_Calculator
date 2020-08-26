x = float(input("Первое число: "))
y = float(input("Второе число: "))
action = input("Действие (+ - * /): ")

if action == "+":
    z = x + y
elif action == "-":
    z = x - y
elif action == "*":
    z = x * y
elif action == "/":
    if y == 0:
        z = "На ноль делить нельзя!"
    else:
        z = round(x / y, 2)
else:
    z = "Ошибка"

print(x, " ", action, " ", y, " = ", z)
