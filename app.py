# Faça um programa completo utilizando classes e métodos que: Possua uma classe chamada bombaCombustível, 
# com no mínimo esses atributos:
# i.tipoCombustivel.
# ii.valorLitro
# iii.quantidadeCombustivel

# Possua no mínimo esses métodos:
# i.abastecerPorValor( )
# método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no 
# veículo
# ii.abastecerPorLitro( )
# método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
# iii. alterarValor( )
# altera o valor do litro do combustível.
# iv. alterarCombustivel( )
# altera o tipo do combustível.
# v.  alterarQuantidadeCombustivel( )
# altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na 
# bomba

# Criando a classe BombaCombustivel
class BombaCombustivel: # Método
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel): # Atributos
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor): # Método
        quantidade_de_litros = valor / self.valorLitro
        if quantidade_de_litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= quantidade_de_litros
            print(f'Foram abastecidos {quantidade_de_litros:.2f} litros de {self.tipoCombustivel}.')
        else:
            print('A bomba não tem combustível suficiente')

    def abastecerPorLitro(self, litros): # Método
        valor_a_pagar = litros * self.valorLitro
        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            print(f'O valor a pagar é de R${valor_a_pagar:.2f} reais de {self.tipoCombustivel}.')
        else:
            print('A bomba não tem combustível suficiente')

    def alterarValor(self, novoValor): # Método
        self.valorLitro = novoValor

    def alterarTipoCombustivel(self, novoCombustivel): # Método
        self.tipoCombustivel = novoCombustivel

    def alterarQuantidadeCombustivel(self, novaQuantidade): # Método
        self.quantidadeCombustivel = novaQuantidade

# Exemplo de uso
bomba_posto = BombaCombustivel('Gasolina', 4.88, 10000)

print('Abastaça 100 reais de gasolina')
bomba_posto.abastecerPorValor(100) # Abastecendo 100 reais de combustível

print('Abasteça 20 litros de gasolina')
bomba_posto.abastecerPorLitro(20) # Abastecendo 20 litros de combustível

print('Aumente o valor do litro')
bomba_posto.alterarValor(5.10) # aumentando o valor para R$ 5.10

print('Abasteça em energia')
bomba_posto.alterarTipoCombustivel('Energia')

print('Aumentando a capacidade de combustível na bomba do posto')
bomba_posto.alterarQuantidadeCombustivel(20000)