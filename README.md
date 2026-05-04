# Simulación de Red con Buffer y Pérdida de Paquetes

## Descripción

Este proyecto implementa una simulación básica de comunicación en red utilizando Python. Se modela un sistema compuesto por un servidor y varios clientes que intercúan mensajes entre sí. La simulación incluye aspectos importantes de redes como la pérdida de paquetes, la congestión y el uso de buffers.

## Estructura del Código

### Clase Nodo

La clase `Nodo` representa tanto al servidor como a los clientes. Cada nodo posee:

- `tipo`: Identifica si es servidor o cliente.
- `conexiones`: Lista de nodos a los que está conectado.
- `buffer`: Lista que almacena temporalmente los mensajes recibidos.

### Métodos principales

#### agregar_conexion(nodo)
Agrega un nodo a la lista de conexiones.

#### eliminar_conexion(nodo)
Elimina un nodo de la lista de conexiones.

#### enviar_mensaje(mensaje)
Envía un mensaje a todos los nodos conectados. Se simula la pérdida de paquetes utilizando la biblioteca `random`, con una probabilidad de que el mensaje no llegue al destino.

#### recibir_mensaje(mensaje, remitente)
Recibe un mensaje y lo almacena en el buffer. También muestra información sobre el remitente. Si el buffer supera cierto tamaño, se indica que hay congestión.

#### procesar_buffer()
Procesa el primer mensaje almacenado en el buffer utilizando `pop(0)`, simulando una cola FIFO (First In, First Out).

#### reconexion(nodo)
Simula la desconexión y reconexión de un nodo, eliminándolo temporalmente de la lista de conexiones y luego agregándolo nuevamente.

## Funcionamiento

1. Se crean los nodos: un servidor y tres clientes.
2. Se establecen las conexiones entre el servidor y los clientes.
3. El servidor envía un mensaje a todos los clientes.
4. Se simula una reconexión de uno de los clientes.
5. El servidor vuelve a enviar un mensaje.
6. Cada cliente procesa los mensajes almacenados en su buffer.

## Conceptos Clave

### Buffer
Es una estructura de almacenamiento temporal donde se guardan los mensajes antes de ser procesados.

### Congestión
Ocurre cuando el buffer acumula más mensajes de los que puede procesar rápidamente.

### Pérdida de paquetes
Se simula de manera aleatoria para representar fallos en la comunicación de red.

## Requisitos

- Python 3.x
- Bibliotecas estándar: `time`, `random`, `os`

## Ejecución

Ejecutar el archivo Python desde la terminal:

```bash
python simulacion_de_red_con_perdidas_de_paquetes_y_congestion.py
