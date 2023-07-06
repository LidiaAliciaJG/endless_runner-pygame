#IMPORTACIÓN DE PAQUETES
import pygame
import sys

#INICIALIZANCIÓN DE PYGAME
pygame.init()

#CREACIÓN DE LA PANTALLA
sc_ancho, sc_alto = 1000, 600
screen = pygame.display.set_mode((sc_ancho, sc_alto))
pygame.display.set_caption('Juego por Lidia Alicia JG')

icono=pygame.image.load('imagenes/icono.png')
pygame.display.set_icon(icono)
#Referencia de icono <a target="_blank" href="https://icons8.com/icon/46980/game-boy-visual">juego</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>

fondo = pygame.image.load('imagenes/fondootonio-modificado.jpg').convert()
#Referencia de imagen <a href="https://www.freepik.es/vector-gratis/fondo-fondo-otono_1165702.htm#query=fondos%20de%20videojuegos&position=6&from_view=keyword&track=ais">Imagen de alekksall</a> en Freepik


#ANIMACIÓN DEL PERSONAJE
#imágenes propias creadas en piskel con una base
quieto = pygame.image.load('imagenes/sprite_chica00.png')

caminaDerecha = [pygame.image.load('imagenes/sprite_chica04.png'),
				pygame.image.load('imagenes/sprite_chica05.png'),
				pygame.image.load('imagenes/sprite_chica06.png'),
				pygame.image.load('imagenes/sprite_chica07.png')]

caminaIzquierda = [pygame.image.load('imagenes/sprite_chica12.png'),
				pygame.image.load('imagenes/sprite_chica13.png'),
				pygame.image.load('imagenes/sprite_chica14.png'),
				pygame.image.load('imagenes/sprite_chica15.png')]

salta = [pygame.image.load('imagenes/sprite_chica01.png')] #sprite_chica05.png

#Variables
x = 0
px = 50 #posición en x del personaje
py = 345 #posición en y del personaje
ancho = 40
velocidad = 10 #del personaje

#Control de FPS
reloj = pygame.time.Clock()
FPS = 18

#Variables salto
salto = False
#Contador de salto
cuentaSalto = 10

#Variables de dirección
izquierda = False
derecha = False

#Pasos
cuentaPasos = 0

#MOVIMIENTO DEL PERSONAJE Y FONDO
def recarga_pantalla():
	# Variables globales
	global cuentaPasos
	global x

	#MOVIMIENTO DEL FONDO EN X
	x_relativa = x % fondo.get_rect().width
	screen.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
	if x_relativa < sc_ancho:
		screen.blit(fondo, (x_relativa, 0))
	x -= 3
	
	#Contador de pasos
	if cuentaPasos + 1 >= 4:
		cuentaPasos = 0
		
	#MOVIMIENTO DEL PERSONAJE
	#Movimiento a la izquierda
	if izquierda:
		screen.blit(caminaIzquierda[cuentaPasos // 1], (int(px), int(py)))
		cuentaPasos += 1

	#Movimiento a la derecha
	elif derecha:
		screen.blit(caminaDerecha[cuentaPasos // 1], (int(px), int(py)))
		cuentaPasos += 1

    #Movimiento en salto
	elif salto + 1 >= 2:
		screen.blit(salta[cuentaPasos // 1], (int(px), int(py)))
		cuentaPasos += 1
		
    #Sin movimiento
	else:
		screen.blit(quieto,(int(px), int(py)))

ejecuta = True

#BUCLE DE EJECUCIÓN
while ejecuta:
	#Control de FPS
	reloj.tick(FPS)

	#Bucle del juego
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			ejecuta = False

	#Opción de tecla pulsada
	keys = pygame.key.get_pressed()

	#Movimiento a la izquierda: Tecla A
	if keys[pygame.K_a] and px > velocidad:
		px -= velocidad
		izquierda = True
		derecha = False

	#Movimiento a la derecha: Tecla D
	elif keys[pygame.K_d] and px < 970 - velocidad - ancho:
		px += velocidad
		izquierda = False
		derecha = True

	#Sin movimiento
	else:
		izquierda = False
		derecha = False
		cuentaPasos = 0

	#Salto: Tecla Espacio
	if not salto:
		if keys[pygame.K_SPACE]:
			salto = True
			izquierda = False
			derecha = False
			cuentaPasos = 0
	else:
		if cuentaSalto >= -10:
			py -= (cuentaSalto * abs(cuentaSalto)) * 0.5
			cuentaSalto -= 1
		else:
			cuentaSalto = 10
			salto = False

	#ACTUALIZACIÓN DE VENTANA
	pygame.display.update()
	#Llamada a la función creada
	recarga_pantalla()

#CIERRE DEL JUEGO
pygame.quit()
sys.exit()
