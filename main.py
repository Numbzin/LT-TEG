"""
=============================================================================
PARADIGMA ESTRUTURADO
=============================================================================
Implementa: Funções Procedurais, Loops, Condicionais, Switch/Case
Integra: Paradigma OO (classes) + Funcional (funções puras)
Responsável: Player 3
=============================================================================
"""

import json
from modelos import Produto, Livro, Eletronico, Cliente
from motor_logico import (
    filtrar_por_categoria,
    filtrar_produtos_em_estoque,
    calcular_total_carrinho,
    aplicar_desconto,
    calcular_parcelas,
    obter_estatisticas_carrinho
)


# =============================================================================
# FUNÇÕES DE CARREGAMENTO E PERSISTÊNCIA
# =============================================================================

def carregar_produtos_do_json():
    """
    Carrega produtos do arquivo JSON e cria objetos.
    Retorna lista de objetos Produto (Livro ou Eletronico)
    """
    try:
        with open('dados.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            produtos = []
            
            # Loop FOR: itera sobre cada item do JSON
            for item in dados['produtos']:
                # Condicional IF/ELIF: cria objeto baseado no tipo
                if item['tipo'] == 'livro':
                    produto = Livro(
                        item['id'], item['nome'], item['preco'],
                        item['estoque'], item['autor'], item['editora']
                    )
                elif item['tipo'] == 'eletronico':
                    produto = Eletronico(
                        item['id'], item['nome'], item['preco'],
                        item['estoque'], item['marca'], item['garantia_meses']
                    )
                else:
                    continue
                
                produtos.append(produto)
            
            return produtos
    
    except FileNotFoundError:
        print("[ERRO] Arquivo dados.json não encontrado!")
        return []


def salvar_produtos_no_json(produtos):
    """
    Salva produtos atualizados no arquivo JSON
    """
    try:
        dados = {'produtos': []}
        
        # Loop FOR: converte objetos para dicionários
        for produto in produtos:
            produto_dict = {
                'id': produto.get_id(),
                'nome': produto.get_nome(),
                'preco': produto.get_preco(),
                'estoque': produto.get_estoque()
            }
            
            # Condicional: adiciona campos específicos por tipo
            if isinstance(produto, Livro):
                produto_dict.update({
                    'tipo': 'livro',
                    'autor': produto.get_autor(),
                    'editora': produto.get_editora()
                })
            elif isinstance(produto, Eletronico):
                produto_dict.update({
                    'tipo': 'eletronico',
                    'marca': produto.get_marca(),
                    'garantia_meses': produto.get_garantia_meses()
                })
            
            dados['produtos'].append(produto_dict)
        
        with open('dados.json', 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=2, ensure_ascii=False)
        
        return True
    
    except Exception as e:
        print(f"[ERRO] Erro ao salvar: {e}")
        return False


# =============================================================================
# FUNÇÕES DE INTERFACE (UI)
# =============================================================================

def exibir_cabecalho():
    """Exibe o cabeçalho da aplicação"""
    print("\n" + "="*70)
    print("       LOJA ONLINE MULTI-PARADIGMA")
    print("="*70)


def exibir_menu():
    """Exibe o menu principal"""
    print("\n[MENU PRINCIPAL]")
    print("  [1] Listar todos os produtos")
    print("  [2] Filtrar por categoria")
    print("  [3] Buscar produto por ID")
    print("  [4] Ver carrinho")
    print("  [5] Adicionar produto ao carrinho")
    print("  [6] Remover produto do carrinho")
    print("  [7] Finalizar compra")
    print("  [0] Sair")
    print("-" * 70)


# =============================================================================
# FUNÇÕES DE FUNCIONALIDADES (Features)
# =============================================================================

def listar_produtos(produtos):
    """
    Lista todos os produtos disponíveis.
    PARADIGMA ESTRUTURADO: Loop FOR itera sobre a lista de produtos
    """
    print("\n" + "="*70)
    print("[PRODUTOS DISPONÍVEIS]")
    print("="*70)
    
    if not produtos:
        print("[AVISO] Nenhum produto cadastrado.")
        return
    
    # Loop FOR: exibe cada produto
    for produto in produtos:
        print(f"\n{produto.exibir_info()}")
    
    print("="*70)


def filtrar_por_categoria_interface(produtos):
    """
    Interface para filtrar produtos por categoria.
    PARADIGMA FUNCIONAL: Usa função filtrar_por_categoria()
    """
    print("\n[FILTRAR POR CATEGORIA]")
    print("  [1] Livros")
    print("  [2] Eletrônicos")
    
    opcao = input("\nEscolha a categoria: ").strip()
    
    # Condicional IF/ELIF: determina categoria
    if opcao == '1':
        # PARADIGMA FUNCIONAL: usa função filter
        filtrados = filtrar_por_categoria(produtos, 'livro')
        print("\n[CATEGORIA: LIVROS]")
    elif opcao == '2':
        # PARADIGMA FUNCIONAL: usa função filter
        filtrados = filtrar_por_categoria(produtos, 'eletronico')
        print("\n[CATEGORIA: ELETRÔNICOS]")
    else:
        print("[ERRO] Opção inválida!")
        return
    
    # Loop FOR: exibe produtos filtrados
    if not filtrados:
        print("[AVISO] Nenhum produto encontrado nesta categoria.")
    else:
        for produto in filtrados:
            print(f"\n{produto.exibir_info()}")


def buscar_produto_por_id(produtos):
    """
    Busca um produto específico pelo ID.
    PARADIGMA ESTRUTURADO: Tratamento de erros com try/except
    """
    try:
        produto_id = int(input("\n[BUSCAR] Digite o ID do produto: "))
        
        # Loop FOR: busca produto
        for produto in produtos:
            if produto.get_id() == produto_id:
                print("\n[PRODUTO ENCONTRADO]")
                print(produto.exibir_info())
                return produto
        
        print("[AVISO] Produto não encontrado!")
        return None
    
    except ValueError:
        print("[ERRO] Digite um número válido!")
        return None


def adicionar_ao_carrinho(cliente, produtos):
    """
    Adiciona produto ao carrinho e DEBITA do estoque.
    INTEGRAÇÃO: OO (carrinho) + Estruturado (loops, condicionais)
    """
    produto = buscar_produto_por_id(produtos)
    
    # Condicional: verifica se produto foi encontrado
    if not produto:
        return
    
    # Condicional: verifica estoque
    if produto.get_estoque() <= 0:
        print("[ERRO] Produto sem estoque!")
        return
    
    try:
        quantidade = int(input(f"Quantidade (disponível: {produto.get_estoque()}): "))
        
        # Condicional: valida quantidade
        if quantidade <= 0:
            print("[ERRO] Quantidade inválida!")
            return
        
        if quantidade > produto.get_estoque():
            print("[ERRO] Estoque insuficiente!")
            return
        
        # DÉBITO NO ESTOQUE - Requisito obrigatório do trabalho
        novo_estoque = produto.get_estoque() - quantidade
        produto.set_estoque(novo_estoque)
        
        # PARADIGMA OO: adiciona ao carrinho
        cliente.get_carrinho().adicionar_item(produto, quantidade)
        
        print(f"[OK] {quantidade}x {produto.get_nome()} adicionado(s) ao carrinho!")
        print(f"[ESTOQUE] Estoque atualizado: {novo_estoque} unidades")
    
    except ValueError:
        print("[ERRO] Digite um número válido!")


def remover_do_carrinho(cliente, produtos):
    """
    Remove produto do carrinho e DEVOLVE ao estoque.
    INTEGRAÇÃO: OO + Estruturado
    """
    carrinho = cliente.get_carrinho()
    itens = carrinho.listar_itens()
    
    # Condicional: verifica se carrinho está vazio
    if not itens:
        print("[AVISO] Carrinho vazio!")
        return
    
    print("\n[ITENS NO CARRINHO]")
    # Loop FOR: lista itens
    for item in itens:
        produto = item['produto']
        print(f"  ID {produto.get_id()}: {produto.get_nome()} (Qtd: {item['quantidade']})")
    
    try:
        produto_id = int(input("\n[REMOVER] Digite o ID do produto a remover: "))
        
        # Loop FOR: busca item no carrinho
        for item in itens:
            if item['produto'].get_id() == produto_id:
                produto = item['produto']
                quantidade = item['quantidade']
                
                # DEVOLVE AO ESTOQUE
                novo_estoque = produto.get_estoque() + quantidade
                produto.set_estoque(novo_estoque)
                
                # Remove do carrinho
                carrinho.remover_item(produto_id)
                
                print(f"[OK] {produto.get_nome()} removido do carrinho!")
                print(f"[ESTOQUE] Estoque devolvido: {novo_estoque} unidades")
                return
        
        print("[AVISO] Produto não encontrado no carrinho!")
    
    except ValueError:
        print("[ERRO] Digite um número válido!")


def exibir_carrinho(cliente):
    """
    Exibe o carrinho com total.
    INTEGRAÇÃO: OO (carrinho) + Funcional (calcular_total)
    """
    carrinho = cliente.get_carrinho()
    itens = carrinho.listar_itens()
    
    print("\n" + "="*70)
    print("[SEU CARRINHO]")
    print("="*70)
    
    # Condicional: verifica se carrinho está vazio
    if not itens:
        print("[AVISO] Carrinho vazio!")
        print("="*70)
        return
    
    # Loop FOR: exibe cada item
    for item in itens:
        produto = item['produto']
        qtd = item['quantidade']
        preco_unit = produto.calcular_preco_final()
        subtotal = preco_unit * qtd
        
        print(f"\n{produto.get_nome()}")
        print(f"  Quantidade: {qtd}x | Preço Unit.: R$ {preco_unit:.2f} | Subtotal: R$ {subtotal:.2f}")
    
    # PARADIGMA FUNCIONAL: calcula total usando reduce
    total = calcular_total_carrinho(itens)
    
    print("-" * 70)
    print(f"[TOTAL] R$ {total:.2f}")
    print("="*70)


def finalizar_compra(cliente, produtos):
    """
    Finaliza a compra com opções de pagamento.
    PARADIGMA ESTRUTURADO - SWITCH/CASE (match/case)
    Requisito obrigatório do paradigma estruturado
    """
    carrinho = cliente.get_carrinho()
    itens = carrinho.listar_itens()
    
    # Condicional: verifica se carrinho está vazio
    if not itens:
        print("[ERRO] Carrinho vazio! Adicione produtos antes de finalizar.")
        return
    
    # Exibe resumo
    exibir_carrinho(cliente)
    
    # PARADIGMA FUNCIONAL: calcula total
    total_geral = calcular_total_carrinho(itens)
    
    print("\n[FORMAS DE PAGAMENTO]")
    print("  [1] À vista (5% de desconto)")
    print("  [2] Parcelado (sem juros)")
    print("  [0] Cancelar")
    
    opcao_pgto = input("\nEscolha a forma de pagamento: ").strip()
    
    # =============================================================================
    # PARADIGMA ESTRUTURADO - SWITCH/CASE (MATCH/CASE)
    # Requisito obrigatório do trabalho
    # =============================================================================
    match opcao_pgto:
        case '1':
            # À vista com desconto
            # PARADIGMA FUNCIONAL: aplica desconto
            valor_final = aplicar_desconto(total_geral, 5)
            desconto = total_geral - valor_final
            
            print("\n" + "="*70)
            print("[COMPRA FINALIZADA - À VISTA]")
            print("="*70)
            print(f"Cliente: {cliente.get_nome()}")
            print(f"Valor Original: R$ {total_geral:.2f}")
            print(f"Desconto (5%%): R$ {desconto:.2f}")
            print(f"[VALOR FINAL] R$ {valor_final:.2f}")
            print("="*70)
            
            # Salva alterações no estoque
            salvar_produtos_no_json(produtos)
            
            # Limpa o carrinho
            carrinho.limpar()
            print("[OK] Compra confirmada! Obrigado pela preferência!")
        
        case '2':
            # Parcelado
            try:
                num_parcelas = int(input("\nNúmero de parcelas (2-12): "))
                
                # Condicional: valida número de parcelas
                if num_parcelas < 2 or num_parcelas > 12:
                    print("[ERRO] Número de parcelas inválido!")
                    return
                
                # PARADIGMA FUNCIONAL: calcula parcelas
                valor_parcela = calcular_parcelas(total_geral, num_parcelas)
                
                print("\n" + "="*70)
                print("[COMPRA FINALIZADA - PARCELADO]")
                print("="*70)
                print(f"Cliente: {cliente.get_nome()}")
                print(f"Valor Total: R$ {total_geral:.2f}")
                print(f"[PARCELAS] {num_parcelas}x de R$ {valor_parcela:.2f} (sem juros)")
                print("="*70)
                
                # Salva alterações no estoque
                salvar_produtos_no_json(produtos)
                
                # Limpa o carrinho
                carrinho.limpar()
                print("[OK] Compra confirmada! Obrigado pela preferência!")
            
            except ValueError:
                print("[ERRO] Digite um número válido!")
        
        case '0':
            print("\n[CANCELADO] Compra cancelada!")
        
        case _:
            # Default case
            print("\n[ERRO] Opção inválida!")


# =============================================================================
# FUNÇÃO PRINCIPAL
# =============================================================================

def main():
    """
    Função principal do programa.
    PARADIGMA ESTRUTURADO: Loop WHILE mantém o programa rodando até usuário sair
    """
    exibir_cabecalho()
    
    # Carrega produtos do JSON
    produtos = carregar_produtos_do_json()
    
    if not produtos:
        print("[ERRO] Não foi possível carregar os produtos!")
        return
    
    # Cadastro do cliente
    print("\n[CADASTRO]")
    nome = input("Nome: ").strip()
    cpf = input("CPF: ").strip()
    
    # PARADIGMA OO: cria objeto Cliente
    cliente = Cliente(nome, cpf)
    
    print(f"\n[BEM-VINDO] Olá, {nome}!")
    
    # =============================================================================
    # PARADIGMA ESTRUTURADO - LOOP WHILE
    # Menu principal repete até usuário escolher sair
    # =============================================================================
    while True:
        exibir_menu()
        opcao = input("Digite sua opção: ").strip()
        
        # =============================================================================
        # PARADIGMA ESTRUTURADO - ESTRUTURA CONDICIONAL IF/ELIF/ELSE
        # =============================================================================
        if opcao == '1':
            listar_produtos(produtos)
        
        elif opcao == '2':
            filtrar_por_categoria_interface(produtos)
        
        elif opcao == '3':
            buscar_produto_por_id(produtos)
        
        elif opcao == '4':
            exibir_carrinho(cliente)
        
        elif opcao == '5':
            adicionar_ao_carrinho(cliente, produtos)
        
        elif opcao == '6':
            remover_do_carrinho(cliente, produtos)
        
        elif opcao == '7':
            finalizar_compra(cliente, produtos)
        
        elif opcao == '0':
            # Salva alterações antes de sair
            salvar_produtos_no_json(produtos)
            print("\n[FINALIZADO] Obrigado por usar nossa loja! Até logo!")
            break  # Sai do loop WHILE
        
        else:
            print("\n[ERRO] Opção inválida! Tente novamente.")


# =============================================================================
# PONTO DE ENTRADA
# =============================================================================

if __name__ == "__main__":
    main()
