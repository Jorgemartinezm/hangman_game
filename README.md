# El juego del Ahorcado

Este código es un juego del ahorcado en el que se elige una palabra aleatoria de un archivo de texto y se va adivinando letra por letra. El juego comienza mostrando una serie de rayas que representan las letras de la palabra a adivinar. Cada vez que el jugador ingresa una letra, si la letra se encuentra en la palabra se reemplaza la raya correspondiente en la pantalla. Si la letra no se encuentra en la palabra, se reduce la cantidad de vidas del jugador. El juego finaliza cuando se adivina la palabra o se agotan las vidas del jugador.

La función normalize se utiliza para reemplazar caracteres con tildes por su versión sin tildes. Esto se hace para evitar problemas con la lectura del archivo de texto y para facilitar la comparación de las letras ingresadas por el usuario con las letras de la palabra a adivinar.

La función run se encarga de ejecutar el juego en sí. Primero se lee el archivo de texto y se elige una palabra aleatoria de la lista de palabras. Luego se utiliza la función normalize para reemplazar los caracteres con tildes por sus equivalentes sin tildes. La palabra se convierte en una lista de caracteres y se elimina el carácter de nueva línea al final de la palabra.

Se inicializan las variables necesarias para el juego, como la cantidad de caracteres de la palabra, la cantidad de aciertos, una lista de caracteres ya utilizados, la cantidad de vidas del jugador y una lista de rayas que representan la palabra a adivinar.

Luego se limpia la pantalla y se muestra el tablero del juego. A partir de este punto, se comienza el bucle principal del juego, en el que se piden letras al jugador y se verifica si la letra ingresada se encuentra en la palabra. Si la letra se encuentra, se reemplaza la raya correspondiente en la pantalla y se aumenta el contador de aciertos. Si la letra no se encuentra, se reduce la cantidad de vidas del jugador y se muestra el nuevo valor de vidas en la pantalla.

El juego continúa hasta que se adivine la palabra o se agoten las vidas del jugador. Si se adivina la palabra, se muestra un mensaje de victoria y se termina el juego. Si se agotan las vidas, se muestra un mensaje de derrota y se termina el juego.
