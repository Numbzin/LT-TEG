# 📝 ANOTAÇÕES PARA O CADERNO - LOJA ONLINE MULTI-PARADIGMA

> **Guia completo para copiar no caderno e estudar para a apresentação**

---

## 📚 PARTE 1: PARADIGMA ORIENTADO A OBJETOS (modelos.py)

### 🔷 **1. ENCAPSULAMENTO**

**O que é:** Esconder os detalhes internos da classe

**Como usar:**

- Atributos privados: `__nome` (dois underscores)
- Acesso via getters/setters

**Exemplo:**

```python
class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome        # PRIVADO
        self.__preco = preco      # PRIVADO

    def get_nome(self):           # GETTER
        return self.__nome

    def set_estoque(self, valor): # SETTER (com validação)
        if valor >= 0:
            self.__estoque = valor
```

**Por que usar:**

- ✓ Protege os dados
- ✓ Controla como os dados são modificados
- ✓ Evita modificações indevidas

---

### 🔷 **2. ABSTRAÇÃO**

**O que é:** Definir um "contrato" que as subclasses devem seguir

**Como usar:**

- Importar ABC (Abstract Base Class)
- Usar `@abstractmethod`

**Exemplo:**

```python
from abc import ABC, abstractmethod

class Produto(ABC):
    @abstractmethod
    def calcular_imposto(self):
        pass  # Subclasses DEVEM implementar
```

**Por que usar:**

- ✓ Força padronização
- ✓ Define comportamento obrigatório
- ✓ Não pode instanciar classe abstrata diretamente

---

### 🔷 **3. HERANÇA**

**O que é:** Classe filha herda atributos/métodos da classe pai

**Como usar:**

- `class Filha(Pai):`
- `super().__init__()` para chamar construtor do pai

**Exemplo:**

```python
class Livro(Produto):  # Livro HERDA de Produto
    def __init__(self, id, nome, preco, estoque, autor):
        super().__init__(id, nome, preco, estoque)  # Chama pai
        self.__autor = autor  # Atributo específico
```

**Por que usar:**

- ✓ Reaproveitamento de código
- ✓ Organização hierárquica
- ✓ Evita repetição

---

### 🔷 **4. POLIMORFISMO**

**O que é:** Mesmo método, comportamentos diferentes em cada classe

**Exemplo no projeto:**

- Produto define `calcular_imposto()` (abstrato)
- Livro implementa: retorna 5%
- Eletronico implementa: retorna 15%

**Código:**

```python
class Livro(Produto):
    def calcular_imposto(self):
        return self.get_preco() * 0.05  # 5%

class Eletronico(Produto):
    def calcular_imposto(self):
        return self.get_preco() * 0.15  # 15%
```

**Por que usar:**

- ✓ Flexibilidade
- ✓ Cada classe tem sua própria lógica
- ✓ Código mais organizado

---

### 🔷 **5. COMPOSIÇÃO**

**O que é:** Um objeto "TEM UM" outro objeto dentro dele

**Exemplo no projeto:**
Cliente TEM UM Carrinho

**Código:**

```python
class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__carrinho = CarrinhoDeCompras()  # COMPOSIÇÃO
```

**Por que usar:**

- ✓ Relacionamento forte (ciclo de vida dependente)
- ✓ Organização modular
- ✓ Se Cliente morre, Carrinho morre junto

---

## 📚 PARTE 2: PARADIGMA FUNCIONAL (motor_logico.py)

### 🟦 **1. FUNÇÕES PURAS**

**O que é:** Função que NÃO modifica nada, só retorna resultado

**Características:**

- ✓ Mesmo input = Mesmo output (sempre)
- ✓ Sem efeitos colaterais
- ✓ Não modifica variáveis externas

**Exemplo:**

```python
def calcular_total_carrinho(itens):
    # NÃO modifica itens
    # Apenas retorna valor
    return reduce(lambda acc, val: acc + val, subtotais)
```

**Por que usar:**

- ✓ Previsível
- ✓ Fácil de testar
- ✓ Sem bugs inesperados

---

### 🟦 **2. MAP (Transformação)**

**O que é:** Transforma cada elemento de uma lista

**Sintaxe:**

```python
map(função, lista)
```

**Exemplo:**

```python
# Pegar só os nomes dos produtos
nomes = list(map(lambda p: p.get_nome(), produtos))

# Calcular todos os preços finais
precos = list(map(lambda p: p.calcular_preco_final(), produtos))
```

**Como funciona:**

