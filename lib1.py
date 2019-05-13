import pygame
import math
ANCHO = 640
ALTO = 480
#================   Colores RGB    ============
NEGRO = [0,0,0]
BLANCO = [255,255,255]
ROJO = [255,0,0]
VERDE = [0,255,0]
AZUL = [0,0,255]
AMARILLO = [255,255,0]
CIAN = [0,255,255]
MAGENTA = [255,0,255]
def polar(amplitud,petalos,angulo):
    '''
    radio=seno()
    '''
    p=math.radians(angulo)
    r=(amplitud*(math.cos(petalos*p)))

    return [r,p]
#===============================================================
def rotapoligono(puntos, angulo):
	rad = math.radians(angulo)
	tl=[]
	for punto in puntos:
		x=int(punto[0]*math.cos(rad)-punto[1]*math.sin(rad))
		y=int(punto[0]*math.sin(rad)+punto[1]*math.cos(rad))
		tl.append(transformada(x,y))
	pygame.draw.polygon(pantalla, VERDE, tl, 1)
#==========================================================
def polar_cart(r,a):
    x=int(r*math.cos(a))
    y=int(r*math.sin(a))
    return [x,y]
# =========================================================
def radio(pf,pm,r):
    '''
    cercania entre puntos
    pf:punto fijo
    pm: punto movil
    r: radio de cercania
    retorna verdadero si esta en el radio falso caso contrario
    '''
    xi=pf[0]-r
    xs=pf[0]+r
    if(pm[0]>=xi) and (pm[0]<=xs):
        return True
    return False
#=================================================================

def trasladar(pto,t):
    xp=pto[0]+traslado[0]
    yp=pto[1]+traslado[1]
    return [xp,yp]
#============== matriz de escalamiento ===========================
'''
    recibe un punto y un par de valores de escalamiento correspondiente a las
    coordenadas
'''
def escalamiento(pto,val):
    xs=pto[0]*val[0]
    ys=pto[1]*val[1]
    return [xs,ys]
#=========== Yeisson: rotacion antihoraria =====================================
def rah(pto,angulo):
    #print "conversion grados centigrados a radianes", math.radians(angulo)
    #print "conversion radianes a centigrados", math.degrees(math.pi/2)
    angulo = math.radians(angulo)
    xp = int(pto[0] * math.cos(angulo) - pto[1] * math.sin(angulo))
    yp = int(pto[0] * math.sin(angulo) + pto[1] * math.cos(angulo))
    print "coorX: ", xp , ",coorY:", yp
    return [xp,yp]

def rh(pto,angulo):
    angulo = math.radians(angulo)
    xp=int((-1)*(pto[0]*math.cos(angulo))+pto[1]*math.sin(angulo))
    yp=int(pto[0]*math.sin(angulo)+ pto[1]*math.cos(angulo))
    return [xp,yp]

#=======================================================
'''
    Dado el centro c y un punto p
    Dibuja la linea vertical y  horizontal del plano cartesiano teniendo en
    cuenta el centro asignado.
'''
def plano_cartesiano(c,p):
    # dibuja la linea vertical del plano cartesiano
    pygame.draw.line(p,BLANCO,[c[0],0],[c[0],ALTO])
    # dibuja la linea horizontal del plano cartesiano
    pygame.draw.line(p,BLANCO,[0,c[1]],[ANCHO,c[1]])
#======================================================
def cart_pantalla(c,p):
    xp=p[0]+c[0]
    yp=-p[1]+c[1]
    np=[xp,yp]
    return np
#====== funcion: recibe el centro de coordenadas y pto en pantalla,
# retorna pto el punto en coordenadas cartesianas
def pant_cartesiano(c,p):
    xp = p[0]-c[0]
    yp = c[1]-p[1]
    return [xp,yp]

#=====================================================
def sumv1v2(p,c,pv1,pv2):
    cxv1 = pv1[0]
    cxv2 = pv2[0]
    cyv1 = pv1[1]
    cyv2 = pv2[1]
    cxnv = cxv1 + cxv2
    cynv = cyv1 + cyv2
    trazar_vector(p,c,pv1)
    trazar_vector(p,c,pv2)
    pv1 = cart_pantalla(c,pv1)
    print "el punto es:", pv1 ,"corx: " ,cxnv
    pv2 = cart_pantalla(c,pv2)
    print "el punto es:", pv2 ,"cory: " ,cynv
    prs = [cxnv,cynv]
    print "el punto del nuevo vector en pantalla es:",cart_pantalla(c,prs)
    pygame.draw.line(p,VERDE,c,cart_pantalla(c,prs))
    return prs
#=====================================================
def trazar_vector(pantalla,c,p,color):
    pygame.draw.line(pantalla,color,cart_pantalla(c,[0,0]),cart_pantalla(c,p))
#=====================================================
def triangulo_cartesiano(p,c,clr,p1,p2,p3):
    pygame.draw.line(p,clr,cart_pantalla(c,p1),cart_pantalla(c,p2))
    pygame.draw.line(p,clr,cart_pantalla(c,p1),cart_pantalla(c,p3))
    pygame.draw.line(p,clr,cart_pantalla(c,p2),cart_pantalla(c,p3))
def triangulo(p,c,clr,p1,p2,p3):
    pygame.draw.line(p,clr,p1,p2)
    pygame.draw.line(p,clr,p1,p3)
    pygame.draw.line(p,clr,p2,p3)
#=====================================================
def escal(es,p):
    np=[]
    for e in p:
        v=e*es
        np.append(v)
    return np


def Punto(pantalla, color, punto):
    pygame.draw.circle(pantalla, VERDE,[punto[0], punto[1]], 2)
def Neg(Punto):
	return [-Punto[0],-Punto[1]]
#==============================================================
def Pitagorico(Nlados, Magnitud):
	Angulo = 0;
	R=[]
	for i in range(Nlados):
		punto = (Magnitud*math.cos(Angulo), Magnitud*math.sin(Angulo))
		R.append(punto)
		Angulo += math.radians(360/Nlados)
	return R

def cardioide(a):
	R = []
	for i in range(-1,360):
		r = a*(1+math.cos(math.radians(i)))
		p = (r*math.cos(math.radians(i)), r*math.sin(math.radians(i)))
		R.append(p)
	return R
'''
def radio(angulo):
    angulo= math.radians(angulo)
    r= 1 + math.cos(angulo)
    return r
'''
#============ rotacion horaria version profe ===============
def RH(pto,angulo):
    ang = math.radians(angulo)
    xp=int(pto[0]*math.cos(ang)) - int(pto[1]*math.sin(ang))
    yp=int(-1* (pto[0]*math.sin(ang))) + int(pto[1]*math.cos(ang))
    return [xp,yp]
