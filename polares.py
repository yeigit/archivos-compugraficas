import pygame
from lib1 import*
#import sys
import math
#ANCHO=500
#ALTO=500
O=[ANCHO/2,ALTO/2]#Define el centro de ejes coordenados
A=[100,50]
B=[200,0]
C=[200,100]
reloj=pygame.time.Clock()
amp=200
print "ANCHO:",ANCHO
print "ANCHO:",ALTO
print "centro en x:",O[0]
print "centro en y:",O[1]
#from lib1 import* NOTA:el orden de la instruccion influye en las variables
# que se declaran en antes de este import
def Punto(p,r=1):
    pygame.draw.circle(pantalla,BLANCO,p,r)
def plano():
        pygame.draw.line(pantalla,ROJO,[O[0],0],[O[0],ALTO])
        pygame.draw.line(pantalla,ROJO,[0,O[1]],[ANCHO,O[1]])
def cart(p):
    '''
    p[x,y]:p[0]=x p[1]=1
    '''
    xp=O[1]+p[0]
    yp=O[0]-p[1]
    return [xp,yp]

def trian(E,F,D):
    pygame.draw.polygon(pantalla,ROJO,[E,F,D],1)

def rotapoligono(puntos, angulo):
	rad = math.radians(angulo)
	tl=[]
	for punto in puntos:
		x=int(punto[0]*math.cos(rad)-punto[1]*math.sin(rad))
		y=int(punto[0]*math.sin(rad)+punto[1]*math.cos(rad))
		tl.append(transformada(x,y))
	pygame.draw.polygon(pantalla, VERDE, tl, 1)

def transformada(tx,ty):
	punto_x = x+ANCHO/2+tx
	punto_y =y+ALTO/2-ty
	return (punto_x,punto_y)


def sPoligono(puntos, s):
    	tl=[]
    	for pto in puntos:
    		x = pto[0]*s[0]
    		y = pto[1]*s[1]
    		tl.append(transformada(x,y))
    	return tl

def circu(r,a):
    p=math.radians(a)
    x=int(r*math.cos(p))

    return x

def polarac(r,a):
    x=int(r*math.cos(a))
    y=int(r*math.sin(a))
    return [x,y]

def polar(amplitud,petalos,angulo):
    '''
    radio=seno()
    '''
    p=math.radians(angulo)
    r=(amplitud*(math.cos(petalos*p)))

    return [r,p]

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    plano()
    an=0
    pygame.display.flip()

    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:

                    amp-=10
                    an=0
                    pantalla.fill(NEGRO)
                if event.button == 5:
                    amp+=10
                    an=0
                    pantalla.fill(NEGRO)

        plano()
        if an <= 600:
            cor=polar(amp,2,an)
            p=cart(polar_cart(cor[0],cor[1]))
            an+=1
            pygame.draw.circle(pantalla,CIAN,p,2)
            pygame.display.flip()
            reloj.tick(60)
