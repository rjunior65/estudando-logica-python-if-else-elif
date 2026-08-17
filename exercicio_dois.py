#Treinando conceito if, elif, else

nota_aluno = float(input('qual a nota do aluno: '))

if nota_aluno >= 70 and nota_aluno <=100:
     print('aluno nota A')     
elif nota_aluno >= 60 and nota_aluno < 70:
     print ('aluno nota B')
elif nota_aluno >= 40 and nota_aluno < 60:
     print('aluno nota C')          
else:
     print('aluno nota D')


