from functools import reduce


# =============================================================================
# FUNÇÕES PURAS (Sem Efeitos Colaterais)
# =============================================================================

def calcular_total_carrinho(itens_carrinho):
    """
    Calcula o total do carrinho de compras.
    FUNÇÃO PURA: Não modifica dados, apenas retorna resultado.
    
    Args:
        itens_carrinho: Lista de dicionários com 'produto' e 'quantidade'
    
    Returns:
        float: Valor total do carrinho
    """
    if not itens_carrinho:
        return 0.0
    
    # MAP: Transforma cada item em seu subtotal
    # FUNÇÃO PURA: Não modifica itens_carrinho
    subtotais = map(
        lambda item: item['produto'].calcular_preco_final() * item['quantidade'],
        itens_carrinho
    )
    
    # REDUCE: Soma todos os subtotais
    total = reduce(lambda acc, valor: acc + valor, subtotais, 0.0)
    
    return total


def aplicar_desconto(valor, percentual):
    """
    Aplica desconto percentual sobre um valor.
    FUNÇÃO PURA: Retorna novo valor sem modificar o original.
    
    Args:
        valor: Valor original
        percentual: Desconto de 0 a 100
    
    Returns:
        float: Valor com desconto aplicado
    """
    if percentual < 0 or percentual > 100:
        return valor
    
    desconto = valor * (percentual / 100)
    return valor - desconto


# =============================================================================
# HIGHER-ORDER FUNCTIONS (Funções de Alta Ordem)
# =============================================================================
# PARADIGMA FUNCIONAL AVANÇADO: Funções que retornam ou recebem funções

def criar_filtro_por_preco_minimo(preco_minimo):
    """
    HIGHER-ORDER FUNCTION: Retorna uma função de filtro personalizada.
    Factory Function - Cria funções especializadas sob demanda.
    
    Este é um exemplo de CLOSURE (função que "captura" variável do escopo externo).
    
    Args:
        preco_minimo: Preço mínimo para filtrar
    
    Returns:
        function: Função que filtra produtos acima do preço mínimo
    
    Exemplo de uso:
        filtro_acima_100 = criar_filtro_por_preco_minimo(100)
        produtos_caros = filtro_acima_100(lista_produtos)
    """
    def filtrar(produtos):
        return list(filter(
            lambda p: p.calcular_preco_final() >= preco_minimo,
            produtos
        ))
    return filtrar


def criar_filtro_por_estoque_minimo(estoque_minimo):
    """
    HIGHER-ORDER FUNCTION: Retorna função de filtro por estoque.
    Factory Function - Permite criar diferentes critérios de filtro.
    
    Args:
        estoque_minimo: Quantidade mínima de estoque
    
    Returns:
        function: Função que filtra produtos com estoque >= estoque_minimo
    
    Exemplo de uso:
        filtro_em_estoque = criar_filtro_por_estoque_minimo(5)
        produtos_disponiveis = filtro_em_estoque(lista_produtos)
    """
    def filtrar(produtos):
        return list(filter(
            lambda p: p.get_estoque() >= estoque_minimo,
            produtos
        ))
    return filtrar


def aplicar_transformacao_em_produtos(produtos, funcao_transformacao):
    """
    HIGHER-ORDER FUNCTION: Recebe função como parâmetro.
    Aplica transformação genérica em lista de produtos.
    
    Args:
        produtos: Lista de objetos Produto
        funcao_transformacao: Função que será aplicada a cada produto
    
    Returns:
        list: Lista com resultados da transformação
    
    Exemplo de uso:
        nomes = aplicar_transformacao_em_produtos(produtos, lambda p: p.get_nome())
        precos = aplicar_transformacao_em_produtos(produtos, lambda p: p.get_preco())
    """
    return list(map(funcao_transformacao, produtos))


def aplicar_filtro_customizado(produtos, funcao_predicado):
    """
    HIGHER-ORDER FUNCTION: Recebe função predicado como parâmetro.
    Filtra produtos baseado em condição customizada.
    
    Args:
        produtos: Lista de objetos Produto
        funcao_predicado: Função que retorna True/False para cada produto
    
    Returns:
        list: Lista filtrada de produtos
    
    Exemplo de uso:
        baratos = aplicar_filtro_customizado(produtos, lambda p: p.get_preco() < 50)
        em_estoque = aplicar_filtro_customizado(produtos, lambda p: p.get_estoque() > 0)
    """
    return list(filter(funcao_predicado, produtos))


