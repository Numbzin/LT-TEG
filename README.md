# 🛒 LOJA ONLINE MULTI-PARADIGMA

**Trabalho em Grupo - Paradigmas de Programação**  
**Universidade:** UVA  
**Disciplina:** Paradigmas de Programação

---

## 👥 EQUIPE

- **Player 1 (Backend/OO):** @lcdakebrada_17 (LC) - `modelos.py`
- **Player 2 (Funcional):** @numbzin - `motor_logico.py`
- **Player 3 (Frontend):** @leoz9404 (Leonardo) - `main.py`
- **Player 4 (QA/Docs):** Testes e Documentação

---

## 🎯 OBJETIVO DO PROJETO

Desenvolver uma **Loja Online** que demonstre a integração de **3 paradigmas de programação**:

1. ✅ **Orientado a Objetos (OO):** Classes, Herança, Polimorfismo, Encapsulamento
2. ✅ **Funcional:** Map, Filter, Reduce, Funções Puras, Higher-Order Functions
3. ✅ **Estruturado:** Loops, Condicionais, Match/Case, Funções Procedurais

---

## 📁 ESTRUTURA DO PROJETO

```
PROJETO_FINAL/
├── dados.json              # Banco de dados (produtos)
├── modelos.py              # 🔷 Paradigma OO (Classes)
├── motor_logico.py         # 🟦 Paradigma Funcional
├── main.py                 # 🟩 Paradigma Estruturado (Interface)
├── GUIA_DE_ESTUDO.md       # 📚 Guia completo para estudar
├── DIAGRAMA_UML_PLAYER4.md # 📐 Guia do diagrama UML
└── README.md               # Este arquivo
```

---

## 🚀 COMO EXECUTAR

### Pré-requisitos:

- Python 3.10+ instalado
- Nenhuma biblioteca externa necessária (usa apenas bibliotecas padrão)

### Passos:

1. **Navegue até a pasta do projeto:**

```bash
cd "c:\Faculdade UVA\Paradigmas\TAG\PROJETO_FINAL"
```

2. **Execute o programa:**

```bash
python main.py
```

3. **Interaja com o menu:**

```
🛒  LOJA ONLINE MULTI-PARADIGMA  🛒
====================================
1 - Listar todos os produtos
2 - Filtrar produtos por categoria
3 - Ver carrinho
4 - Adicionar produto ao carrinho
5 - Remover produto do carrinho
6 - Finalizar compra
0 - Sair
====================================
```

---

## 🔷 PARADIGMA ORIENTADO A OBJETOS (modelos.py)

### Classes Implementadas:

#### 1. **Produto (Superclasse Abstrata)**

- Atributos privados: `__id`, `__nome`, `__preco`, `__estoque`
- Método abstrato: `calcular_imposto()`
- Demonstra: **Encapsulamento**

#### 2. **Livro (Subclasse)**

- Herda de `Produto`
- Atributos específicos: `__autor`, `__editora`
- `calcular_imposto()` retorna 0.0 (isenção)
- Demonstra: **Herança** e **Polimorfismo**

#### 3. **Eletronico (Subclasse)**

- Herda de `Produto`
- Atributos específicos: `__marca`, `__garantia_meses`
- `calcular_imposto()` retorna 15%
- Demonstra: **Herança** e **Polimorfismo**

#### 4. **Carrinho**

- Gerencia itens (adicionar, remover, listar)
- Lista privada: `__itens`
- Demonstra: **Agregação**

#### 5. **Cliente**

- Possui um `Carrinho` (composição)
- Atributos: `__nome`, `__cpf`
- Demonstra: **Composição**

**Conceitos:** Encapsulamento, Herança, Polimorfismo, Composição, Agregação

---

## 🟦 PARADIGMA FUNCIONAL (motor_logico.py)

### Funções Implementadas:

#### 1. **Map (Transformação)**

```python
formatar_precos_para_exibicao(produtos)
# Transforma lista de Produtos → lista de strings formatadas
```

#### 2. **Filter (Filtragem)**

```python
filtrar_por_categoria(produtos, tipo)
# Seleciona apenas produtos da categoria especificada
```

#### 3. **Reduce (Agregação)**

```python
calcular_total_carrinho(itens_carrinho)
# Combina todos os itens em um valor total
```

#### 4. **Higher-Order Functions**

**Função que RECEBE outra função:**

```python
aplicar_operacao_em_produtos(produtos, operacao)
# Aplica qualquer operação aos produtos
```

**Função que RETORNA outra função (Closure):**

```python
criar_filtro_por_preco(preco_limite)
# Retorna uma função de filtro personalizada
```

**Conceitos:** Funções Puras, Imutabilidade, Map/Filter/Reduce, Lambda, Closures

---

## 🟩 PARADIGMA ESTRUTURADO (main.py)

### Estruturas Demonstradas:

#### 1. **Loops**

- `for` - Iterar sobre produtos/carrinho
- `while` - Menu infinito até sair

#### 2. **Condicionais**

- `if/elif/else` - Validações e decisões
- **`match/case`** - Menu de pagamento (requisito obrigatório!)

#### 3. **Funções Procedurais**

- Cada função faz UMA tarefa específica
- Modularização e reutilização

#### 4. **Controle de Estoque**

- Débito ao adicionar no carrinho
- Devolução ao remover do carrinho

#### 5. **Tratamento de Erros**

