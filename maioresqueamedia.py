def media(n1,n2,n3,n4,n5):
    return (n1 + n2 + n3 + n4 + n5)/5

num1 = int(input('digite um primeiro número : '))
num2 = int(input('digite um segundo número : '))
num3 = int(input('digite um terceiro número : '))
num4 = int(input('digite um quarto número : '))
num5 = int(input('digite um quinto número : '))

m = media(num1,num2,num3,num4,num5)
print(f'{m:.2f}')
if num1 > m:
    print(f'{num1:.2f}')
if num2 > m:
    print(f'{num2:.2f}')
if num3 > m:
    print(f'{num3:.2f}')
if num4 > m:
    print(f'{num4:.2f}')
if num5 > m:
    print(f'{num5:.2f}')
