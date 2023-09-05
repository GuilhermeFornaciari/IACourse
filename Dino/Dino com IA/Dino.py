from objetos import *
import neat
TELA_LARGURA = 800
TELA_ALTURA = 300

preto  = 0,0,0

def mover_tela(chaojogo,cactos,dinos,lista_genomas,redes):
    chaojogo.mover()

    for i,dino in enumerate(dinos):
        
        dino.mover()
        if cactos[0].colisao(dino): 
            dino.vivo = False  
            if not dino.interagiu_cacto: #
                #Bot professor que testa os bots criados
                if dino.y == dino.POS_INICIAL:
                    lista_genomas[i].fitness -= 100 

                dino.interagiu_cacto = True
        #Bot professor que testa os bots criados
        if cactos[0].x < dino.x - dino.IMAGENS[0].get_width() and not dino.interagiu_cacto:
            dino.interagiu_cacto = True
            lista_genomas[i].fitness += 30

        if dino.apagar():
            dinos.pop(i)
            lista_genomas.pop(i)
            redes.pop(i)
        

            

    for cac in cactos:
        cac.mover()
        if cac.apagar():
            cactos.pop()
            for dino in dinos:
                dino.interagiu_cacto = False



def rodar(genomas, config):
    pontuacao = 0
    #Configura a tela
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA)) 
    # Cria os elementos do jogo
    dinos = []
    cactos = [cacto(900,3)]
    chaojogo = Chao()
    relogio = pygame.time.Clock()
    redes = []
    lista_genomas = []
    dinos = []
        
    #Bot de criação de bots
    for _,genoma in genomas:
        rede = neat.nn.FeedForwardNetwork.create(genoma,config)
        redes.append(rede)
        genoma.fitness = 0
        lista_genomas.append(genoma)
        dinos.append(Dino())
        

    while len(dinos) != 0:
        pontuacao += .5
        relogio.tick(60)
        #Comando para sair do pygame se for nescessário
        detectaEvento(dinos)
        if len(cactos) == 0:
            cactos.append(cacto(None,None)) 

        #integração do jogo com a tomada de decisão da IA 1 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        print("\n"*30)
        for i,dino in enumerate(dinos):
            print(i+1,lista_genomas[i].fitness)

            lista_genomas[i].fitness += 0.5
            output = redes[i].activate((
                                            cactos[0].img.get_height(),
                                            abs(cactos[0].x - dino.x),
                                            VELOCIDADE
                                          ))
                
            #-1 a 1, se > 0.5: pular
            if output[0] > 0.0:
                lista_genomas[i].fitness -= dino.pular() 
            output = None
        
        

        #Define uma Lista com o cacto, e o dino que serão usados no futuro

        

        mover_tela(chaojogo,cactos,dinos,lista_genomas,redes)
        desenhar_tela(tela,dinos,cactos,chaojogo,pontuacao)



def main():
    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,
                                'config.txt'
                                )
    populacao = neat.Population(config)
    populacao.run(rodar)
    

main()