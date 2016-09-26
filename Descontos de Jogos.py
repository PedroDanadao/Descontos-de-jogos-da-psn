from urllib.request import urlopen
from urllib.request import Request
from collections import OrderedDict


def main():
    print("---------------------------------------------")
    #cria um dicionario para armazenar o nome do jogo e seu link
    links = {}

    #sempre que quiser adicionar um jogo você vai seguir o seguinte modelo
    #links["nome do jogo"] = "link do jogo"(no psprices.com, e tem que ser na versão br)

    #Overwatch
    links["Overwatch"] = "https://psprices.com/region-br/game/191580/overwatch-origins-edition"
    #Horizon zero Dawn
    links["Horizon"] = "https://psprices.com/region-br/game/256271/horizon-zero-dawn"
    #The last Guardian
    links["The Last Guardian"] = "https://psprices.com/region-br/game/257623/the-last-guardian"
    #Ratchet and Clanck
    links["Ratchet and Clanck"] = "https://psprices.com/region-br/game/100525/ratchet-and-clanktm"
    #Trackmania Turbo
    links["Trackmania Turbo"] = "https://psprices.com/region-br/game/217465/trackmania-turbo"
    #Firewatch
    links["Firewatch"] = "https://psprices.com/region-br/game/151026/firewatch"
    #Bioshock Collection
    links["Bioshock Collection"] = "https://psprices.com/region-br/game/834037/bioshock-the-collection"
    #Valkyria Chronicles
    links["Valkyria Chronicles"] = "https://psprices.com/region-br/game/254597/valkyria-chronicles-remastered"
    #Gravity Rush Remaster
    links["Gravity Rush Remaster"] = "https://psprices.com/region-br/game/119539/gravity-rushtm-remastered"
    #Fallout 4
    links["Fallout 4"] = "https://psprices.com/region-br/game/116287/fallout-4-digital-deluxe-bundle"
    #Odin Sphere
    links["Odin Sphere"] = "https://psprices.com/region-br/game/256507/odin-sphere-leifthrasir"
    #The Witness
    links["The Witness"] = "https://psprices.com/region-br/game/126482/the-witness"
    
    #cria um novo dicionario com os jogos em ordem alfabetica
    links_o = OrderedDict(sorted(links.items()))

    #laço que cria um 'contador'(link) que vai receber os links do dicionario organizado
    for nome, link in links_o.items():
        site = Site(link)
        site.toString()
    
    print("---------------------------------------------")
    input("Tecle enter para encerrar ")


#Classe que recebe a url de uma página de um jogo no psprices.com, e verifica se tal jogo
#tem desconto
class Site:
    def __init__(self, url):
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        self.url = url
        #cria uma string do codigo fonte
        self.sourceCode = str(urlopen(req).read())
        self.precoAntigo = ''
        self.precoAtual = ''

    #verifica o antigo preco do jogo CASO ele tenha desconto
    def getPrecoAntigo(self):
        if '<span class="content__game_card__price_drop__val">R$' in self.sourceCode:
            #pega o que estiver entre '<span class="content__game_card__price_drop__val">R$' e '</span></span>'
            self.precoAntigo = self.sourceCode.split('<span class="content__game_card__price_drop__val">R$')[1]
            self.precoAntigo = self.precoAntigo.split('</span></span>')[0]

    #verifica o preco atual do jogo, independente dele ter tido desconto ou nao
    #caso o jogo tenha desconto na psn plus, o atributo(string): precoAtual terá um '+' à sua direita
    def getPrecoAtual(self):
        if 'content__game_card__price_plus_ico">&nbsp;</span>' in self.sourceCode:
            self.precoAtual = self.sourceCode.split('<span class="content__game_card__price_plus_ico">&nbsp;</span> ')[1]
            self.precoAtual = self.precoAtual.split('</span>')[0] + ' +'
        else:    
            self.precoAtual = self.sourceCode.split('<span class="content__game_card__price" itemprop="price" content="')[1]
            self.precoAtual = self.precoAtual.split('">')[0]

    #informa ao usuário, o preco antigo(caso tenha) e o preco atual do jogo
    def toString(self):
        print("#############################################")
        print('    ' + self.url.split('/')[-1] + '\n') #imprime tudo oque vem depois do último '/' no link
        
        self.getPrecoAtual()
        self.getPrecoAntigo()
        
        if(self.precoAntigo != ''):
            print('preço antigo: ' + self.precoAntigo)
        print('preço atual: ' + self.precoAtual + '\n')
        
		
main() #chama a função main
