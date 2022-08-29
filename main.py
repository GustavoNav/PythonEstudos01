#funcao para imprimir a situacao na forca
def forca_imprimi(n):
    estados = ["""
       |--------|
       |        |
                |
                |
                |        
                |
                |
    """, """
       |--------|
       |        |
       O        |
                |
                |        
                |
                |
    """, """
       |--------|
       |        |
       O        |
       |        |
                |        
                |
                |
    """, """
       |--------|
       |        |
       O        |
      /|        |
       |        |        
                |
                |
    """, """
       |--------|
       |        |
       O        |
      /|\       |
       |        |        
                |
                |
    """, """
       |--------|
       |        |
       O        |
      /|\       |
       |        |        
      /         |
                |
    """, """
       |--------|
       |        |
       O        |
      /|\       |
       |        |        
      / \       |
                |
    """]
    print(estados[n.tentativas])


# funcao para salvar as palavras do arquivo palavras.txt
def listar():
    lista_palavras = []
    with open("palavras.txt", "r") as arquivo:
        for row in arquivo:
            lista_palavras.append(row.split("\n")[0])
        return lista_palavras


# funcao para imprimir a situacao da palavra e devolver se a pálavra foi concluida
def rep(n):
    situa = ""
    x = True
    for c in n.nome_palavra:
        if c not in n.descoberta:
            situa += "_ "
            x = False
        else:
            situa += c + " "
    return situa, x


# classe do jogo, contendo a palavra, a lista de letras que o usario descobriu e as tentativas restantes
class forca:
    tentativas = 0
    descoberta = []

    def __init__(self, nome_palavra):
        self.nome_palavra = nome_palavra


# no inicio é utilizada a funcao listar() para salvar as palavras do arquivo em uma lista
lista_p = listar()

for p in lista_p:
    # criando o objeto j_atual apartir da classe forca, em seguida realizada a limpeza da lista de descobertas da classe
    j_atual = forca(p)
    j_atual.descoberta = []

    # estrutura de repeticao com a interecao com o usuario
    while True:
        print("/\ Situação atual:\t", rep(j_atual)[0])
        print("/\ Tentativas:\t", j_atual.tentativas)
        forca_imprimi(j_atual)

        entrada = str(input("/\ Digite uma letra: ")).lower()
        if entrada in j_atual.descoberta:
            print("\nVocê já usou essa! tente outra letra!")

        elif entrada in j_atual.nome_palavra:
            print("CORRETO")
            j_atual.descoberta.append(entrada)

        else:
            print("\nX ERRADO X\n")
            j_atual.tentativas += 1

        if j_atual.tentativas == 7:
            print("\nX X X VOCÊ PERDEU X X X\n")
            break

        if rep(j_atual)[1]:
            print("\n> > > VOCÊ GANHOU < < <")
            print("A palavra é:\t", rep(j_atual)[0])
            print("\n\n")
            break
