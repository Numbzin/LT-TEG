# 📚 GUIA DE ESTUDO COMPLETO - LOJA ONLINE MULTI-PARADIGMA

**Use este documento para estudar e entender TUDO que foi feito!**  
**O professor vai perguntar sobre cada parte - estejam preparados!** 🎯

---

## 📁 ESTRUTURA DO PROJETO

```
PROJETO_FINAL/
├── dados.json                    # Banco de dados (JSON)
├── modelos.py                    # ✅ PARADIGMA OO
├── motor_logico.py               # ✅ PARADIGMA FUNCIONAL
├── main.py                       # ✅ PARADIGMA ESTRUTURADO
├── GUIA_DE_ESTUDO.md            # Este guia
├── DIAGRAMA_UML_PLAYER4.md       # Guia do diagrama UML
└── README.md                     # Documentação principal
```

---

## 🎯 PARADIGMA ORIENTADO A OBJETOS (Player 1)

**Arquivo:** `modelos.py`  
**Responsável:** @lcdakebrada_17 (LC)

### 📦 Classes Implementadas:

#### 1. **Classe `Produto` (Superclasse)**

```python
class Produto:
    def __init__(self, id, nome, preco, estoque):
        self.__id = id          # Atributo PRIVADO (encapsulamento)
        self.__nome = nome      # Atributo PRIVADO
        self.__preco = preco    # Atributo PRIVADO
        self.__estoque = estoque # Atributo PRIVADO
```

**Conceitos demonstrados:**

- ✅ **ENCAPSULAMENTO:** Atributos privados com `__` (duplo underscore)
- ✅ **GETTERS:** Métodos `get_nome()`, `get_preco()`, etc.
- ✅ **MÉTODO ABSTRATO:** `calcular_imposto()` - força subclasses a implementar

**Por que atributos privados?**

- Impede acesso direto: `produto.__preco` dá erro!
- Força uso de getters: `produto.get_preco()` ✅

---

#### 2. **Classe `Livro` (Subclasse de Produto)**

```python
class Livro(Produto):
    def __init__(self, id, nome, preco, estoque, autor, editora):
        super().__init__(id, nome, preco, estoque)  # Chama construtor do pai
        self.__autor = autor      # Atributo específico de Livro
        self.__editora = editora  # Atributo específico de Livro
```

**Conceitos demonstrados:**

- ✅ **HERANÇA:** Livro herda de Produto (usa `super()`)
- ✅ **POLIMORFISMO:** Sobrescreve `calcular_imposto()` retornando 0.0
- ✅ **ESPECIALIZAÇÃO:** Adiciona atributos específicos (autor, editora)

**Polimorfismo em ação:**

```python
def calcular_imposto(self):
    return 0.0  # Livros são ISENTOS de imposto
```

---

#### 3. **Classe `Eletronico` (Subclasse de Produto)**

```python
class Eletronico(Produto):
    def calcular_imposto(self):
        return self.get_preco() * 0.15  # Eletrônicos têm 15% de imposto
```

**Polimorfismo:**

- Mesmo método `calcular_imposto()`
- Comportamento DIFERENTE em cada classe!
- Livro retorna 0, Eletrônico retorna 15%

---

#### 4. **Classe `Carrinho`**

```python
class Carrinho:
    def __init__(self):
        self.__itens = []  # Lista PRIVADA de itens
```

**Métodos:**

- `adicionar_item(produto, quantidade)` - adiciona produto
- `remover_item(produto_id)` - remove por ID
- `listar_itens()` - retorna lista de itens
- `limpar()` - esvazia o carrinho

---

#### 5. **Classe `Cliente`**

```python
class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__carrinho = Carrinho()  # COMPOSIÇÃO!
```

**Conceito:** COMPOSIÇÃO

- Cliente **TEM UM** Carrinho
- Carrinho é parte do Cliente
- Se Cliente é deletado, Carrinho também é!

---

### 🎤 PERGUNTAS QUE O PROFESSOR PODE FAZER (Player 1):

**P: O que é encapsulamento?**  
R: É esconder os detalhes internos da classe usando atributos privados (`__nome`). Só permite acesso via getters/setters.

**P: O que é herança?**  
R: É quando uma classe (Livro) herda características de outra (Produto). Livro e Eletrônico herdam de Produto.

