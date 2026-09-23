
# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# média abaixo de 5.0: REPROVADO
# média entre 5.0 e 6.9: RECUPERAÇÃO
# média 7.0 ou suoerior: APROVADO
print('CALCULANDO A MÉDIA')

primeira_nota = float(input('Digite sua primeira nota: '))
segunda_nota =  float(input('Digite sua segunda nota: '))
media = (primeira_nota + segunda_nota) / 2

if media <= 4.9:
  print(f'Sua média é de {media}, voçê está REPROVADO!')
elif media >= 5 and media <= 6.9:
  print(f'Sua média foi de {media}, voçê está de RECUPERAÇÃO!')
elif media >= 7 and media <= 10:
  print(f'{"\033[1;34m"}Sua média foi de {media}, voçê foi APROVADO!')
else:
  print('As suas notas são INVÁLIDAS!')
