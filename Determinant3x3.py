a11 = float(input("a11: ").replace(",","."))
a12 = float(input("a12: ").replace(",","."))
a13 = float(input("a13: ").replace(",","."))
v1 = float(input("Vabaliige v1: ").replace(",","."))
a21 = float(input("a21: ").replace(",","."))
a22 = float(input("a22: ").replace(",","."))
a23 = float(input("a23: ").replace(",","."))
v2 = float(input("Vabaliige v2: ").replace(",","."))
a31 = float(input("a31: ").replace(",","."))
a32 = float(input("a32: ").replace(",","."))
a33 = float(input("a33: ").replace(",","."))
v3 = float(input("Vabaliige v3: ").replace(",","."))

def multiply(a, b ,c):
    return a *  b * c


def calculate(a11, a12, a13, a21, a22, a23, a31, a32, a33):
    p1 = multiply(a11, a22, a33)
    p2 = multiply(a21, a32, a13)
    p3 = multiply(a12, a23, a31)

    n1 = multiply(a13, a22, a31)
    n2 = multiply(a12, a21, a33)
    n3 = multiply(a11, a23, a32)


    result = p1 + p2 + p3 - n1 - n2 - n3
    return result
    


D = calculate(a11, a12, a13, a21, a22, a23, a31, a32, a33)
Dx = calculate(v1, a12, a13, v2, a22, a23, v3, a32, a33)
Dy = calculate(a11, v1, a13, a21, v2, a23, a31, v3, a33)
Dz = calculate(a11, a12, v1, a21, a22, v2, a31, a32, v3)

x = Dx / D
y = Dy / D
z = Dz / D

print(x)
print(y)
print(z)
