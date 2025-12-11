# Título del proyecto
Look&Go

# Resumen del proyecto
Look&Go es un proyecto que permite controlar la asistencia de los usuarios mediante la identificación facial.

Una vez inicias es programa te realiza una foto de tu cara y la comprueba con el resto de imágenes guardadas en la base de datos (JSON).

Si el usuario está registrado, se le permite acceder al programa y puede realizar las funciones disponibles.

Si el usuario no está registrado, se le pide que se registre para poder utilizar el programa.

# Tecnologías utilizadas
- Python como lenguaje de programación.
    Dentro del lenguaje hemos dividodo las carpetas en:
        - bbdd (base de datos): Donde se encuentra el archivo JSON que almacena los usuarios.
        - fotos: Para guardar las fotos tomadas del usuario
        - src (fuente): Donde se encuentran los archivos principales del programa.

- JSON como lenguaje de base de datos.

# ¿Como hemos desarrollado el proyecto?
Para este proyecto hemos utilizado la metodología agil Scrum para la gestión del proyecto.

Scrum nos permite dividir el proyecto en sprints semanales.
En nuestro caso el proyecto nos ha llevado 2 semanas.

## Primera semana
Durante la primera semana hemos realizado la planificación del proyecto, realizando en pseudocódigo los algoritmos principales, pensado como vamos divir las carpetas del proyecto. Posteriormente hemos pasado a código los algoritmos principales.

## Segunda semana
Durante la segunda semana terminamos de implementar todos los algoritmos que faltaban, creamos la clase usuario y realizamos pruebas para comprobar que todo funciona correctamente.


# Historia de usuario

- **Inicio de sesión facial**: Como usuario registrado, quiero que el sistema me identifique automáticamente mediante reconocimiento facial por voz para acceder a las funcionalidades.

- **Registro de nuevos usuarios**: Como usuario no registrado, quiero que el asistente detecte mi presencia y me ofrezca la posibilidad de registrarme mediante comandos de voz y una captura fotográfica, para poder acceder al sistema en el futuro.

- **Interacción por voz**: Como usuario validado, quiero poder realizar consultas (hora, fecha) y acciones (abrir navegador, YouTube) mediante comandos de voz para agilizar mis tareas.

# Licencias
Este producto ha sido desarrollado con fines educativos, como proyecto escolar.