```
[Produto1, Produto2, Produto3]
         ↓ map(lambda p: p.get_nome())
    ["Nome1", "Nome2", "Nome3"]
```

---

### 🟦 **3. FILTER (Filtro)**

**O que é:** Filtra elementos que atendem uma condição

**Sintaxe:**

```python
filter(função_condicional, lista)
```

**Exemplo:**

```python
# Só produtos em estoque
disponiveis = list(filter(lambda p: p.get_estoque() > 0, produtos))

# Produtos até R$ 100
baratos = list(filter(lambda p: p.get_preco() <= 100, produtos))
```

**Como funciona:**

```
[Prod(R$50), Prod(R$150), Prod(R$30)]
         ↓ filter(lambda p: p.get_preco() <= 100)
    [Prod(R$50), Prod(R$30)]
```

---

### 🟦 **4. REDUCE (Agregação)**

**O que é:** Reduz lista inteira a UM único valor

**Sintaxe:**

```python
from functools import reduce
reduce(função, lista, valor_inicial)
```

**Exemplo:**

```python
# Somar tudo
total = reduce(lambda acc, val: acc + val, [10, 20, 30], 0)
# Resultado: 60

# No projeto: soma subtotais do carrinho
total = reduce(lambda acc, val: acc + val, subtotais, 0.0)
```

**Como funciona:**

```
[10, 20, 30]
  ↓ reduce com soma
   60
```

---

### 🟦 **5. LAMBDA (Função Anônima)**

**O que é:** Função pequena sem nome

**Sintaxe:**

```python
lambda parametros: expressão
```

**Exemplos:**

```python
# Função normal
def dobrar(x):
    return x * 2

# Com lambda
dobrar = lambda x: x * 2

# Uso comum: dentro de map/filter
list(map(lambda x: x * 2, [1, 2, 3]))  # [2, 4, 6]
```

---

### 🟦 **6. HIGHER-ORDER FUNCTIONS (Funções de Alta Ordem)**

**O que é:** Funções que recebem ou retornam outras funções

**Tipo 1: Recebe função como parâmetro**

```python
def aplicar_transformacao(lista, funcao):
    return list(map(funcao, lista))
```

**Tipo 2: Retorna uma função (Factory/Closure)**

```python
def criar_filtro(preco_minimo):
    def filtrar(produtos):
        return filter(lambda p: p.get_preco() >= preco_minimo, produtos)
    return filtrar

# Uso:
filtro_100 = criar_filtro(100)  # Cria função especializada
caros = filtro_100(produtos)     # Usa a função criada
```

---

### 🟦 **7. IMUTABILIDADE**

**O que é:** NÃO modificar dados originais, criar novos

**Exemplo ERRADO (modifica original):**

```python
lista.sort()  # Modifica a lista original ❌
```

**Exemplo CORRETO (imutável):**

```python
nova_lista = sorted(lista)  # Cria nova lista ordenada ✅
```

**No projeto:**

```python
def ordenar_por_preco(produtos):
    return sorted(produtos, key=lambda p: p.get_preco())
    # produtos original não é modificado
```

---

## 📚 PARTE 3: PARADIGMA ESTRUTURADO (main.py)

### 🟩 **1. LOOP WHILE**

**O que é:** Repete enquanto condição for verdadeira

**Sintaxe:**

```python
while condição:
    # código que repete
```

**Exemplo no projeto:**

```python
while True:  # Loop infinito
    exibir_menu()
    opcao = input("Opção: ")

    if opcao == '0':
        break  # SAI do loop
```

**Por que usar:**

- ✓ Menu que repete até usuário sair
- ✓ Processos contínuos

---

### 🟩 **2. LOOP FOR**

**O que é:** Itera sobre cada elemento de uma sequência

**Sintaxe:**

```python
for elemento in lista:
    # código
```

**Exemplos:**

```python
# Listar produtos
for produto in produtos:
    print(produto.exibir_info())

# Buscar produto por ID
for produto in produtos:
    if produto.get_id() == id_procurado:
        return produto
```

---

### 🟩 **3. CONDICIONAIS (IF/ELIF/ELSE)**

**O que é:** Executa código baseado em condições

**Sintaxe:**

```python
if condição1:
    # executa se condição1 for True
elif condição2:
    # executa se condição2 for True
else:
    # executa se nenhuma condição for True
```

**Exemplo no projeto:**

```python
if opcao == '1':
    listar_produtos()
elif opcao == '2':
    filtrar_categoria()
elif opcao == '0':
    break
else:
    print("Opção inválida!")
```

