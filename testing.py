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
portero.set_colorkey([0, 0, 0])
publico = pygame.image.load("crowd.jpg").convert()
balon = pygame.image.load("balon.png").convert()
balon.set_colorkey([255, 0, 0])
balon_pos = [0, 0]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            balon_pos = [list(pygame.mouse.get_pos())]
    #Lógica de programación del juego
    mouse_pos = pygame.mouse.get_pos()
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
    ventana.blit(portero, [0, 0])
    ventana.blit(balon, balon_pos)
    pygame.draw.rect(ventana, blanco, (100, 0, 200, 50))

    pygame.draw.line(ventana, blanco, (linea1_puntero_x, linea1_puntero_y_1), (linea1_puntero_x, linea1_puntero_y_2), 5)
    pygame.draw.line(ventana, blanco, (linea2_puntero_x_1, linea2_puntero_y), (linea2_puntero_x_2, linea2_puntero_y), 5)


    #Fin Zona dibujo
    
    pygame.display.flip()
    reloj.tick(180)
pygame.quit()