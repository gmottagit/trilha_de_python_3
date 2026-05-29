def numero_reagentes(reagentes):
    reagentesSet = set(reagentes)
    print(reagentesSet)
    print(len(reagentesSet))


# Dados do inventário físico (cada índice representa um frasco individual)
reagentes = ['Etanol', 'Acetona', 'Etanol', 'Ácido Sulfúrico', 'Benzeno', 'Acetona',
'Etanol', 'Ácido Sulfúrico', 'Metanol', 'Tolueno', 'Etanol', 'Acetona', 'Ácido Acético', 'Etanol', 'Benzeno', 'Ácido Sulfúrico', 'Metanol', 'Ácido Acético',
'Etanol', 'Acetona', 'Tolueno', 'Ácido Sulfúrico', 'Benzeno', 'Etanol', 'Acetona',
'Metanol', 'Ácido Sulfúrico', 'Acetona', 'Ácido Acético', 'Etanol']

lotes = ['2023-ETA-01', '2023-ACE-01', '2023-ETA-01', '2023-SUL-01',
'2023-BEN-01', '2024-ACE-01', '2023-ETA-02', '2024-SUL-01', '2023-MET-01',
'2024-TOL-01', '2023-ETA-01', '2023-ACE-01', '2023-ACA-01', '2023-ETA-02',
'2023-BEN-01', '2023-SUL-01', '2023-MET-01', '2024-ACA-01', '2023-ETA-01',
'2023-ACE-01', '2024-TOL-01', '2024-SUL-01', '2023-BEN-01', '2023-ETA-01',
'2023-ACE-01', '2023-MET-01', '2023-SUL-01', '2024-ACE-01', '2024-ACA-01',
'2023-ETA-02']

purezas = [99.5, 92.0, 99.5, 98.0, 99.9, 98.5, 96.0, 99.0, 99.0, 98.8, 99.5, 92.0, 99.2,
96.0, 99.9, 98.0, 99.0, 95.0, 99.5, 92.0, 98.8, 99.0, 99.9, 99.5, 92.0, 99.0, 98.0, 98.5,
95.0, 96.0]

################################
# MAIN #
###############################
#1
numero_reagentes(reagentes)
print("\n")

#2
listaZip = zip(reagentes, lotes, purezas)
listaOrdenada = list(listaZip)

#3
for tuplas in listaOrdenada:
     print(f"Frasco do Lote: {tuplas[1]} | Reagente: {tuplas[0]} | Pureza: {tuplas[2]}%")

#4
lotesPuros = [purezas[1] for purezas in listaOrdenada if purezas[2] >= 98.0]
print("\n")
print(lotesPuros)