**P: O que é polimorfismo?**  
R: É quando métodos com o mesmo nome têm comportamentos diferentes. `calcular_imposto()` funciona diferente em Livro (0%) e Eletrônico (15%).

**P: Por que usar `super()`?**  
R: Para chamar o construtor da classe pai e reaproveitar código. Evita repetir `self.__id`, `self.__nome`, etc.

**P: Qual a diferença entre Composição e Herança?**  
R: Herança é "É UM" (Livro É UM Produto). Composição é "TEM UM" (Cliente TEM UM Carrinho).

---

## 🧮 PARADIGMA FUNCIONAL (Player 2)

**Arquivo:** `motor_logico.py`  
**Responsável:** @numbzin (VOCÊ)

### 🔑 Conceitos Principais:

#### 1. **FUNÇÕES PURAS**

- Mesmo input → Mesmo output
- Sem efeitos colaterais (não altera variáveis globais)
- Não modifica a lista original

```python
def aplicar_desconto(valor, percentual):
    return valor * (1 - percentual / 100)  # NÃO altera 'valor'
```

---

#### 2. **MAP (Transformação)**

Transforma cada elemento de uma lista:

```python
def formatar_precos_para_exibicao(produtos):
    return list(map(lambda p: f"R$ {p.get_preco():.2f}", produtos))
```

**O que faz:** Pega lista de Produtos → Retorna lista de strings formatadas  
**Exemplo:** `[Produto(89.90), Produto(150.00)]` → `["R$ 89.90", "R$ 150.00"]`

---

#### 3. **FILTER (Filtragem)**

Seleciona elementos que atendem uma condição:

```python
def filtrar_por_categoria(produtos, tipo):
    return list(filter(
        lambda p: p.__class__.__name__.lower() == tipo.lower(),
        produtos
    ))
```

**O que faz:** Pega todos os produtos → Retorna só os da categoria especificada  
**Exemplo:** `filtrar_por_categoria(produtos, 'livro')` → Só livros

---

#### 4. **REDUCE (Agregação)**

Combina todos os elementos em um único valor:

```python
def calcular_total_carrinho(itens_carrinho):
    return reduce(
        lambda total, item: total + (item['produto'].calcular_preco_final() * item['quantidade']),
        itens_carrinho,
        0.0
    )
```

**O que faz:** Soma o valor de TODOS os itens do carrinho  
**Como funciona:**

1. Começa com 0.0
2. Para cada item: soma (preço × quantidade)
3. Retorna o total acumulado

---

#### 5. **FUNÇÕES DE ORDEM SUPERIOR**

**Requisito obrigatório do professor!**

##### a) Função que RECEBE outra função:

```python
def aplicar_operacao_em_produtos(produtos, operacao):
    return list(map(operacao, produtos))
```

**Uso:**

```python
nomes = aplicar_operacao_em_produtos(produtos, lambda p: p.get_nome())
```

##### b) Função que RETORNA outra função:

```python
def criar_filtro_por_preco(preco_limite):
    def filtro(produtos):
        return list(filter(
            lambda p: p.calcular_preco_final() <= preco_limite,
            produtos
        ))
    return filtro  # Retorna a FUNÇÃO, não o resultado!
```

**Uso:**

```python
filtro_ate_100 = criar_filtro_por_preco(100.0)  # Cria o filtro
produtos_baratos = filtro_ate_100(produtos)      # Usa o filtro
```

**Por que isso é importante?**  
Demonstra **CLOSURE** - a função interna "lembra" do `preco_limite`.

---

### 🎤 PERGUNTAS QUE O PROFESSOR PODE FAZER (Player 2):

**P: O que é uma função pura?**  
R: É uma função que sempre retorna o mesmo resultado para os mesmos argumentos e não tem efeitos colaterais (não altera variáveis externas).

**P: Qual a diferença entre map, filter e reduce?**  
R:

- **MAP:** Transforma cada elemento (1 lista → 1 lista do mesmo tamanho)
- **FILTER:** Seleciona elementos (1 lista → 1 lista menor)
- **REDUCE:** Combina tudo (1 lista → 1 valor)

**P: O que é uma função de ordem superior?**  
R: É uma função que recebe outra função como parâmetro OU retorna uma função como resultado.

**P: O que é closure?**  
R: É quando uma função interna "captura" variáveis da função externa. Exemplo: `criar_filtro_por_preco()` captura o `preco_limite`.