def compor_funcoes(*funcoes):
    """
    HIGHER-ORDER FUNCTION: Composição de funções.
    Retorna uma função que aplica múltiplas funções em sequência.
    
    COMPOSIÇÃO FUNCIONAL: f(g(h(x))) = compor(f, g, h)(x)
    
    Args:
        *funcoes: Sequência de funções a serem compostas
    
    Returns:
        function: Função composta
    
    Exemplo de uso:
        processar = compor_funcoes(
            lambda x: filtrar_produtos_em_estoque(x),
            lambda x: ordenar_por_preco(x)
        )
        resultado = processar(produtos)
    """
    def funcao_composta(valor):
        resultado = valor
        for funcao in funcoes:
            resultado = funcao(resultado)
        return resultado
    return funcao_composta


def criar_ordenador_customizado(funcao_chave, reverso=False):
    """
    HIGHER-ORDER FUNCTION: Retorna função de ordenação customizada.
    
    Args:
        funcao_chave: Função que extrai a chave de ordenação
        reverso: Se True, ordena em ordem decrescente
    
    Returns:
        function: Função que ordena lista de produtos
    
    Exemplo de uso:
        ordenar_por_estoque = criar_ordenador_customizado(lambda p: p.get_estoque())
        produtos_ordenados = ordenar_por_estoque(lista_produtos)
    """
    def ordenar(produtos):
        return sorted(produtos, key=funcao_chave, reverse=reverso)
    return ordenar


# =============================================================================
# FILTROS (Higher-Order Functions)
# =============================================================================

def filtrar_produtos_disponiveis(produtos):
    """
    Filtra produtos que estão disponíveis em estoque.
    FILTER: Filtra elementos baseado em condição.
    FUNÇÃO PURA: Retorna nova lista sem modificar original.
    
    Args:
        produtos: Lista de objetos Produto
    
    Returns:
        list: Lista filtrada de produtos disponíveis
    """
    return list(filter(lambda p: p.esta_disponivel(), produtos))


def filtrar_por_preco_maximo(produtos, preco_max):
    """
    Filtra produtos com preço até o valor máximo especificado.
    FILTER: Filtra elementos baseado em condição.
    FUNÇÃO PURA: Retorna nova lista sem modificar original.
    
    Args:
        produtos: Lista de objetos Produto
        preco_max: Preço máximo aceito
    
    Returns:
        list: Lista filtrada de produtos dentro do orçamento
    """
    return list(filter(
        lambda p: p.calcular_preco_final() <= preco_max,
        produtos
    ))


def filtrar_por_tipo(produtos, tipo_classe):
    """
    Filtra produtos por tipo (classe).
    FILTER: Filtra elementos baseado em condição.
    
    Args:
        produtos: Lista de objetos Produto
        tipo_classe: Classe para filtrar (ex: Livro, Eletronico)
    
    Returns:
        list: Lista filtrada por tipo
    """
    return list(filter(lambda p: isinstance(p, tipo_classe), produtos))


def filtrar_por_categoria(produtos, tipo):
    """
    Filtra produtos por categoria (livro ou eletronico).
    FILTER: Filtra elementos baseado em condição.
    FUNÇÃO PURA: Retorna nova lista sem modificar original.
    
    Args:
        produtos: Lista de objetos Produto
        tipo: String 'livro' ou 'eletronico'
    
    Returns:
        list: Lista filtrada por categoria
    """
    return list(filter(
        lambda p: p.__class__.__name__.lower() == tipo.lower(),
        produtos
    ))

def filtrar_produtos_em_estoque(produtos):
    """
    Filtra apenas produtos que têm estoque disponível.
    FILTER: Filtra elementos baseado em condição.
    FUNÇÃO PURA: Retorna nova lista sem modificar original.
    
    Args:
        produtos: Lista de objetos Produto
    
    Returns:
        list: Lista filtrada de produtos com estoque > 0
    """
    return list(filter(lambda p: p.get_estoque() > 0, produtos))


