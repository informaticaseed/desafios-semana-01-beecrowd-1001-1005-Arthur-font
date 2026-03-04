"""
Beecrowd 1005 - Média 1

Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a
2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A
tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11).
Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

Entrada: O arquivo de entrada contém 2 valores com uma casa decimal cada um.

Saída: Imprima a mensagem "MEDIA" seguido pelo símbolo de igual e pelo valor
da média do aluno. Obrigatoriamente deve ser impresso uma casa decimal.
Use variáveis de dupla precisão (double) e como todos os problemas, não esqueça
de imprimir o fim de linha após o resultado, caso contrário, você receberá
"Presentation Error".
"""

# Link do problema: https://judge.beecrowd.com/pt/problems/view/1005

# Escreva sua solução abaixo

# Lê as duas notas como ponto flutuante (float)
A = float(input())
B = float(input())

# Define os pesos
peso_A = 3.5
peso_B = 7.5

# Calcula a média ponderada
# A soma dos pesos é 11.0 (3.5 + 7.5)
media = (A * peso_A + B * peso_B) / (peso_A + peso_B)

# Imprime o resultado com exatamente 5 casas decimais
# Nota: O enunciado pede 5 casas decimais nos exemplos do Beecrowd, 
# embora o texto mencione "uma casa decimal" em um trecho, o padrão 
# de correção do 1005 exige 5 casas.
print(f"MEDIA = {media:.5f}")