**P: Por que usar lambda?**  
R: Para criar funções anônimas pequenas e rápidas, principalmente em map/filter/reduce.

---

## 🏗️ PARADIGMA ESTRUTURADO (Player 3)

**Arquivo:** `main.py`  
**Responsável:** @leoz9404 (Leonardo)

### 🔑 Conceitos Principais:

#### 1. **FUNÇÕES PROCEDURAIS**

Funções que executam tarefas específicas:

```python
def exibir_cabecalho():
    print("="*60)
    print("🛒  LOJA ONLINE MULTI-PARADIGMA  🛒")
    print("="*60)
```

**Características:**

- Modularização: cada função faz UMA coisa
- Reutilização: chama a função sempre que precisar

---

#### 2. **ESTRUTURAS DE REPETIÇÃO**

##### a) **FOR Loop:**

```python
for produto in produtos:
    print(produto.exibir_info())
```

**Usado para:** Iterar sobre listas (produtos, itens do carrinho)

##### b) **WHILE Loop:**

```python
while True:
    exibir_menu()
    opcao = input("Digite sua opção: ")
    # ... processa opção
    if opcao == '0':
        break  # Sai do loop
```

**Usado para:** Menu infinito (até usuário escolher sair)

---

#### 3. **ESTRUTURAS CONDICIONAIS**

##### a) **IF/ELIF/ELSE:**

```python
if opcao == '1':
    listar_produtos(produtos)
elif opcao == '2':
    filtrar_por_categoria()
else:
    print("Opção inválida!")
```

##### b) **IF aninhado:**

```python
if item['tipo'] == 'livro':
    livro = Livro(...)
elif item['tipo'] == 'eletronico':
    eletronico = Eletronico(...)
```

---

#### 4. **SWITCH/CASE (MATCH/CASE)** ⭐ **REQUISITO OBRIGATÓRIO!**

```python
match opcao_pgto:
    case '1':
        # À vista com desconto
        valor_final = aplicar_desconto(total_geral, 5)
        print(f"Valor final: R$ {valor_final:.2f}")

    case '2':
        # Parcelado
        num_parcelas = int(input("Parcelas: "))
        valor_parcela = calcular_parcelas(total_geral, num_parcelas)
        print(f"{num_parcelas}x de R$ {valor_parcela:.2f}")

    case '0':
        print("Compra cancelada!")

    case _:  # Default
        print("Opção inválida!")
```

**Por que usamos match/case?**  
É o equivalente ao `switch` do Java/C. Python 3.10+ suporta!

---

#### 5. **TRY/EXCEPT (Tratamento de erros)**

```python
try:
    produto_id = int(input("Digite o ID: "))
except ValueError:
    print("❌ ERRO: Digite um número válido!")
    return
```

**Para que serve?**  
Evita que o programa quebre se o usuário digitar texto em vez de número.

---

#### 6. **CONTROLE DE ESTOQUE** ⚠️ **IMPORTANTE!**

##### Adicionar ao carrinho:

```python
# DEBITA do estoque
novo_estoque = produto.get_estoque() - quantidade
produto.set_estoque(novo_estoque)
```

##### Remover do carrinho:

```python
# DEVOLVE ao estoque
novo_estoque = produto.get_estoque() + quantidade
produto.set_estoque(novo_estoque)
```

**Requisito do professor:** Débito no estoque!

---

### 🎤 PERGUNTAS QUE O PROFESSOR PODE FAZER (Player 3):

**P: Qual a diferença entre for e while?**  
R:

- **FOR:** Itera sobre uma sequência conhecida (lista, range)
- **WHILE:** Repete enquanto condição for verdadeira (menu infinito)

**P: O que é break?**  
R: Interrompe o loop imediatamente e sai dele. Usado para sair do menu quando usuário escolhe "0".

**P: Por que usar try/except?**  
R: Para evitar que o programa quebre quando o usuário digita algo errado. Captura o erro e mostra mensagem amigável.

**P: O que é match/case?**  
R: É o switch do Python (3.10+). Compara um valor com vários casos possíveis. Mais limpo que vários if/elif.

**P: Como funciona o controle de estoque?**  
R: Quando adiciona ao carrinho, SUBTRAI do estoque. Quando remove do carrinho, DEVOLVE ao estoque.