# =============================================================================
# MAPEAMENTO (Higher-Order Functions)
# =============================================================================

def listar_nomes_produtos(produtos):
    """
    Extrai lista de nomes dos produtos.
    MAP: Transforma cada produto em seu nome.
    FUNÇÃO PURA: Retorna nova lista sem modificar original.
    
    Args:
        produtos: Lista de objetos Produto
    
    Returns:
        list: Lista de strings com nomes dos produtos
    """
    return list(map(lambda p: p.get_nome(), produtos))


def calcular_precos_finais(produtos):
    """
    Calcula lista de preços finais dos produtos.
    MAP: Transforma cada produto em seu preço final.
    FUNÇÃO PURA: Retorna nova lista de valores.
    
    Args:
        produtos: Lista de objetos Produto
    
    Returns:
        list: Lista de floats com preços finais
    """
    return list(map(lambda p: p.calcular_preco_final(), produtos))


# =============================================================================
# ORDENAÇÃO (Higher-Order Functions)
# =============================================================================

def ordenar_por_preco(produtos, crescente=True):
    """
    Ordena produtos por preço final.
    FUNÇÃO PURA: Retorna nova lista ordenada sem modificar original.
    IMUTABILIDADE: Cria nova lista ordenada.
    
    Args:
        produtos: Lista de objetos Produto
        crescente: True para ordem crescente, False para decrescente
    
    Returns:
        list: Nova lista ordenada
    """
    # sorted() cria nova lista (não modifica original)
    return sorted(
        produtos,
        key=lambda p: p.calcular_preco_final(),
        reverse=not crescente
    )


def ordenar_por_nome(produtos):
    """
    Ordena produtos por nome alfabeticamente.
    FUNÇÃO PURA: Retorna nova lista ordenada.
    IMUTABILIDADE: Não modifica lista original.
    
    Args:
        produtos: Lista de objetos Produto
    
    Returns:
        list: Nova lista ordenada por nome
    """
    return sorted(produtos, key=lambda p: p.get_nome())


# =============================================================================
# AGREGAÇÃO (Reduce)
# =============================================================================

def contar_produtos_no_carrinho(itens_carrinho):
    """
    Conta total de produtos no carrinho (somando quantidades).
    REDUCE: Agrega valores em um resultado único.
    
    Args:
        itens_carrinho: Lista de dicionários com 'produto' e 'quantidade'
    
    Returns:
        int: Quantidade total de produtos
    """
    if not itens_carrinho:
        return 0
    
    return reduce(
        lambda acc, item: acc + item['quantidade'],
        itens_carrinho,
        0
    )


def calcular_total_impostos(itens_carrinho):
    """
    Calcula o total de impostos dos produtos no carrinho.
    REDUCE: Agrega valores em resultado único.
    MAP + REDUCE: Primeiro mapeia para impostos, depois soma.
    
    Args:
        itens_carrinho: Lista de dicionários com 'produto' e 'quantidade'
    
    Returns:
        float: Total de impostos
    """
    if not itens_carrinho:
        return 0.0
    
    # MAP: Calcula imposto de cada item
    impostos = map(
        lambda item: item['produto'].calcular_imposto() * item['quantidade'],
        itens_carrinho
    )
    
    # REDUCE: Soma todos os impostos
    return reduce(lambda acc, valor: acc + valor, impostos, 0.0)


# =============================================================================
# BUSCA (Recursão)
# =============================================================================

def buscar_produto_por_id_recursivo(produtos, produto_id, index=0):
    """
    Busca produto por ID usando RECURSÃO.
    RECURSÃO: Função que chama a si mesma.
    
    Args:
        produtos: Lista de objetos Produto
        produto_id: ID do produto a buscar
        index: Índice atual (usado internamente na recursão)
    
    Returns:
        Produto ou None: Produto encontrado ou None
    """
    # CASO BASE: Lista vazia ou chegou ao fim
    if index >= len(produtos):
        return None
    
    # CASO BASE: Encontrou o produto
    if produtos[index].get_id() == produto_id:
        return produtos[index]
    
    # RECURSÃO: Continua buscando no restante da lista
    return buscar_produto_por_id_recursivo(produtos, produto_id, index + 1)


