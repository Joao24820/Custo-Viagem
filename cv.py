dis = float(input('Qual é a distancia da sua viagem ?\nKM: '))
print('Voce esta prestes a começar uma viagem de {} Km'.format(dis))
if dis <= 200:
    p = dis * 0.45
else:
    p = dis * 0.50
print('E o preço da passagem será R$ {:.2f}'.format(p))
