import pandas as pd

# Função principal: calcula desconto
def calcular_desconto(valor, porcentagem):
    """
    Calcula o preço final após aplicar desconto.
    - valor: preço original (float)
    - porcentagem: % de desconto (ex: 20 para 20%)
    Retorna o valor final arredondado para 2 casas decimais.
    """
    if porcentagem < 0 or porcentagem > 100:
        raise ValueError("Porcentagem de desconto deve ser entre 0 e 100!")
    
    desconto = valor * (porcentagem / 100)
    valor_final = valor - desconto
    return round(valor_final, 2)

# Dados de exemplo (você pode trocar por uma lista maior ou ler de um CSV real depois)
produtos = {
    'Produto': ['Camisa Polo', 'Calça Jeans', 'Tênis Esportivo', 'Boné', 'Jaqueta'],
    'Preço Original (R$)': [89.90, 149.90, 299.00, 39.90, 199.90],
    'Desconto (%)': [10, 20, 15, 5, 25]
}

# Cria o DataFrame com pandas
df = pd.DataFrame(produtos)

# Aplica a função em cada linha (usando apply + lambda)
df['Preço Final (R$)'] = df.apply(
    lambda row: calcular_desconto(row['Preço Original (R$)'], row['Desconto (%)']),
    axis=1
)

# Mostra no terminal
print("Tabela de Produtos com Descontos:")
print(df)

# Salva em CSV (útil para enviar ao cliente ou abrir no Excel)
df.to_csv('produtos_com_desconto.csv', index=False, encoding='utf-8-sig')
print("\nArquivo 'produtos_com_desconto.csv' salvo com sucesso! Abra no Excel.")