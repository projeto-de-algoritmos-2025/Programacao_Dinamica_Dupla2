# ALGORITMO DE PROGRAMAÇÃO DINÂMICA — Mochila (Knapsack)

**Conteúdo da Disciplina**: Programação Dinâmica (PD)<br>

## Alunos

|Matrícula | Aluno |
| -- | -- |
| 23/1011293  | Enzo Emir |
| 23/1026465  | Marcelo Makoto |

<table>
  <tr>
    <td align="center"><a href="https://github.com/EnzoEmir"><img style="border-radius: 60%;" src="https://github.com/EnzoEmir.png" width="200px;" alt=""/><br /><sub><b>Enzo Emir</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/MM4k"><img style="border-radius: 60%;" src="https://github.com/MM4k.png" width="200px;" alt=""/><br /><sub><b>Marcelo Makoto</b></sub></a><br /></td>
  </tr>
</table>

## Sobre
Este projeto implementa o clássico problema da Mochila 0/1 usando Programação Dinâmica. O contexto escolhido é gastronômico: dado um limite de calorias diárias (capacidade da mochila), é selecionado um subconjunto de itens alimentares que maximize os "pontos de delícia" sem ultrapassar a capacidade. O usuário informa sua capacidade calórica (mínimo 1500) e o algoritmo retorna a melhor combinação possível, exibindo também o que sobrou de calorias e uma curiosidade sobre quantos gramas de açúcar equivaleriam.

## Algoritmo (visão geral)
O problema da Mochila 0/1 consiste em, dado um conjunto de n itens (cada um com peso e valor), escolher um subconjunto que maximize o valor total sem exceder a capacidade máxima. A solução por Programação Dinâmica constrói uma matriz `dp` de dimensões `(n+1) x (capacidade+1)` onde `dp[i][c]` representa o melhor valor possível usando apenas os primeiros `i` itens com capacidade `c`.

Transição:
- Se o peso do item i excede `c`: `dp[i][c] = dp[i-1][c]`.
- Caso contrário: `dp[i][c] = max(dp[i-1][c], valor_i + dp[i-1][c - peso_i])`.

Após preencher a matriz, o valor ótimo está em `dp[n][capacidade]`. Em seguida faz-se backtracking para recuperar quais itens foram escolhidos: percorremos de `i = n` até `1` verificando se `dp[i][capacidade_atual] != dp[i-1][capacidade_atual]`. Quando diferente, significa que o item i foi incluído; reduzimos a capacidade pelo peso dele e seguimos.

### Complexidade
- Tempo: O(n * C), onde n é o número de itens e C a capacidade.
- Espaço: O(n * C) (poderia ser otimizado para O(C) se só quiséssemos o valor, mas perderíamos a recuperação direta dos itens sem lógica adicional).

## Estrutura do Código
- Classe `Item`: encapsula nome, peso (calorias) e delícia (valor).
- Função `Knapsack(...)`: monta a matriz de DP completa.
- Função `recuperar_itens(...)`: realiza o backtracking para listar os itens escolhidos.
- Função `Knapsack_com_itens(...)`: empacota o fluxo (cria listas de pesos/valores, chama DP, recupera solução).
- Função `obter_capacidade_calorica()`: interação robusta com o usuário garantindo mínimo de 1500 calorias.
- Função `main()`: função principal, execução do algoritmo e saída formatada.

## Exemplo de Saída
```
--- Itens Disponíveis ---
Pizza Inteira: 1200g, 150 delícia
...
Capacidade escolhida: 2000 calorias

275 pontos de delicia
Itens Escolhidos (Backtracking):
 -> Pizza Inteira (1200 calorias)
 -> Milkshake de Chocolate (800 calorias)

Peso total utilizado: 2000 calorias de 2000 calorias
Não tinha como ter comido melhor!!!
```
Obs: O exemplo acima é ilustrativo; a combinação depende da capacidade inserida e pode variar.

## Screenshots
Abaixo estão capturas de tela do programa em execução (exemplos):

<p align="center">
  <img src="assets/modelo.png" alt="Print 1" width="700px"/>
</p>

## Instalação
Requisitos:
- Python 3.8+

Passos:
1. Clonar o repositório.
2. (Opcional) Criar e ativar um ambiente virtual.

```powershell
python -m venv .venv
./.venv/Scripts/Activate.ps1
```

## Uso
1. Abra um terminal na pasta do projeto.
2. Execute:

```powershell
python main.py
```
3. Informe a capacidade calórica desejada (>= 1500) e aguarde o resultado.

## Estrutura do Repositório
- `main.py` — implementação do algoritmo da Mochila 0/1 com interação via terminal.
- `README.md` — documentação e instruções do projeto.

## Apresentação
Vídeo disponível em: [Vídeo](https://youtu.be/WpSouqRjYZY) 