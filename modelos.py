"""
=============================================================================
PARADIGMA ORIENTADO A OBJETOS
=============================================================================
Implementa: Classes, Herança, Encapsulamento, Polimorfismo, Abstração
Responsável: Player 1
=============================================================================
"""

from abc import ABC, abstractmethod


# =============================================================================
# CLASSE ABSTRATA (Abstração)
# =============================================================================

class Produto(ABC):
    """
    Classe abstrata base para todos os produtos.
    ABSTRAÇÃO: Define contrato que todas as subclasses devem seguir.
    ENCAPSULAMENTO: Atributos privados (__)
    """
    
    def __init__(self, id, nome, preco, estoque):
        """
        Construtor da classe base.
        ENCAPSULAMENTO: Atributos privados (convenção __atributo)
        """
        self.__id = id
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque
    
    # =========================================================================
    # GETTERS E SETTERS (Encapsulamento)
    # =========================================================================
    
    def get_id(self):
        """Retorna o ID do produto"""
        return self.__id
    
    def get_nome(self):
        """Retorna o nome do produto"""
        return self.__nome
    
    def get_preco(self):
        """Retorna o preço base do produto"""
        return self.__preco
    
    def get_estoque(self):
        """Retorna a quantidade em estoque"""
        return self.__estoque
    
    def set_estoque(self, novo_estoque):
        """
        Altera o estoque do produto.
        ENCAPSULAMENTO: Controla como o atributo é modificado
        """
        if novo_estoque >= 0:
            self.__estoque = novo_estoque
    
    # =========================================================================
    # MÉTODOS ABSTRATOS (Abstração + Polimorfismo)
    # =========================================================================
    
    @abstractmethod
    def calcular_imposto(self):
        """
        MÉTODO ABSTRATO: Cada tipo de produto calcula seu imposto.
        POLIMORFISMO: Implementação diferente em cada subclasse.
        """
        pass
    
    @abstractmethod
    def exibir_info(self):
        """
        MÉTODO ABSTRATO: Cada tipo de produto exibe suas informações.
        POLIMORFISMO: Implementação específica em cada subclasse.
        """
        pass
    
    # =========================================================================
    # MÉTODOS CONCRETOS
    # =========================================================================
    
    def calcular_preco_final(self):
        """
        Calcula o preço final (preço base + imposto).
        Método concreto que usa método abstrato (calcular_imposto).
        """
        return self.__preco + self.calcular_imposto()
    
    def esta_disponivel(self):
        """Verifica se o produto está disponível em estoque"""
        return self.__estoque > 0


# =============================================================================
# SUBCLASSE: LIVRO (Herança)
# =============================================================================

class Livro(Produto):
    """
    Classe que representa um livro.
    HERANÇA: Estende a classe Produto
    POLIMORFISMO: Implementa métodos abstratos de forma específica
    """
    
    def __init__(self, id, nome, preco, estoque, autor, editora):
        """
        Construtor da subclasse.
        HERANÇA: Chama o construtor da classe pai (super)
        """
        super().__init__(id, nome, preco, estoque)
        self.__autor = autor
        self.__editora = editora
    
    # =========================================================================
    # GETTERS (Encapsulamento)
    # =========================================================================
    
    def get_autor(self):
        """Retorna o autor do livro"""
        return self.__autor
    
    def get_editora(self):
        """Retorna a editora do livro"""
        return self.__editora
    
    # =========================================================================
    # IMPLEMENTAÇÃO DE MÉTODOS ABSTRATOS (Polimorfismo)
    # =========================================================================
    
    def calcular_imposto(self):
        """
        POLIMORFISMO: Implementação específica do cálculo de imposto.
        Livros: 5% de imposto
        """
        return self.get_preco() * 0.05
    
    def exibir_info(self):
        """
        POLIMORFISMO: Implementação específica da exibição.
        Mostra informações específicas de livros (autor, editora).
        """
        preco_final = self.calcular_preco_final()
        imposto = self.calcular_imposto()
        
        info = f"[LIVRO]\n"
        info += f"   ID: {self.get_id()}\n"
        info += f"   Nome: {self.get_nome()}\n"
        info += f"   Autor: {self.__autor}\n"
        info += f"   Editora: {self.__editora}\n"
        info += f"   Preço Base: R$ {self.get_preco():.2f}\n"
        info += f"   Imposto (5%): R$ {imposto:.2f}\n"
        info += f"   Preço Final: R$ {preco_final:.2f}\n"
        info += f"   Estoque: {self.get_estoque()} unidades"
        
        return info


