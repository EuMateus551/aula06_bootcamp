from datetime import time

### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir
# que todos os registros tenham valores positivos para `quantidade` e `preço`.
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos
# forem positivos ou "Dados inválidos" caso contrário.

quantidade = 20
preco = 100.00

if quantidade and preco > 0:
    print('Os dados são válidos!')
else:
    print('Os dados não são válidos!')

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT.
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

temp = int(input('Insira a temperatura atual: '))

if temp < 18:
    print(f'A temperatura está em {temp}°C e é considerada Baixa')
elif temp >= 18 and temp <= 26:
    print(f'A temperatura está em {temp}°C e é considerada Normal')
else:
    print(f'A temperatura está em {temp}°C e é considerada Alta')

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`,
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
log = {
    'timestamp': '2021-06-23 10:00:00',
    'level': 'ERROR',
    'message': 'Falha na conexão',
}
if log['level'] == 'ERROR':
    print(log['message'])

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação,
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha
# fornecido um email válido. Escreva um programa que valide essas condições
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

idade = int(input('Insira sua idade: '))
email = input('Insira seu email: ')

if idade >= 18 and idade <= 65:
    if '@' in email and '.' in email.split('@')[-1]:
        print('Seus dados foram validados!')
    else:
        print('Erro: formato de email inválido')
else:
    print('Sua idade é inválida')

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h).
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

valor = 12000.00
hora = time(20, 0)

if valor > 10000.00 and hora < 9 or hora > 18:
    print('Transação suspeita não autorizada')
else:
    print('Transação autorizada')

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = input('Digite um texto: ')

palavras = texto.split(' ')
contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

for palavra, quantidade in contagem.items():
    print(f'{palavra}:{quantidade}')

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

numeros = [10, 20, 40, 50, 60, 70, 80, 90, 100]

menor_numero = min(numeros)
maior_numero = max(numeros)

normalizardos = []
for n in numeros:
    valor = (n - menor_numero) / (maior_numero - menor_numero)
    normalizardos.append(valor)

print(normalizardos)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

usuarios: dict = [
    {'nome': 'mateus', 'email': 'mateus@gmail'},
    {'nome': '', 'email': 'joao@gmail'},
    {'nome': 'mateus', 'email': 'mateus@gmail'},
    {
        'nome': 'mateus',
    },
    {'nome': 'mateus', 'email': ''},
]
usuarios_com_falta: list = []

for usuario in usuarios:
    if (
        'nome' not in usuario
        or usuario['nome'] == ''
        or 'email' not in usuario
        or usuario['email'] == ''
    ):
        usuarios_com_falta.append(usuario)

print('Usuários que estão com dados incompletos:')
for i in usuarios_com_falta:
    print(i)

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

num = [1, 3, 35, 7, 2, 10, 8]

pares = []

for n in num:
    if n % 2 == 0:
        pares.append(n)

print(pares)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

produtos = [
    {'categoria': 'Eletrônicos'},
    {'categoria': 'Roupas'},
    {'categoria': 'Eletrônicos'},
    {'categoria': 'Livros'},
    {'categoria': 'Roupas'},
    {'categoria': 'Livros'},
]

vendas_por_categoria = {}

for produto in produtos:
    categoria = produto['categoria']
    if categoria in vendas_por_categoria:
        vendas_por_categoria[categoria] += 1
    else:
        vendas_por_categoria[categoria] = 1

print(vendas_por_categoria)


### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

entrada = ' '

while entrada.upper != 'SAIR':
    entrada = input('Digite alguma coisa: ')
    print(entrada)

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

num = -1
while num < 0 or num > 10:
    try:
        num = int(input('Insira um número de 0 até 10: '))
    except ValueError:
        print('Por favor, digite um número válido!')
print(f'Você digitou o número válido: {num}')

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

dados = list(range(0, 30))
quantos_por_vez = 6
pagina = 0

while True:
    inicio = pagina * quantos_por_vez
    fim = inicio + quantos_por_vez
    pagina_dados = dados[inicio:fim]

    if not pagina_dados:
        break

    print(f'Página {pagina+1}:{pagina_dados}')

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
usuario_salvo = 'Mateus'
senha_salva = 'mateus123'
limite_tentativas = 3

while limite_tentativas > 0:
    usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')

    if usuario == usuario_salvo:
        if senha == senha_salva:
            print('Login efetuado com sucesso!')
            break
        else:
            print('Senha digitada incorretamente')
    else:
        print('Usuário digitado incorretamente')
    limite_tentativas -= 1
else:
    print('Bloqueio: Limite de tentativas atingido')
### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

dados = list(range(0, 10))
indice = 0
condicao_parada = 10

while indice < len(dados) and dados[indice] != condicao_parada:
    print(f'dado: {dados[indice]}')
    indice += 1
