senhas = ['abc', 'segura123', '12345', 'python123', 'oi']
for senha in senhas:
     if len(senha) >= 6:
          print(f'A senha {senha} é valida.')
     else:
          print(f'A senha {senha} deve possuir no minimo 6 caracteres')  