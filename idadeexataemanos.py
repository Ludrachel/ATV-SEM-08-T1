dia_atual = int(input('digite o dia atual : '))
mes_atual = int(input('digite o mês atual : '))
ano_atual = int(input('digite o ano atual : '))

dia_nasc = int(input('digite o dia do seu nascimento : '))
mes_nasc = int(input('digite o mês do seu nascimento : '))
ano_nasc = int(input('digite o ano do seu nascimento : '))

idade = ano_atual - ano_nasc
if mes_atual < mes_nasc:
    idade-=1
elif mes_atual == mes_nasc and dia_atual < dia_nasc:
    idade-1
print(f'Você tem {idade} ou irá fazer {idade}')
