#Treinando conceito if, elif, else

orcamento = float(input("Qual é o seu orçamento atual? R$ "))

if orcamento >= 5000:
    print("Você tem grana suficiente para a RTX 5070!")

elif orcamento >= 4000:
    # Ele só chega aqui se o orçamento for MENOR que 5000, mas MAIOR ou IGUAL a 4000.
    print("O orçamento dá para pegar uma RTX 5060 Ti!")

elif orcamento >= 2000:
    # Ele só chega aqui se for menor que 4000 e maior ou igual a 2000.
    print("Você pode comprar uma placa de vídeo de entrada.")
else:
    # Se o valor for menor que 2000, cai direto aqui.
    print("Melhor juntar mais um pouco para o upgrade.")