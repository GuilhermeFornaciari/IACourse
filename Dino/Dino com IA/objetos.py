import pygame
import random
import os

VELOCIDADE = 10
TELA_LARGURA = 800
TELA_ALTURA = 300
branco = 255,255,255 #Valor RGB do branco
preto  = 0,0,0


pygame.font.init()
FONTE = pygame.font.SysFont('VT323', 35)


def desenhar_tela(tela,dinos,cactos,chaojogo,pontuacao):
    tela.fill(branco)
    for i,dino in enumerate(dinos):
        dino.desenhar(tela)
    for cac in cactos:
        cac.desenhar(tela)
    chaojogo.desenhar(tela)
    
    ponto = FONTE.render(f"Pontuação: {round(pontuacao)}", 1 ,preto)
    tela.blit(ponto,(TELA_LARGURA - ponto.get_width(), 30))
    pygame.display.update()



def detectaEvento(dinos):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

    return True



class Chao:
    IMAGEM = pygame.image.load(os.path.join('imagens/', 'chao.png'))
    LARGURA = IMAGEM.get_width()
    
    Y = TELA_ALTURA - 40
    def __init__(self) -> None:
        self.x1 = 0
        self.x2 = self.LARGURA

    def mover(self):
        self.x1 -= VELOCIDADE
        self.x2 -= VELOCIDADE
        #Reseta a posição do chao
        if self.x1 <= -self.LARGURA:
            self.x1 = self.LARGURA
        if self.x2 <= -self.LARGURA:
            self.x2 = self.LARGURA

    def desenhar(self,tela):
        tela.blit(self.IMAGEM,(self.x1,self.Y))
        tela.blit(self.IMAGEM,(self.x2,self.Y))



class Dino:
    IMAGENS = [
        pygame.image.load(os.path.join('imagens/dino', 'dino_1.png')),
        pygame.image.load(os.path.join('imagens/dino', 'dino_2.png')),
        pygame.image.load(os.path.join('imagens/dino', 'dinoMorto.png'))
    ]
    
    POS_INICIAL = TELA_ALTURA - 100
    def __init__(self) -> None:
        self.x = 50
        self.y = self.POS_INICIAL
        self.animacao = 0
        self.tempo = 0
        self.aceleracao = 0.0
        self.vivo = True
        self.pulou = False
        self.interagiu_cacto = False
    
    def apagar(self,):
        if self.x <= -self.IMAGENS[0].get_width():
            return True
        else:
            return False
    def desenhar(self,tela):
        if self.vivo:
            self.tempo +=1
            if self.tempo > 12:
                self.tempo = 0
                if self.animacao == 0:
                    self.animacao = 1
                else:
                    self.animacao = 0
        else:
            self.animacao = 2
                

        tela.blit(self.IMAGENS[self.animacao],(self.x,self.y))
    def mover(self):

        if not self.vivo:
            self.x -= VELOCIDADE
            return
        self.y += self.aceleracao

        if self.y < self.POS_INICIAL: 
            self.aceleracao += 0.8
        if self.y > self.POS_INICIAL:
            self.aceleracao = 0
            self.y = self.POS_INICIAL
            self.pulou = False
         
            
    def pular(self):
        if not self.pulou and self.y == self.POS_INICIAL:
            self.aceleracao = -14.0
            self.pulou = True
            return 30
        return 0

    def getmask(self):
        return pygame.mask.from_surface(self.IMAGENS[0])
    

class cacto: 
    IMAGEM = [
        pygame.image.load(os.path.join('imagens/cacto', 'cacto_1.png')),
        pygame.image.load(os.path.join('imagens/cacto', 'cacto_2.png')),
        pygame.image.load(os.path.join('imagens/cacto', 'cacto_3.png')),
        pygame.image.load(os.path.join('imagens/cacto', 'cacto_4.png')),
        pygame.image.load(os.path.join('imagens/cacto', 'cacto_5.png')),
        pygame.image.load(os.path.join('imagens/cacto', 'cacto_6.png'))
    ]
    def __init__(self,x,tipocacto) -> None:
        if x == None:
            self.x = random.randrange(TELA_LARGURA,TELA_LARGURA+200)
        else:
            self.x = x

        if tipocacto == None:
            self.tipocacto = random.randrange(0,5)
        else:
            self.tipocacto = tipocacto
        self.img = self.IMAGEM[self.tipocacto]
        self.y = TELA_ALTURA - self.img.get_height() - 10
    def apagar(self):
        if self.x < 2 * -self.img.get_width():
            return True
        else:
            return False
    
    def mover(self):
        self.x -= VELOCIDADE

    def colisao(self,dino):
        maskDino = dino.getmask()
        maskCacto = pygame.mask.from_surface(self.img)

        distancia = abs(self.x - dino.x), abs(self.y - dino.y)
        contato = maskCacto.overlap(maskDino,distancia)
        return contato
    def desenhar(self,tela):
        tela.blit(self.img,(self.x,self.y))
        


        
        
        
        

        
        
                

        
    

