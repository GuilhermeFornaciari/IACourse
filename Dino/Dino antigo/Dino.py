from objetos import *

TELA_LARGURA = 800
TELA_ALTURA = 300
preto  = 0,0,0


def mover_tela(chaojogo,cactos,dinos):
    chaojogo.mover()
    for i,dino in enumerate(dinos):
        dino.mover()
        if cactos[0].colisao(dino): #Detecta se o dino bateu no cacto
            dino.vivo = False  #Para todos os dinos que encostaram no cacto

        if dino.apagar():
            dinos.pop(i)
        

            

    for cac in cactos:
        cac.mover()
        if cac.apagar():
            cactos.pop()

def rodar():
    pontuacao = 0
    #Configura a tela
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA)) 
    
    # Cria os elementos do jogo
    cactos = [cacto(900,3)]
    chaojogo = Chao()
    relogio = pygame.time.Clock()


    dinos = [Dino()]
    while len(dinos) != 0:
        pontuacao += .5
        relogio.tick(60)
        #Comando para sair do pygame se for nescessário
        detectaEvento(dinos)
        if len(cactos) == 0:
            cactos.append(cacto(None,None)) 

        mover_tela(chaojogo,cactos,dinos)
        desenhar_tela(tela,dinos,cactos,chaojogo,pontuacao)

    roda = True
    resetMensagem = FONTE.render("Pressione espaço para jogar novamente", 1, preto)
    tela.blit(resetMensagem,(TELA_LARGURA/2 - resetMensagem.get_width()/2,100))
    pygame.display.update()
    while roda:
        roda = detectaEvento([Dino()])
            

def main():
    geracao = 1
    while True:
        rodar()

main()