op = input("Operation + - * /.")
First = input("First number.")
Second = input("Second number.")
if op == "+":
    ans = (float(First) + (float(Second)))
if op == "-":
    ans = (float(First) - (float(Second)))
if op == "*":
    ans = (float(First) * (float(Second)))
if op == "/":
    ans = (float(First) / (float(Second)))


print(float(ans))