- `try/except` para entradas inválidas

**Conceitos:** Sequência, Repetição, Seleção, Modularização

---

## 🔗 INTEGRAÇÃO DOS 3 PARADIGMAS

```
main.py (Estruturado)
    │
    ├─── USA ───> modelos.py (OO)
    │              └─ Cliente, Produto, Carrinho
    │
    └─── USA ───> motor_logico.py (Funcional)
                   └─ filtrar, calcular, formatar
```

**Exemplo prático:**

```python
# Estruturado: Loop
for item in carrinho.listar_itens():  # OO: Método de Carrinho
    produto = item['produto']
    print(produto.get_nome())         # OO: Getter

# Funcional: Função pura
total = calcular_total_carrinho(itens)
```

---

## 📊 FUNCIONALIDADES

### ✅ O Sistema Permite:

1. **Listar Produtos:** Exibe todos os produtos disponíveis
2. **Filtrar por Categoria:** Livros ou Eletrônicos
3. **Adicionar ao Carrinho:** Com controle de estoque
4. **Remover do Carrinho:** Devolve ao estoque
5. **Ver Carrinho:** Mostra itens e total
6. **Finalizar Compra:**
   - Pagamento à vista (5% desconto)
   - Pagamento parcelado (até 12x)
   - Usa **match/case** (requisito obrigatório!)

---

## 🧪 TESTANDO O SISTEMA

### Teste 1: Listar Produtos

```
Opção: 1
Resultado: Mostra todos os livros e eletrônicos
```

### Teste 2: Adicionar ao Carrinho

```
Opção: 4
ID: 1
Quantidade: 2
Resultado: Produto adicionado + estoque debitado
```

### Teste 3: Ver Carrinho

```
Opção: 3
Resultado: Mostra itens, quantidades e total com impostos
```

### Teste 4: Finalizar Compra

```
Opção: 6
Pagamento: 1 (À vista)
Resultado: Aplica 5% desconto + limpa carrinho
```

---

## 📚 DOCUMENTAÇÃO ADICIONAL

- **`GUIA_DE_ESTUDO.md`** - Estudo completo de todos os conceitos
- **`DIAGRAMA_UML_PLAYER4.md`** - Guia para criar diagrama de classes
- **`dados.json`** - Banco de dados de produtos

---

## 🎤 PERGUNTAS FREQUENTES

**P: Por que 3 arquivos separados?**  
R: Cada arquivo representa um paradigma diferente, facilitando a separação de responsabilidades.

**P: O estoque é controlado?**  
R: Sim! Ao adicionar ao carrinho, o estoque é DEBITADO. Ao remover, é DEVOLVIDO.

**P: Onde está o match/case?**  
R: Na função de finalizar compra (`main.py`), para escolher forma de pagamento.

**P: Como funciona o cálculo de impostos?**  
R: Livros são isentos (0%), Eletrônicos têm 15% de imposto. Isso demonstra **polimorfismo**.

**P: O que são Higher-Order Functions?**  
R: Funções que recebem ou retornam outras funções. Exemplo: `criar_filtro_por_preco()`.

---

## ✅ CHECKLIST DE REQUISITOS

### Paradigma OO:

- [x] Encapsulamento (atributos privados)
- [x] Herança (Produto → Livro/Eletronico)
- [x] Polimorfismo (calcular_imposto)
- [x] Composição (Cliente possui Carrinho)
- [x] Agregação (Carrinho usa Produtos)

### Paradigma Funcional:

- [x] Map (transformação)
- [x] Filter (filtragem)
- [x] Reduce (agregação)
- [x] Funções Puras
- [x] Higher-Order Functions (recebe e retorna função)
- [x] Lambda expressions

### Paradigma Estruturado:

- [x] Loops (for/while)
- [x] Condicionais (if/elif/else)
- [x] Match/Case (switch)
- [x] Try/Except
- [x] Funções procedurais
- [x] Controle de estoque

---

## 🎯 COMO ESTUDAR PARA A APRESENTAÇÃO

1. **Leia o GUIA_DE_ESTUDO.md** - Contém todas as explicações
2. **Execute o programa** - Teste todas as funcionalidades
3. **Entenda seu módulo** - Cada player deve dominar sua parte
4. **Pratique respostas** - Use as perguntas do guia
5. **Crie o diagrama UML** - Player 4 deve preparar

---

## 💡 DICAS PARA A APRESENTAÇÃO

- **Seja direto:** Explique o conceito e mostre no código
- **Use exemplos:** "Polimorfismo está aqui, veja como..."
- **Demonstre funcionando:** Execute e mostre o resultado
- **Trabalho em equipe:** Um completa o raciocínio do outro

---

## 📞 CONTATOS

- **Player 1:** @lcdakebrada_17
- **Player 2:** @numbzin
- **Player 3:** @leoz9404
- **Player 4:** (adicionar contato)

---

## 🏆 CONCLUSÃO

Este projeto demonstra com sucesso a **integração de 3 paradigmas de programação** em um sistema funcional e completo. Cada paradigma contribui com suas vantagens:

- **OO:** Organização e modelagem do domínio
- **Funcional:** Lógica clara e previsível
- **Estruturado:** Interface simples e direta

**Resultado:** Sistema coeso, bem estruturado e fácil de manter! ✅

---

**BOA APRESENTAÇÃO! 🎉**