---

### 🟩 **4. MATCH/CASE (Switch/Case do Python)**

**O que é:** Escolhe ação baseado em valor (Python 3.10+)

**Sintaxe:**

```python
match variavel:
    case 'valor1':
        # ação 1
    case 'valor2':
        # ação 2
    case _:
        # default (qualquer outro valor)
```

**Exemplo no projeto (finalizar_compra):**

```python
match opcao_pgto:
    case '1':
        # À vista com desconto
        valor_final = aplicar_desconto(total, 5)
        print(f"Total: R$ {valor_final}")

    case '2':
        # Parcelado
        parcelas = calcular_parcelas(total, num_parcelas)

    case '0':
        print("Cancelado")

    case _:
        print("Opção inválida")
```

**Por que usar:**

- ✓ Mais legível que vários if/elif
- ✓ Mais organizado

---

### 🟩 **5. TRY/EXCEPT (Tratamento de Erros)**

**O que é:** Trata erros sem quebrar o programa

**Sintaxe:**

```python
try:
    # código que pode dar erro
except TipoDoErro:
    # o que fazer se der erro
```

**Exemplo:**

```python
try:
    quantidade = int(input("Quantidade: "))
except ValueError:
    print("Digite um número válido!")
```

---

## 📚 PARTE 4: INTEGRAÇÃO DOS 3 PARADIGMAS

### 🔄 **Como os paradigmas trabalham juntos:**

```
ADICIONAR AO CARRINHO (Exemplo Completo)

1. ESTRUTURADO: Loop e condicionais
   - Loop para buscar produto
   - IF para validar estoque

2. ORIENTADO A OBJETOS: Usar classes
   - cliente.get_carrinho() → acessa objeto Carrinho
   - carrinho.adicionar_item() → método da classe

3. FUNCIONAL: Calcular totais
   - calcular_total_carrinho(itens) → função pura
   - filter, map, reduce para processar dados
```

**Fluxo completo:**

```python
# 1. ESTRUTURADO: Loop para buscar
for produto in produtos:
    if produto.get_id() == id_busca:  # ESTRUTURADO: Condicional

        # 2. OO: Usar método da classe
        carrinho = cliente.get_carrinho()
        carrinho.adicionar_item(produto, qtd)

        # 3. FUNCIONAL: Calcular total
        total = calcular_total_carrinho(carrinho.listar_itens())
```

---

## 📚 PARTE 5: CONCEITOS IMPORTANTES

### ✨ **1. ESTOQUE (Requisito do trabalho)**

**DÉBITO (Adicionar ao carrinho):**

```python
novo_estoque = produto.get_estoque() - quantidade
produto.set_estoque(novo_estoque)
```

**CRÉDITO (Remover do carrinho):**

```python
novo_estoque = produto.get_estoque() + quantidade
produto.set_estoque(novo_estoque)
```

**PERSISTÊNCIA:**

```python
salvar_produtos_no_json(produtos)  # Salva no arquivo
```

---

### ✨ **2. JSON (Banco de Dados)**

**CARREGAR:**

```python
with open('dados.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
```

**SALVAR:**

```python
with open('dados.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, indent=2)
```

---

## 📚 PARTE 6: TABELA RESUMO

### 🎯 PARADIGMA OO - ONDE ESTÁ NO CÓDIGO

| Conceito           | Onde encontrar                      | Exemplo                                 |
| ------------------ | ----------------------------------- | --------------------------------------- |
| **Encapsulamento** | `modelos.py` - Atributos privados   | `self.__nome`                           |
| **Herança**        | `modelos.py` - Livro/Eletronico     | `class Livro(Produto):`                 |
| **Polimorfismo**   | `modelos.py` - calcular_imposto()   | Cada classe implementa diferente        |
| **Abstração**      | `modelos.py` - Classe Produto       | `@abstractmethod`                       |
| **Composição**     | `modelos.py` - Cliente tem Carrinho | `self.__carrinho = CarrinhoDeCompras()` |

---

### 🎯 PARADIGMA FUNCIONAL - ONDE ESTÁ NO CÓDIGO

