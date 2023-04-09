def datas(dia1,mes1,ano1,dia2,mes2,ano2):
    if ano1 > ano2:
        return f'{dia1}/{mes1}/{ano1}'
    elif ano2 > ano1:
        return f'{dia2}/{mes2}/{ano2}'
    elif mes1 > mes2:
        return f'{dia1}/{mes1}/{ano1}'
    elif mes2 > mes1:
        return f'{dia2}/{mes2}/{ano2}'
    elif dia1 > dia2:
        return f'{dia1}/{mes1}/{ano1}'
    elif dia2 > dia1:
        return f'{dia2}/{mes2}/{ano2}'
def main():
    d = int(input('digite algum dia : '))
    m = int(input('digite algum mês : '))
    a = int(input('digite algum ano : '))

    d2 = int(input('digite outro dia : '))
    m2 = int(input('digite outro mês : '))
    a2 = int(input('digite outro ano : '))

    print(f'A data mais recente é {datas(d,m,a,d2,m2,a2)}')
if __name__ == '__main__':
    main()
