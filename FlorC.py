import bpy #libreria de blender
import math # libreria de matematicas para las funciones trigonometricas


#limpiar pantalla 
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

#parametros de la figura
radio=3
angulo_actual=0
paso_angular=60 #Aumenta 60 grados para obtener 6 circulos al rededor

#Crear el curculo central
bpy.ops.mesh.primitive_circle_add(radius=radio, location=(0,0,0), vertices=64)

#cilo 
while angulo_actual<360:
  x=radio*math.cos(math.radians(angulo_actual))
  y=radio*math.sin(math.radians(angulo_actual))
  
  
#Circulos que se crean al rededor de la primer circunferencia
  bpy.ops.mesh.primitive_circle_add(radius=radio, location=(x,y,0), vertices=64)
  
  #El angulo aumenta con cadaiteracion para que no se vuelva un ciclo infinito
  angulo_actual+=paso_angular 
