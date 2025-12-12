# 📝 RESUMO PARA ESCREVER NO CADERNO (Versão Rápida)

> **⚠️ NÃO ESCREVA O CÓDIGO INTEIRO! Apenas as anotações abaixo!** > **O código completo está no computador - você só precisa ENTENDER os conceitos**

---

## 📐 DIAGRAMA UML - ARQUITETURA DO SISTEMA

### O que é UML?

**UML (Unified Modeling Language)** = Linguagem visual para documentar sistemas orientados a objetos.

### 🎯 Estrutura das Classes (HIERARQUIA)

```
         ┌─────────────┐
         │  Produto    │ ← Classe PAI (abstrata)
         │  (ABC)      │
         └──────┬──────┘
                │
        ┌───────┴───────┐
        │               │
   ┌────▼────┐    ┌────▼────────┐
   │  Livro  │    │ Eletronico  │ ← Classes FILHAS
   └─────────┘    └─────────────┘

   ┌──────────────┐      ┌──────────────────┐
   │   Cliente    │◆────→│ CarrinhoDeCompras│
   └──────────────┘      └──────────────────┘
        ↑                         ↑
        │                         │
    (tem um)                (contém múltiplos)
                                  │
                            ┌─────▼─────┐
                            │  Produto  │
                            └───────────┘
```

**Legenda:**

- `△` ou `▲` = **HERANÇA** ("é um")
- `◆────→` = **COMPOSIÇÃO** ("tem um", não existe sem o dono)
- `-` = atributo **PRIVADO** (encapsulado)
- `+` = método **PÚBLICO**

### 📦 Detalhes de Cada Classe

#### 1️⃣ **Produto** (Classe Abstrata - PAI)

```
Atributos privados:
  - __id: int
  - __nome: str
  - __preco: float
  - __estoque: int

Métodos principais:
  + calcular_imposto() → ABSTRATO (obriga filhos implementarem)
  + calcular_preco_final() → preco + imposto
  + exibir_info() → retorna string formatada
```

#### 2️⃣ **Livro** (Herda de Produto)

```
Atributos extras:
  - __autor: str
  - __editora: str

Implementação:
  + calcular_imposto() → retorna 0.0 (5% já embutido)
```

#### 3️⃣ **Eletronico** (Herda de Produto)

```
Atributos extras:
  - __marca: str
  - __garantia_meses: int

Implementação:
  + calcular_imposto() → retorna preco * 0.15 (15%)
```

#### 4️⃣ **CarrinhoDeCompras** (Independente)

```
Atributos:
  - __itens: list (lista de dicionários)

Métodos:
  + adicionar_item(produto, quantidade)
  + remover_item(produto_id)
  + calcular_total() → usa REDUCE (funcional!)
```

#### 5️⃣ **Cliente** (Composição)

```
Atributos:
  - __nome: str
  - __carrinho: CarrinhoDeCompras ← COMPOSIÇÃO!

Relacionamento: Cliente TEM UM Carrinho
```

### 🔗 Relacionamentos Importantes

| Tipo           | Exemplo                     | Significado                |
| -------------- | --------------------------- | -------------------------- |
| **Herança**    | Livro → Produto             | "Livro É UM Produto"       |
| **Herança**    | Eletronico → Produto        | "Eletronico É UM Produto"  |
| **Composição** | Cliente → CarrinhoDeCompras | "Cliente TEM UM Carrinho"  |
| **Agregação**  | Carrinho → Produtos         | "Carrinho CONTÉM Produtos" |

---

## 🎯 PARADIGMAS DO PROJETO

### 1️⃣ ORIENTADO A OBJETOS (modelos.py)

**5 conceitos principais:**

✅ **ENCAPSULAMENTO**

- Atributos privados: `__nome` (2 underscores)
- Getters: `get_nome()`
- Setters: `set_estoque(valor)`
- **POR QUE:** Protege os dados

✅ **ABSTRAÇÃO**

- `from abc import ABC, abstractmethod`
- Classe Produto é abstrata
- `@abstractmethod` força implementação nas subclasses
- **POR QUE:** Define "contrato" obrigatório