| Conceito         | Onde encontrar                                      | Exemplo                                     |
| ---------------- | --------------------------------------------------- | ------------------------------------------- |
| **Map**          | `motor_logico.py` - listar_nomes_produtos()         | `map(lambda p: p.get_nome(), produtos)`     |
| **Filter**       | `motor_logico.py` - filtrar_por_categoria()         | `filter(lambda p: tipo, produtos)`          |
| **Reduce**       | `motor_logico.py` - calcular_total_carrinho()       | `reduce(lambda acc, val: acc + val, lista)` |
| **Função Pura**  | `motor_logico.py` - aplicar_desconto()              | Não modifica, só retorna                    |
| **Higher-Order** | `motor_logico.py` - criar_filtro_por_preco_minimo() | Retorna função                              |
| **Lambda**       | `motor_logico.py` - Em todos os map/filter          | `lambda p: p.get_nome()`                    |

---

### 🎯 PARADIGMA ESTRUTURADO - ONDE ESTÁ NO CÓDIGO

| Conceito         | Onde encontrar                 | Exemplo               |
| ---------------- | ------------------------------ | --------------------- |
| **While**        | `main.py` - função main()      | Loop infinito do menu |
| **For**          | `main.py` - listar_produtos()  | Itera sobre produtos  |
| **If/Elif/Else** | `main.py` - menu principal     | Valida opções do menu |
| **Match/Case**   | `main.py` - finalizar_compra() | Switch de pagamento   |
| **Try/Except**   | `main.py` - várias funções     | Trata erros de input  |

---

## 🎯 CHECKLIST PARA ARGUIÇÃO

```
☑ ORIENTADO A OBJETOS:
  ✓ Encapsulamento (atributos privados __)
  ✓ Herança (Livro/Eletronico herdam de Produto)
  ✓ Polimorfismo (calcular_imposto diferente em cada classe)
  ✓ Abstração (classe Produto é ABC)
  ✓ Composição (Cliente TEM Carrinho)

☑ FUNCIONAL:
  ✓ Map (transformar dados)
  ✓ Filter (filtrar dados)
  ✓ Reduce (agregar dados)
  ✓ Funções puras (sem efeitos colaterais)
  ✓ Higher-Order Functions (funções que retornam funções)
  ✓ Imutabilidade (sorted em vez de sort)

☑ ESTRUTURADO:
  ✓ Loop WHILE (menu principal)
  ✓ Loop FOR (iterar listas)
  ✓ IF/ELIF/ELSE (condicionais)
  ✓ MATCH/CASE (switch do Python)
  ✓ TRY/EXCEPT (tratamento de erros)
  ✓ Funções procedurais

☑ EXTRAS:
  ✓ Estoque (débito e crédito)
  ✓ Persistência (JSON)
  ✓ Integração dos 3 paradigmas
```

---

## 🎯 PERGUNTAS E RESPOSTAS PARA TREINAR

### **PARADIGMA OO**

**P: O que é encapsulamento?**
R: É esconder os detalhes internos da classe usando atributos privados (`__nome`) e controlando o acesso via getters/setters.

**P: Qual a diferença entre herança e composição?**
R: Herança é "É UM" (Livro É UM Produto). Composição é "TEM UM" (Cliente TEM UM Carrinho).

**P: O que é polimorfismo?**
R: É quando classes diferentes implementam o mesmo método de formas diferentes. Ex: `calcular_imposto()` é diferente em Livro e Eletronico.

---

### **PARADIGMA FUNCIONAL**

**P: O que é uma função pura?**
R: É uma função que não modifica nada e sempre retorna o mesmo resultado para os mesmos parâmetros.

**P: Qual a diferença entre map, filter e reduce?**
R: Map TRANSFORMA cada elemento, Filter SELECIONA elementos, Reduce AGREGA tudo em um valor único.

**P: O que é Higher-Order Function?**
R: É uma função que recebe ou retorna outras funções. Ex: `criar_filtro_por_preco()` retorna uma função de filtro.

---

### **PARADIGMA ESTRUTURADO**

**P: Por que usar match/case em vez de if/elif?**
R: É mais legível, organizado e específico para quando você tem múltiplas opções baseadas em um único valor.

**P: Qual a diferença entre for e while?**
R: For itera sobre uma sequência conhecida. While repete enquanto uma condição for verdadeira.

---

## 💡 DICAS FINAIS PARA APRESENTAÇÃO

1. **Pratique explicar cada conceito com suas palavras**
2. **Aponte no código onde cada conceito está**
3. **Execute o programa e mostre funcionando**
4. **Esteja preparado para perguntas cruzadas**
5. **Trabalhe em equipe - um complementa o outro**

---

**🎓 DICA DE ESTUDO:**

Copie essas anotações no caderno e depois tente explicar cada conceito sem olhar. Se conseguir explicar, você entendeu! 💪

**BOA APRESENTAÇÃO! 🎉**
