from gerenciarLivros import GerenciarLivros

if __name__ == '__main__':
   gerLivros = GerenciarLivros()

   titulo = 'aaaaaa'
   autor='aaaaaaaasdafsafdsa'
   anoPublicacao = 2000
   preco=12.3

   gerLivros.criar(titulo, autor, anoPublicacao, preco)

   titulo = 'bbbbbb'
   autor = 'aaaaabvcbcvbrghrfgaaasdafsafdsa'
   anoPublicacao = 20021
   preco = 12.3

   gerLivros.criar(titulo, autor, anoPublicacao, preco)

   gerLivros.mostrar()

   print(gerLivros.buscar('aaaaa'))