✅ **HERANÇA**

- Livro e Eletronico herdam de Produto
- `class Livro(Produto):`
- `super().__init__()` chama construtor do pai
- **POR QUE:** Reutilizar código

✅ **POLIMORFISMO**

- Mesmo método, comportamentos diferentes
- `calcular_imposto()` é diferente em cada classe:
  - Livro: 5%
  - Eletronico: 15%
- **POR QUE:** Flexibilidade

✅ **COMPOSIÇÃO**

- Cliente TEM UM Carrinho
- `self.__carrinho = CarrinhoDeCompras()`
- **DIFERENÇA:** Herança é "É UM", Composição é "TEM UM"

---

### 2️⃣ FUNCIONAL (motor_logico.py)

**6 conceitos principais:**

✅ **FUNÇÃO PURA**

- Não modifica nada
- Mesmo input = Mesmo output
- Sem efeitos colaterais

✅ **MAP** (Transformação)

```
[Prod1, Prod2] → map → ["Nome1", "Nome2"]
```

- `map(lambda p: p.get_nome(), produtos)`

✅ **FILTER** (Filtro)

```
[R$50, R$150, R$30] → filter ≤100 → [R$50, R$30]
```

- `filter(lambda p: p.get_preco() <= 100, produtos)`

✅ **REDUCE** (Agregação)

```
[10, 20, 30] → reduce soma → 60
```

- `reduce(lambda acc, val: acc + val, lista, 0)`

✅ **LAMBDA**

- Função anônima: `lambda x: x * 2`
- Usado dentro de map/filter/reduce

✅ **HIGHER-ORDER FUNCTION**

- Função que retorna outra função
- Ex: `criar_filtro_por_preco(100)` retorna função

---

### 3️⃣ ESTRUTURADO (main.py)

**5 estruturas principais:**

✅ **WHILE**

```python
while True:
    # menu
    if opcao == '0':
        break
```

✅ **FOR**

```python
for produto in produtos:
    print(produto.exibir_info())
```

✅ **IF/ELIF/ELSE**

```python
if opcao == '1':
    listar()
elif opcao == '2':
    filtrar()
else:
    print("Inválido")
```

✅ **MATCH/CASE** (Python 3.10+)

```python
match opcao_pgto:
    case '1':
        # à vista
    case '2':
        # parcelado
    case _:
        # default
```

✅ **TRY/EXCEPT**

```python
try:
    qtd = int(input())
except ValueError:
    print("Erro!")
```

---

## 📊 TABELA RÁPIDA DE ONDE ESTÁ CADA COISA

| Paradigma       | Conceito       | Arquivo         | Exemplo                |
| --------------- | -------------- | --------------- | ---------------------- |
| **OO**          | Encapsulamento | modelos.py      | `__nome`               |
| **OO**          | Herança        | modelos.py      | `class Livro(Produto)` |
| **OO**          | Polimorfismo   | modelos.py      | `calcular_imposto()`   |
| **Funcional**   | Map            | motor_logico.py | Transformar lista      |
| **Funcional**   | Filter         | motor_logico.py | Filtrar categoria      |
| **Funcional**   | Reduce         | motor_logico.py | Somar total            |
| **Estruturado** | While          | main.py         | Menu principal         |
| **Estruturado** | Match/Case     | main.py         | Formas de pagamento    |

---

## 🎯 PERGUNTAS MAIS PROVÁVEIS NA ARGUIÇÃO

### **SOBRE O DIAGRAMA UML**

**P: O que é o diagrama UML e para que serve?**
R: É uma representação visual da arquitetura do sistema. Mostra as classes, seus atributos, métodos e relacionamentos. Serve para documentar e facilitar o entendimento da estrutura do projeto.

**P: Qual a diferença entre os símbolos △ e ◆ no diagrama?**
R:

- `△` = HERANÇA (Livro É UM Produto)
- `◆` = COMPOSIÇÃO (Cliente TEM UM Carrinho)

