import pygame, random
pygame.init()

size = (800, 500)
color_fondo = (100, 200, 255)

# Colores
negro = (0, 0, 0)
blanco = (255, 255, 255)
verde = (0, 255, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)
#Ventana desplegable
ventana = pygame.display.set_mode(size)
#Titulo juego
pygame.display.set_caption("Penalty Shootout")

#FPS
reloj = pygame.time.Clock()
#Bucle central
pygame.mouse.set_visible(0)
fondo = pygame.image.load("background.png").convert()
fondo.set_colorkey([0, 0, 0])
portero = pygame.image.load("Ochoa.png").convert()
portero.set_colorkey([255, 0, 0])
publico = pygame.image.load("crowd.jpg").convert()
balon = pygame.image.load("balon.png").convert()
balon.set_colorkey([255, 0, 0])
balon_pos = [370, 410]
target_pos = [370, 410]
velocidad = 0.3
velocidad_portero = 5
portero_pos = [330, 120]
movimiento_realizado = False
direccion_movimiento = None
tiempo_movimiento = 0
    
def actualizar_portero():
    global direccion_movimiento, tiempo_movimiento
    # Actualiza la posición del portero de manera aleatoria
    if direccion_movimiento == 'izquierda':
        portero_pos[0] = max(portero_pos[0] - velocidad_portero, 0)
    elif direccion_movimiento == 'derecha':
        portero_pos[0] = min(portero_pos[0] + velocidad_portero, size[0] - portero.get_width())
        
    if pygame.time.get_ticks() - tiempo_movimiento > 1000:
        direccion_movimiento = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            target_pos = list(pygame.mouse.get_pos())
            movimiento_realizado = True
            if portero_pos[0] < target_pos[0]:
                direccion_movimiento = 'derecha'
            else:
                direccion_movimiento = 'izquierda'
            tiempo_movimiento = pygame.time.get_ticks()
    #Lógica de programación del juego
    mouse_pos = pygame.mouse.get_pos()
    if movimiento_realizado:
        actualizar_portero()
    
    elapsed_time = pygame.time.get_ticks()
    time_fraction = min(elapsed_time / 1000.0, 1.0)
    balon_pos[0] = int(balon_pos[0] + (target_pos[0] - balon_pos[0]) * velocidad * time_fraction)
    balon_pos[1] = int(balon_pos[1] + (target_pos[1] - balon_pos[1]) * velocidad * time_fraction)

    linea1_puntero_x = mouse_pos[0]
    linea1_puntero_y_1 = mouse_pos[1] - 15
    linea1_puntero_y_2 = mouse_pos[1] + 15
    linea2_puntero_x_1 = mouse_pos[0] - 15
    linea2_puntero_x_2 = mouse_pos[0] + 15
    linea2_puntero_y = mouse_pos[1]
    

    #Zona de dibujo
    ventana.fill(color_fondo)
    pygame.draw.rect(ventana, blanco, (600, 10, 300, 50))
    ventana.blit(publico, [0, 50])
    ventana.blit(fondo, [0, 0])
    ventana.blit(portero, portero_pos)
    ventana.blit(balon, balon_pos)
    pygame.draw.rect(ventana, blanco, (100, 0, 200, 50))

    pygame.draw.line(ventana, blanco, (linea1_puntero_x, linea1_puntero_y_1), (linea1_puntero_x, linea1_puntero_y_2), 5)
    pygame.draw.line(ventana, blanco, (linea2_puntero_x_1, linea2_puntero_y), (linea2_puntero_x_2, linea2_puntero_y), 5)


    #Fin Zona dibujo
    
    pygame.display.flip()
    reloj.tick(50)
pygame.quit()