---

## 🔗 INTEGRAÇÃO DOS 3 PARADIGMAS

### Como tudo se conecta:

```
main.py (Estruturado)
    ↓
    ├─ Usa CLASSES de modelos.py (OO)
    │   └─ Cliente, Produto, Carrinho
    │
    └─ Usa FUNÇÕES de motor_logico.py (Funcional)
        └─ filtrar_por_categoria, calcular_total_carrinho, etc.
```

### Exemplo prático na opção "Ver Carrinho":

```python
def exibir_carrinho(cliente):
    # ✅ OO: Acessa objeto Cliente
    carrinho = cliente.get_carrinho()
    itens = carrinho.listar_itens()

    # ✅ ESTRUTURADO: Loop FOR
    for item in itens:
        produto = item['produto']
        print(f"{produto.get_nome()}")

    # ✅ FUNCIONAL: Usa funções puras
    total = calcular_total_carrinho(itens)
    print(f"Total: R$ {total:.2f}")
```

**3 paradigmas em UMA função!** 🎯

---

## 📊 CHECKLIST FINAL ANTES DA APRESENTAÇÃO

### ✅ Paradigma OO (Player 1):

- [ ] Sabe explicar encapsulamento com exemplo
- [ ] Sabe explicar herança (Produto → Livro/Eletrônico)
- [ ] Sabe explicar polimorfismo (calcular_imposto)
- [ ] Sabe explicar composição (Cliente TEM Carrinho)

### ✅ Paradigma Funcional (Player 2):

- [ ] Sabe explicar map com exemplo
- [ ] Sabe explicar filter com exemplo
- [ ] Sabe explicar reduce com exemplo
- [ ] Sabe explicar função de ordem superior (recebe e retorna função)
- [ ] Sabe explicar o que é função pura

### ✅ Paradigma Estruturado (Player 3):

- [ ] Sabe explicar for vs while
- [ ] Sabe explicar if/elif/else
- [ ] Sabe explicar match/case (switch)
- [ ] Sabe explicar como funciona o débito de estoque
- [ ] Sabe explicar como os 3 paradigmas se integram

### ✅ Geral (todos):

- [ ] Sistema roda sem erros
- [ ] Todas as funcionalidades testadas
- [ ] Entendem o fluxo completo (carregar dados → adicionar carrinho → finalizar)
- [ ] Sabem onde está cada paradigma no código

---

## 🎯 DICAS PARA A ARGUIÇÃO

1. **Não decore, ENTENDA!**

   - Professor vai mudar a pergunta se perceber decoreba
   - Entenda o CONCEITO, não apenas o código

2. **Use exemplos práticos:**

   - "Polimorfismo é quando Livro tem imposto 0% e Eletrônico 15%"
   - Melhor que definição teórica!

3. **Mostre o código rodando:**

   - Professor vai pedir pra adicionar produto no carrinho
   - Vai pedir pra mostrar o estoque diminuindo
   - Pratiquem ANTES!

4. **Sejam honestos:**

   - Se não souber, diga "Não sei explicar bem, mas entendo que faz X"
   - Melhor que inventar resposta errada

5. **Ajudem uns aos outros:**
   - Se um player travar, outro pode complementar
   - Mostra trabalho em equipe!

---

## 💡 EXEMPLO DE FLUXO COMPLETO

**Para treinar antes da apresentação:**

1. **Rodar o programa:**

   ```bash
   python main.py
   ```

2. **Fazer uma compra completa:**

   - Digitar nome e CPF
   - Listar produtos (opção 1)
   - Adicionar Clean Code ao carrinho (opção 5)
   - Adicionar Mouse Gamer ao carrinho (opção 5)
   - Ver carrinho (opção 4)
   - Finalizar compra à vista (opção 7, depois 1)

3. **Explicar o que aconteceu em CADA etapa:**
   - Onde usou OO? (Cliente, Produto, Carrinho)
   - Onde usou Funcional? (calcular_total_carrinho, filtrar)
   - Onde usou Estruturado? (while, if/elif, match/case)

---

## 🚀 VOCÊS ESTÃO PRONTOS!

**Estudem este guia, rodem o sistema, entendam cada parte.**  
**O código está IMPECÁVEL e atende TODOS os requisitos!** ✅

**BOA SORTE NA APRESENTAÇÃO!** 🎉
