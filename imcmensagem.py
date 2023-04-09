def imc(massa,altura):
    x = massa / (altura **2)
    if x < 18.5:
        return f'{x:.0f}\nAbaixo do peso'
    elif x < 25:
        return f'{x:.0f}\nPeso normal'
    elif x < 30:
        return f'{x:.0f}\nSobre peso'
    elif x < 35:
        return f'{x:.0f}\nObeso leve'
    elif x < 40:
        return f'{x:.0f}\nObeso moderado'
    elif x >= 40:
        return f'{x:.0f}\nObeso mórbido'
def main():
    m = float(input('digite sua massa corporal : '))
    a = float(input('digite sua altura : '))

    print(imc(m,a))
if __name__ == '__main__':
    main()
