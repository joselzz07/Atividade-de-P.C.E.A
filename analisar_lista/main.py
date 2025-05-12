# Lista fornecida de números

# Função para calcular as estatísticas
def estatisticas(lista):
    total = 0
    maior = lista[0]
    menor = lista[0]
    contador_pares = 0
    
    # Loop para iterar pela lista
    for num in lista:
        # Somando os números para calcular a média
        total += num
        
        # Verificando se o número é maior ou menor
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        
        # Verificando se o número é par
        if num % 2 == 0:
            contador_pares += 1
    
    # Calculando a média
    media = total / len(lista)
    
    # Exibindo os resultados
    print(f'Média: {media}')
    print(f'Maior número: {maior}')
    print(f'Menor número: {menor}')
    print(f'Quantidade de números pares: {contador_pares}')

# Chamando a função com a lista fornecida
estatisticas(numeros)