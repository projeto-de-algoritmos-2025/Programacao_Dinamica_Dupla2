class Item:
    def __init__(self, nome, peso, delicia):
        self.nome = nome        
        self.peso = peso        
        self.delicia = delicia  
    
    def __str__(self):
        return f"{self.nome}: {self.peso} calorias, {self.delicia} delicia"


def Knapsack(num_itens, pesos, valores, capacidade_maxima):
    matriz = [[0 for capacidade in range(capacidade_maxima + 1)] for item in range(num_itens + 1)]
    
    for capacidade in range(capacidade_maxima + 1):
        matriz[0][capacidade] = 0
    
    for item in range(1, num_itens + 1):
        for capacidade in range(1, capacidade_maxima + 1):
            if pesos[item-1] > capacidade:
                matriz[item][capacidade] = matriz[item-1][capacidade]
            else:
                matriz[item][capacidade] = max(
                    matriz[item-1][capacidade], 
                    valores[item-1] + matriz[item-1][capacidade - pesos[item-1]]
                )
    return matriz[num_itens][capacidade_maxima]


def Knapsack_com_itens(itens, capacidade_maxima):
    num_itens = len(itens)
    pesos = [item.peso for item in itens]
    valores = [item.delicia for item in itens]
    
    return Knapsack(num_itens, pesos, valores, capacidade_maxima)


def teste():   
    capacidade = 2500       
    itens = [
        Item("Pizza", 500, 10),
        Item("Salada", 50, 1)
    ]
    
    print("Itens disponiveis:")
    for i, item in enumerate(itens, 1):
        print(f"{i}. {item}")
    
    resultado = Knapsack_com_itens(itens, capacidade)
    print(f"Resultado: {resultado} delicia")


if __name__ == "__main__":
    teste()
