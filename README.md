# trilha_de_python_3
DESAFIO 3

Este programa tem como objetivo estruturar os frascos de reagentes químicos cujos dados foram importados do armazenamento e estão espalhados em três listas diferentes. As listas contêm os seguintes dados separados: 
- nomes dos reagentes;
- códigos de lote (incluindo ano e identificação do produto);
- percentual de pureza (%) correspondente a cada frasco.

O código recebe essas listas, faz a correspondência entre os dados através da função zip e depois tranforma esse conjunto de dados em uma lista de tuplas estruturadas. Depois disso o codigo faz para o usuário esses seguintes passos:
1. Imprime o nome dos reagentes disponíveis;
2. Imprime a quantidade de reagentes diferentes;
3. Imprime os frascos estruturados no formato: "Frasco do Lote: [Lote] | Reagente: [Nome] | Pureza: [Valor]%"
4. Imprime os lotes que contém a pureza igual ou maior que 98.0%

---------------
INSTRUÇÕES:

Para testar o código, você deve rodar o arquivo inventario_lab.py em uma maquina que contém o Python instalado ou através de ferramentas online como Google Colab.

-------------
PERGUNTAS TEÓRICAS:

● Levando em consideração a estrutura do nosso inventário, por que
seria incorreto usar a função dict() para transformar o resultado do
nosso zip() em um dicionário, utilizando o nome do reagente como
"Chave" e o lote como "Valor"?

Seria incorreto porque existem vários frascos do mesmo reagente no inventário. Em um dicionário, as chaves devem ser únicas para que um dicionário possa funcionar como o esperado.

● O que a função zip() gera na memória do Python antes de usarmos a
função list() para forçar a visualização dos dados?

A função zip() gera um objeto iteravel do tipo zip. Esse objeto não armazena imediatamente todos os dados na memória, mas produz os elementos sob demanda conforme são percorridos.

● Observando o seu código final, de que forma o List Comprehension
substitui a necessidade de criar uma lista vazia e usar a estrutura de
repetição for tradicional acompanhada do método .append()?

O List Comprehension permite criar e preencher uma lista em uma única linha de código. Em vez de ter que criar uma lista vazia, percorrer os elementos com for, verificar uma condição e usar .append() para adicionar os valores um de cada vez, o List Comprehension permite fazer tudo isso de maneira integrada.
