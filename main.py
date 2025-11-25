class Item:
    def __init__(self, nome, peso, delicia):
        self.nome = nome        
        self.peso = peso        
        self.delicia = delicia  
    
    def __str__(self):
        return f"{self.nome}: {self.peso}g, {self.delicia} delícia"

def Knapsack(num_itens, pesos, valores, capacidade_maxima):
    matriz = [[0 for capacidade in range(capacidade_maxima + 1)] for item in range(num_itens + 1)]
    
    for item in range(1, num_itens + 1):
        for capacidade in range(1, capacidade_maxima + 1):
            if pesos[item-1] > capacidade:
                matriz[item][capacidade] = matriz[item-1][capacidade]
            else:
                matriz[item][capacidade] = max(
                    matriz[item-1][capacidade], 
                    valores[item-1] + matriz[item-1][capacidade - pesos[item-1]]
                )
    
    return matriz

def recuperar_itens(matriz, num_itens, pesos, capacidade_maxima, itens_originais):
    itens_escolhidos = []
    cap_atual = capacidade_maxima
    
    for i in range(num_itens, 0, -1):
        if matriz[i][cap_atual] != matriz[i-1][cap_atual]:
            
            item_selecionado = itens_originais[i-1]
            itens_escolhidos.append(item_selecionado)
            
            cap_atual -= pesos[i-1]
            
    return itens_escolhidos

def Knapsack_com_itens(itens, capacidade_maxima):
    num_itens = len(itens)
    pesos = [item.peso for item in itens]
    valores = [item.delicia for item in itens]
    
    matriz = Knapsack(num_itens, pesos, valores, capacidade_maxima)
    
    valor_maximo = matriz[num_itens][capacidade_maxima]
    
    itens_selecionados = recuperar_itens(matriz, num_itens, pesos, capacidade_maxima, itens)
    
    return valor_maximo, itens_selecionados

def obter_capacidade_calorica():
    while True:
        try:
            print("--- Menu de Capacidade Calorica ---")
            print("Escolha sua capacidade calorica diaria (minimo 1500 calorias):")
            capacidade = int(input("Digite a capacidade desejada: "))
            
            if capacidade < 1500:
                print("Erro: A capacidade deve ser pelo menos 1500 calorias.")
                print("Tente novamente.\n")
                continue
            
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            return capacidade
            
        except ValueError:
            print("Erro: Digite apenas numeros inteiros.")
            print("Tente novamente.\n")
            import os
            os.system('cls' if os.name == 'nt' else 'clear')

def main():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    capacidade = obter_capacidade_calorica()
    
    itens = [
        Item("Pizza Inteira", 1200, 150),
        Item("Hambúrguer", 600, 60),
        Item("Salada", 100, 20),
        Item("Refrigerante", 300, 10),
        Item("Batata Frita", 400, 45)
    ]
    
    print("\n--- Itens Disponíveis ---")
    for item in itens:
        print(item)
    print("-" * 30)
    
    print(f"Capacidade escolhida: {capacidade} calorias")
    
    melhor_valor, lista_itens = Knapsack_com_itens(itens, capacidade)
    
    print(f"\nMelhor 'Delícia' Possível: {melhor_valor}")
    print("Itens Escolhidos (Backtracking):")
    peso_total = 0
    for item in lista_itens:
        print(f" -> {item.nome} ({item.peso}g)")
        peso_total += item.peso
    
    print(f"\nPeso total utilizado: {peso_total}g de {capacidade}g")
    print(f"Capacidade restante: {capacidade - peso_total}g")

if __name__ == "__main__":
    main()