**P: Por que Produto é abstrata no diagrama?**
R: Porque ela define um "contrato" que obriga as subclasses (Livro e Eletronico) a implementarem o método `calcular_imposto()`. Produto é apenas um modelo, não pode ser instanciada diretamente.

---

### **PARADIGMA OO**

**P: O que é encapsulamento?**
R: Esconder detalhes internos usando atributos privados (`__nome`) e controlar acesso via getters/setters.

**P: Diferença entre herança e composição?**
R: Herança = "É UM" (Livro É UM Produto)
Composição = "TEM UM" (Cliente TEM Carrinho)

**P: O que é polimorfismo?**
R: Mesmo método, comportamentos diferentes. Ex: `calcular_imposto()` varia por classe.

---

### **PARADIGMA FUNCIONAL**

**P: O que é função pura?**
R: Não modifica nada, sempre retorna mesmo resultado para mesmos parâmetros.

**P: Diferença entre map, filter e reduce?**
R:

- MAP = Transforma cada elemento
- FILTER = Seleciona elementos
- REDUCE = Agrega em valor único

**P: O que é Higher-Order Function?**
R: Função que recebe ou retorna outras funções.

---

### **PARADIGMA ESTRUTURADO**

**P: Por que usar match/case?**
R: Mais legível que vários if/elif quando há múltiplas opções baseadas em um valor.

**P: Diferença for vs while?**
R:

- FOR = Itera sequência conhecida
- WHILE = Repete enquanto condição for True

---

## ✅ CHECKLIST FINAL

```
☑ DIAGRAMA UML:
  ✓ Produto (classe abstrata)
  ✓ Livro e Eletronico (herança)
  ✓ Cliente e Carrinho (composição)
  ✓ Relacionamentos bem definidos

☑ OO:
  ✓ Encapsulamento (__atributos privados)
  ✓ Herança (Livro/Eletronico herdam Produto)
  ✓ Polimorfismo (calcular_imposto diferente)
  ✓ Abstração (Produto é ABC)
  ✓ Composição (Cliente TEM Carrinho)

☑ FUNCIONAL:
  ✓ Map (transformar)
  ✓ Filter (filtrar)
  ✓ Reduce (agregar)
  ✓ Funções puras
  ✓ Higher-Order Functions
  ✓ Lambda

☑ ESTRUTURADO:
  ✓ While (menu)
  ✓ For (iterar)
  ✓ If/Elif/Else
  ✓ Match/Case
  ✓ Try/Except

☑ EXTRAS:
  ✓ Estoque (débito/crédito)
  ✓ JSON (persistência)
  ✓ 3 paradigmas integrados
```

---

## 💡 COMO ESTUDAR

1. **Leia este resumo**
2. **Copie os conceitos principais no caderno** (sem códigos longos)
3. **Abra os arquivos no computador e localize cada conceito**
4. **Execute o programa e teste as funcionalidades**
5. **Treine explicar cada conceito com suas palavras**

---

## 🎤 ROTEIRO PARA APRESENTAÇÃO

1. **Mostre o programa funcionando** (2min)
2. **Explique o paradigma que você fez** (3min)
3. **Aponte no código onde está cada conceito** (2min)
4. **Responda perguntas** (3min)

**TOTAL: 10 minutos**

---

## 🔥 COLA RÁPIDA PARA URGÊNCIA

**OO:** Encapsulamento (`__privado`), Herança (`super()`), Polimorfismo (mesmo método, ações diferentes)

**Funcional:** Map (transforma), Filter (filtra), Reduce (soma tudo), Lambda (`lambda x: x*2`)

**Estruturado:** While (repete), For (itera), If/Elif (condicional), Match (switch), Try/Except (trata erro)

**Integração:** While busca produto (estruturado) → carrinho.adicionar (OO) → calcular_total com reduce (funcional)

---

**🎓 DICA FINAL:**

**NÃO tente memorizar código!** Memorize apenas:

- O que é cada conceito
- Onde está no projeto
- Por que usamos

O resto é só **executar e mostrar funcionando!** 💪

**BOA SORTE NA APRESENTAÇÃO! 🎉**
