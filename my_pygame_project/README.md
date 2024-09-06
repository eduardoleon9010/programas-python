# Juego de la invasion con PyGame

Este proyecto es un juego sencillo de una nave espacial donde el objetivo es 
esquivar los enemigos que caen desde arriba. El juego fue creado utilizando 
la librería **PyGame**.

## Instrucciones

1. **Mover la nave**: Utiliza las flechas del teclado izquierda y derecha 
para mover la nave.
2. **Disparar**: Presiona la barra espaciadora para disparar balas desde la nave.
3. **Esquivar enemigos**: Los enemigos caen desde la parte superior de la 
pantalla y debes esquivarlos. Si chocas con uno de ellos, pierdes una vida.
4. **Ganar**: El juego se gana si eliminas 10 enemigos. 

## Características

- **Menú inicial**: Antes de comenzar el juego, se muestra un menú con 
instrucciones para empezar.
- **Enemigos dinámicos**: Los enemigos caen desde la parte superior de 
la pantalla a una velocidad constante.
- **Pantalla de Game Over**: Si tu nave choca con un enemigo y pierdes 
todas las vidas, el juego muestra una pantalla de "Game Over".
- **Pantalla de Victoria**: Si eliminas 10 enemigos, se muestra un 
mensaje de victoria.
- **Pausa**: Puedes pausar el juego presionando la tecla 'P'.

## Instalación

1. Clona o descarga este repositorio.
2. Asegúrate de tener **Python 3.x** y **PyGame** instalado. Si no tienes 
PyGame, puedes instalarlo usando:

   ```bash
   pip install pygame
