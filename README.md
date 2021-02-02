# RoboticaUdeA
**Nota 1:** Las instrucciones dadas asumen que ya se tiene creado y configurado previamente el espacio de trabajo.

**Nota 2:** Es importante saber que la versión de Linux usada fue **Ubuntu 16.04** con la versión **Kinetic** de ROS.

Para utilizar correctamente este repositorio y garantizar su funcionamiento debe seguir los siguientes pasos; Clonar el repositorio usando el comando en consola:
```
$ git clone https://github.com/Will0204/RoboticaUdeA
```
En la carpeta src del espacio de trabajo creado pegar las carpetas **ur5** y **robotic** descargadas previamente del repositorio

Inicie el ambiente ROS en una consola 
```
$ roscore
```
y en otra diferente escriba el comando
```
$ roslaunch ur5_gazebo ur5_6_cubes.launch
```

Se deberá abrir el ambiente Gazebo con el mundo creado asi:

Para llevar el robot a la posición inicial se debe dar click en el botón **play** en la parte inferior izquierda.

Finalmente, en una consola nueva, lance el ejecutable .py que moverá el robot según la tarea propuesta; el comando es:

```
$ rosrun ur5_gazebo send_trajectory.py
```
Luego de ejecutarse completamente la secuencia el resultado debe verse así:
