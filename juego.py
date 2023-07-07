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

#MÚSICA DE FONDO
pygame.mixer.music.load('sonido/A_Dogs_Life-FiftySounds.mp3') 
pygame.mixer.music.play(-1) 
#pygame.mixer.music.set_volume(0.5)
#Referencia de canción: Obra: La Vida de un Perro / Música de https://www.fiftysounds.com/es/

#IMAGENES PARA VOLUMEN DE SONIDO
sonido_subir = pygame.image.load('sonido/medio.png')
sonido_bajar = pygame.image.load('sonido/bajo.png')
sonido_mute = pygame.image.load('sonido/mute.png')
sonido_max = pygame.image.load('sonido/alto.png')
#Referencia de íconos: <a target="_blank" href="https://icons8.com/icon/46657/volumen-bajo">Volumen bajo</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>


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

	#VOLUMEN DE MUSICA
	#Bajar volumen: tecla 9
	if keys[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0: 
		pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01) 
		screen.blit(sonido_bajar, (850, 25)) 
	elif keys[pygame.K_9] and pygame.mixer.music.get_volume() == 0.0:
		screen.blit(sonido_mute, (850, 25))

	#Subir volumen
	if keys[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0: 
		pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
		screen.blit(sonido_subir, (850, 25))
	elif keys [pygame.K_0] and pygame.mixer.music.get_volume() == 1.0:
			screen.blit(sonido_max, (850, 25)) 

	#Mutear sonido
	elif keys[pygame.K_m]:
		pygame.mixer.music.set_volume(0.0) 
		screen.blit(sonido_mute, (850, 25))

	#Reactivar sonido en maximo
	elif keys[pygame.K_COMMA]:
		pygame.mixer.music.set_volume(1.0)
		screen.blit(sonido_max, (850, 25))

	#MOVIMIENTO DEL PERSONAJE
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
	#Llamada a la función de actualización de la ventana
	recarga_pantalla()

#CIERRE DEL JUEGO
pygame.quit()
sys.exit()