# =============================================================================
# SUBCLASSE: ELETRÔNICO (Herança)
# =============================================================================

class Eletronico(Produto):
    """
    Classe que representa um produto eletrônico.
    HERANÇA: Estende a classe Produto
    POLIMORFISMO: Implementa métodos abstratos de forma específica
    """
    
    def __init__(self, id, nome, preco, estoque, marca, garantia_meses):
        """
        Construtor da subclasse.
        HERANÇA: Chama o construtor da classe pai (super)
        """
        super().__init__(id, nome, preco, estoque)
        self.__marca = marca
        self.__garantia_meses = garantia_meses
    
    # =========================================================================
    # GETTERS (Encapsulamento)
    # =========================================================================
    
    def get_marca(self):
        """Retorna a marca do eletrônico"""
        return self.__marca
    
    def get_garantia_meses(self):
        """Retorna o período de garantia em meses"""
        return self.__garantia_meses
    
    # =========================================================================
    # IMPLEMENTAÇÃO DE MÉTODOS ABSTRATOS (Polimorfismo)
    # =========================================================================
    
    def calcular_imposto(self):
        """
        POLIMORFISMO: Implementação específica do cálculo de imposto.
        Eletrônicos: 15% de imposto
        """
        return self.get_preco() * 0.15
    
    def exibir_info(self):
        """
        POLIMORFISMO: Implementação específica da exibição.
        Mostra informações específicas de eletrônicos (marca, garantia).
        """
        preco_final = self.calcular_preco_final()
        imposto = self.calcular_imposto()
        
        info = f"[ELETRONICO]\n"
        info += f"   ID: {self.get_id()}\n"
        info += f"   Nome: {self.get_nome()}\n"
        info += f"   Marca: {self.__marca}\n"
        info += f"   Garantia: {self.__garantia_meses} meses\n"
        info += f"   Preço Base: R$ {self.get_preco():.2f}\n"
        info += f"   Imposto (15%): R$ {imposto:.2f}\n"
        info += f"   Preço Final: R$ {preco_final:.2f}\n"
        info += f"   Estoque: {self.get_estoque()} unidades"
        
        return info


# =============================================================================
# CLASSE: CARRINHO DE COMPRAS (Composição)
# =============================================================================

class CarrinhoDeCompras:
    """
    Gerencia os itens do carrinho de compras.
    COMPOSIÇÃO: Contém lista de produtos (has-a relationship)
    """
    
    def __init__(self):
        """Construtor: inicializa carrinho vazio"""
        self.__itens = []  # Lista de dicionários: {'produto': Produto, 'quantidade': int}
    
    def adicionar_item(self, produto, quantidade):
        """
        Adiciona produto ao carrinho.
        Se já existe, incrementa a quantidade.
        """
        # Verifica se produto já está no carrinho
        for item in self.__itens:
            if item['produto'].get_id() == produto.get_id():
                item['quantidade'] += quantidade
                return
        
        # Se não existe, adiciona novo item
        self.__itens.append({
            'produto': produto,
            'quantidade': quantidade
        })
    
    def remover_item(self, produto_id):
        """Remove produto do carrinho pelo ID"""
        self.__itens = [
            item for item in self.__itens 
            if item['produto'].get_id() != produto_id
        ]
    
    def listar_itens(self):
        """Retorna lista de itens do carrinho"""
        return self.__itens.copy()  # Retorna cópia para preservar encapsulamento
    
    def limpar(self):
        """Limpa todos os itens do carrinho"""
        self.__itens = []
    
    def esta_vazio(self):
        """Verifica se o carrinho está vazio"""
        return len(self.__itens) == 0


# =============================================================================
# CLASSE: CLIENTE (Composição)
# =============================================================================

class Cliente:
    """
    Representa um cliente da loja.
    COMPOSIÇÃO: Cliente "tem um" carrinho (has-a relationship)
    """
    
    def __init__(self, nome, cpf):
        """
        Construtor: cria cliente com carrinho vazio.
        COMPOSIÇÃO: Instancia CarrinhoDeCompras
        """
        self.__nome = nome
        self.__cpf = cpf
        self.__carrinho = CarrinhoDeCompras()  # Composição
    
    # =========================================================================
    # GETTERS (Encapsulamento)
    # =========================================================================
    
    def get_nome(self):
        """Retorna o nome do cliente"""
        return self.__nome
    
    def get_cpf(self):
        """Retorna o CPF do cliente"""
        return self.__cpf
    
    def get_carrinho(self):
        """
        Retorna o carrinho do cliente.
        COMPOSIÇÃO: Expõe o objeto carrinho
        """
        return self.__carrinho