def buscar_produto_por_nome(produtos, nome):
    """
    Busca produtos que contêm o nome especificado (case-insensitive).
    FILTER: Filtra elementos baseado em condição.
    
    Args:
        produtos: Lista de objetos Produto
        nome: Nome ou parte do nome a buscar
    
    Returns:
        list: Lista de produtos encontrados
    """
    nome_lower = nome.lower()
    return list(filter(
        lambda p: nome_lower in p.get_nome().lower(),
        produtos
    ))


# =============================================================================
# ESTATÍSTICAS (Higher-Order Functions)
# =============================================================================

def calcular_valor_medio_produtos(produtos):
    """
    Calcula o preço médio dos produtos.
    MAP + REDUCE: Mapeia preços e calcula média.
    
    Args:
        produtos: Lista de objetos Produto
    
    Returns:
        float: Preço médio ou 0 se lista vazia
    """
    if not produtos:
        return 0.0
    
    # MAP: Extrai preços finais
    precos = map(lambda p: p.calcular_preco_final(), produtos)
    
    # REDUCE: Soma todos os preços
    total = reduce(lambda acc, preco: acc + preco, precos, 0.0)
    
    return total / len(produtos)


def obter_produto_mais_caro(produtos):
    """
    Retorna o produto mais caro da lista.
    REDUCE: Encontra o máximo através de agregação.
    
    Args:
        produtos: Lista de objetos Produto
    
    Returns:
        Produto ou None: Produto mais caro ou None se lista vazia
    """
    if not produtos:
        return None
    
    return reduce(
        lambda p1, p2: p1 if p1.calcular_preco_final() > p2.calcular_preco_final() else p2,
        produtos
    )


def obter_produto_mais_barato(produtos):
    """
    Retorna o produto mais barato da lista.
    REDUCE: Encontra o mínimo através de agregação.
    
    Args:
        produtos: Lista de objetos Produto
    
    Returns:
        Produto ou None: Produto mais barato ou None se lista vazia
    """
    if not produtos:
        return None
    
    return reduce(
        lambda p1, p2: p1 if p1.calcular_preco_final() < p2.calcular_preco_final() else p2,
        produtos
    )


# =============================================================================
# VALIDAÇÕES (Funções Puras)
# =============================================================================

def validar_estoque_suficiente(produto, quantidade_desejada):
    """
    Valida se há estoque suficiente para a compra.
    FUNÇÃO PURA: Apenas retorna resultado booleano.
    
    Args:
        produto: Objeto Produto
        quantidade_desejada: Quantidade que cliente deseja comprar
    
    Returns:
        bool: True se há estoque suficiente, False caso contrário
    """
    return produto.get_estoque() >= quantidade_desejada


def validar_quantidade_positiva(quantidade):
    """
    Valida se quantidade é positiva.
    FUNÇÃO PURA: Apenas validação, sem efeitos colaterais.
    
    Args:
        quantidade: Valor a validar
    
    Returns:
        bool: True se quantidade é válida (> 0)
    """
    return quantidade > 0


# =============================================================================
# CÁLCULOS FINANCEIROS (Funções Puras)
# =============================================================================

def calcular_parcelas(valor_total, num_parcelas):
    """
    Calcula o valor de cada parcela.
    FUNÇÃO PURA: Apenas cálculo matemático, sem efeitos colaterais.
    
    Args:
        valor_total: Valor total da compra
        num_parcelas: Número de parcelas
    
    Returns:
        float: Valor de cada parcela
    """
    if num_parcelas <= 0:
        return valor_total
    return valor_total / num_parcelas


def obter_estatisticas_carrinho(itens_carrinho):
    """
    Retorna estatísticas do carrinho.
    FUNÇÃO PURA: Apenas análise de dados.
    
    Args:
        itens_carrinho: Lista de dicionários com 'produto' e 'quantidade'
    
    Returns:
        dict: Dicionário com estatísticas (total_itens, total_produtos, valor_total)
    """
    if not itens_carrinho:
        return {
            'total_itens': 0,
            'total_produtos': 0,
            'valor_total': 0.0
        }
    
    return {
        'total_itens': len(itens_carrinho),
        'total_produtos': contar_produtos_no_carrinho(itens_carrinho),
        'valor_total': calcular_total_carrinho(itens_carrinho)
    }
