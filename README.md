# Flor-de-vida-
Creamos una flor de vida, esta esta costruida por 6 circulos que se van colocando al redeor de una circunferencia central, todo con el fin de aplicair los conocimientos del tema 1.2 que son aspectos matematicos  para aplicar esto hacemos uso de las funciones trigonometricas.
En esta práctica, usamos Python (el lenguaje de programación) para que Blender sea el que mida con una regla y un compás invisibles, y ponga cada objeto en su lugar exacto.

1. Como vimos vamos a trabajar en blender, creamos un nuevo archivo e iniciamos con la codificación.
2. El primer paso es  importar blender con __bpy__ , es importante ya que nos permite controlar las fromas, luces, así como controlar todo lo que coloquemos dentro de nuestro archivo. 
la segunda librería que debemos importar es __math__ que nos ayudara a calcular cosas como seno y coseno que necesitaremos para dibujar los circulos (petalos) de nuetsra flor. 

```python
import bpy 
import math
```
3. En esta parte preparamos nuestra pantalla para despudes poder crear objetos sin ningún problema, así como también el poder eliminar y limpiar nuetsra pantalla en cada ejecución.
__bpy.ops__: "Ops" viene de Operaciones. Es la forma de decirle a Blender: "Haz algo que un usuario haría con el ratón".
__select_all(action='SELECT')__: Nos ayuda a que presionando una tecla podamos seleccionar todo lo que haya en la pantalla.
__delete()__: Borra todo lo seleccionado. Hacemos esto para que, si ejecutas el código 10 veces, no termines con 60 círculos amontonados.

```python
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
```
4. Determinaremos las variables necesarias para poder crear nuestros circulos, las cuales son : __radio, angulo_actual, paso_ angular__.

__radio__: Es la distancia desde el centro del circulo inicial que se encuntra en la posición (0,0,0) hasta donde se colocarán los nuevos círculos.

__angulo_actual__ : Es nuestro punto de partida. En matemáticas, 0 grados es hacia la derecha (el eje X positivo).

__paso_angular__ : Esto define la separación de los petalos. Como queremos solo 6 petalos en angulo es de 60 pero si quieres más círculos, este número debe ser más pequeño (por ejemplo, 30). Si quieres menos, debe ser más grande (por ejemplo, 90).

```python
radio = 3
angulo_actual = 0
paso_angular = 60
```
5. Creamos el circulo inicial con __bpy.ops.mesh.primitive_circule_add__ dentro de los parentesis colocamos su atributos que serán posición, vertices y el tamaño del radio.
   
```python
bpy.ops.mesh.primitive_circle_add(radius=radio, location=(0,0,0), vertices=64)
```
6. Para poder crear los circulos (petalos de la flor ) haremos uso de una función recursiva, en este caso __while__.
   + Condición del ciclo: Mientras el __angulo_actual sea menor__ (<) que 360 el ciclo se serguira ejecutando.
   + __math.radians(angulo_actual__): Aquí está el primer detalle técnico. Dado que la computadora solo entiende radieanes debemos transfromar el angulo actual de lo contrario los circulos estarían en              cualquier lugar.

      <img width="150" height="159" alt="image" src="https://github.com/user-attachments/assets/2929a658-4b1f-4b4a-92c5-0075195ed816" />

   + __math.cos__ y __math.sin__:  El Coseno calcula la posición en el eje horizontal (X) y el Seno en el eje vertical (Y).
   + __radio * ...__ : Si el resultado del seno/coseno es 1, y tu radio es 3, el objeto se pondrá a una distancia de 3 metros del centro. Si no multiplicamos por el radio, ¡todos los círculos quedarían               pegaditos en     el centro!

```python
# Ciclo
while angulo_actual < 360:
    # Calculo de la posicion usando trigonometria
    x = radio * math.cos(math.radians(angulo_actual))
    y = radio * math.sin(math.radians(angulo_actual))

```
6.1. Construcción de los circulos dentro del __while__ , se hará de la misma forma que el central con una diferencia en la location esta obtendrá sus valores de x y y calculados anterirmente y para el eje z un valor 0 ya que solo es un dibujo plano. 

```python
bpy.ops.mesh.primitive_circle_add(radius=radio, location=(x, y, 0), vertices=64)

```
7. El incremento que hace que nuestro ciclo no se vuelva infrinito
  +  __+=__ significa: "Toma lo que ya tienes y súmale esto".
  +  Si empezamos en 0 y el paso_angular es 60, después de esta línea el angulo_actual vale 60.

```python
angulo_actual += paso_angular

```


# Código completo 

```python
import bpy # libreria de blender
import math # libreria de matematicas para las funciones trigonometricas

# Limpiar pantalla
# Esto selecciona todos los objetos existentes y los borra para empezar de cero
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Parametros de la figura
radio = 3
angulo_actual = 0
paso_angular = 60 # Aumenta 60 grados para obtener 6 circulos al rededor

# Crear el circulo central
bpy.ops.mesh.primitive_circle_add(radius=radio, location=(0,0,0), vertices=64)

# Ciclo
while angulo_actual < 360:
    # Calculo de la posicion usando trigonometria
    x = radio * math.cos(math.radians(angulo_actual))
    y = radio * math.sin(math.radians(angulo_actual))
    
    # Circulos que se crean al rededor de la primer circunferencia
    bpy.ops.mesh.primitive_circle_add(radius=radio, location=(x, y, 0), vertices=64)
    
    # El angulo aumenta con cada iteracion para que no se vuelva un ciclo infinito
    angulo_actual += paso_angular
```



**Resultado**

<img width="443" height="577" alt="Captura de pantalla 2026-02-12 132502" src="https://github.com/user-attachments/assets/3b2c2674-e41d-46a7-a05a-df75433c31b8" />
