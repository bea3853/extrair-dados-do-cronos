import pandas as pd
import matplotlib.pyplot as plt

# Dados dos cursos
cursos = [
    "Mecânico de Usinagem"] * 62 + \
    ["NR - 11 - Operação de Ponte Rolante"] * 34 + \
    ["Operador de Empilhadeira de Pequeno Porte"] * 22 + \
    ["5S"] * 22 + \
    ["Analista da Qualidade"] * 8 + \
    ["Automação de Iluminação com Dispositivos Inteligentes"] * 17 + \
    ["Auxiliar De Almoxarife"] * 9 + \
    ["Auxiliar Mecânico de Manutenção"] * 10 + \
    ["Black Belt em Lean Seis Sigma"] * 8 + \
    ["Cálculo da Folha de Pagamento"] * 11 + \
    ["Caldeireiro Montador"] * 17 + \
    ["COMUNICAÇÃO EM LIBRAS E LÍNGUA PORTUGUESA ESCRITA"] * 8 + \
    ["Energia Solar Fotovoltaica - Tecnologias e Aplicações"] * 20 + \
    ["Excel Básico"] * 13 + \
    ["Excel Completo"] * 11 + \
    ["Implantação de Serviços em Nuvem AWS - Arquiteto de Soluções Associate"] * 10 + \
    ["Inspetor de Qualidade"] * 31 + \
    ["Instalador de Sistemas Fotovoltaicos"] * 11 + \
    ["Pacote Office"] * 16 + \
    ["Programação em Python"] * 21 + \
    ["SOLIDWORKS"] * 9 + \
    ["Torneiro Mecânico"] * 11


# Criar um DataFrame
df = pd.DataFrame(cursos, columns=['Curso'])

# Contar a frequência de cada curso
contagem = df['Curso'].value_counts()

# Criar o gráfico de pizza
plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(contagem, autopct='%1.1f%%', startangle=140)

# Ajustar a fonte da porcentagem
for text in autotexts:
    text.set_color('white')

# Adicionar uma legenda
plt.legend(wedges, contagem.index, title="Cursos", loc="upper left", bbox_to_anchor=(1, 1))

# Adicionar título
plt.title('Cursos mais procurados em Outubro de 2024')
plt.title('Fonte: Cronos CMS/SENAI | 29-10 | 16h')

# Exibir o gráfico
plt.axis('equal')  # Para garantir que o gráfico seja um círculo
plt.tight_layout()  # Para melhorar o layout
plt.show()

# Exibir a tabela com porcentagens
porcentagens = contagem / contagem.sum() * 100
print(porcentagens)
