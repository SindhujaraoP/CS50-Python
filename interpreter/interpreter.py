def main():
    x,y,z = input("Expression: ").split(" ")
    arith(x,y,z)


def arith(a,b,c):
    if b == '+':
        print (f"{float(int(a)+int(c)):.1f}")
    elif b == '-':
        print (f"{float(int(a)-int(c)):.1f}")
    elif b == '*':
        print (f"{float(int(a)*int(c)):.1f}")
    elif b == '/':
        print (f"{float(int(a)/int(c)):.1f}")


main()

