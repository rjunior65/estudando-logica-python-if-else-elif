# 1. Perguntamos e limpamos os espaços/maiúsculas do texto
resposta_membro = input('O cliente é membro do clube? (sim/nao): ').strip().lower()
resposta_aniversario = input('Hoje é aniversário da loja? (sim/nao): ').strip().lower()

# 2. Convertemos as respostas de texto em variáveis booleanas (True ou False)
eh_membro = resposta_membro == 'sim'
aniversario_loja = resposta_aniversario == 'sim'

# 3. Usamos o operador 'and' para verificar se os dois critérios são verdadeiros
if eh_membro and aniversario_loja:
    print('Parabéns! O cliente ganhou o SUPER DESCONTO de aniversário!')
else:
    print('O cliente não atende aos requisitos para o desconto especial.')