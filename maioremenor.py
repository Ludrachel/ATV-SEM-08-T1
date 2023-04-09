def maior(n1,n2,n3,n4,n5):
    m = 0
    if n1>n2 and n1>n3 and n1>n4 and n1>n5:
        m = n1
    elif n2>n1 and n2>n3 and n2>n4 and n2>n5:
        m = n2
    elif n3>n1 and n3>n2 and n3>n4 and n3>n5:
        m = n3
    elif n4>n1 and n4>n2 and n4>n3 and n4>n5:
        m = n4
    elif n5>n1 and n5>n2 and n5>n3 and n5>n4:
        m = n5
    return m

def menor(n1,n2,n3,n4,n5):
    m = 0
    if n1<n2 and n1<n3 and n1<n4 and n1<n5:
        m = n1
    elif n2<n1 and n2<n3 and n2<n4 and n2<n5:
        m = n2
    elif n3<n1 and n3<n2 and n3<n4 and n3<n5:
        m = n3
    elif n4<n1 and n4<n2 and n4<n3 and n4<n5:
        m = n4
    elif n5<n1 and n5<n2 and n5<n3 and n5<n4:
        m = n5
    return m
def main():
    num1 = int(input('digite um primeiro número : '))
    num2 = int(input('digite um segundo número : '))
    num3 = int(input('digite um terceiro número : '))
    num4 = int(input('digite um quarto número : '))
    num5 = int(input('digite um quinto número : '))

    print(f'Dentre esses o maior é o {maior(num1,num2,num3,num4,num5)}')
    print(f'Dentre esses o menor é o {menor(num1,num2,num3,num4,num5)}')
if __name__ == '__main__':
    main()
