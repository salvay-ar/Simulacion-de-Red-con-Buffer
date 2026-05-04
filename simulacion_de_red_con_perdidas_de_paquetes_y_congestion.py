import time
import random
import os

os.system("cls")

class Nodo:

    def __init__(self, tipo):
        self.tipo = tipo
        self.conexiones = []        
        self.buffer = [] 
                                      
    def agregar_conexion(self, nodo): 
        self.conexiones.append(nodo)
   
    def eliminar_conexion(self, nodo):
        if nodo in self.conexiones:
            self.conexiones.remove(nodo)

    def enviar_mensaje(self, mensaje):
        print(f"{self.tipo} envía: ¡{mensaje}!")

        for conexion in self.conexiones:
            if random.random() < 0.3: #(30% probabilidad de perder paquetes)
                print(f"Paquete perdido de {self.tipo} a {conexion.tipo}")
            else:
                conexion.recibir_mensaje(mensaje, self.tipo)

    def recibir_mensaje(self, mensaje, remitente):
        print(f"{self.tipo} recibe: ¡{mensaje}! (de {remitente})")

        # Guardar en buffer
        self.buffer.append((mensaje, remitente))

        # Simular congestión
        if len(self.buffer) > 3:
            print(f"{self.tipo} tiene congestión en el buffer: ({len(self.buffer)} mensajes)")

    def procesar_buffer(self):
        if self.buffer:
            mensaje, remitente = self.buffer.pop(0)
            print(f"{self.tipo} procesa: ¡{mensaje}! (de {remitente})")
        else:
            print(f"{self.tipo} no tiene mensajes en el buffer")

    def reconexion(self, nodo):
        print("\nSimulando desconexión y reconexión dinámica...")
        self.eliminar_conexion(nodo)

        time.sleep(2)

        self.agregar_conexion(nodo)
        print(f"{nodo.tipo} reconectado a {self.tipo}\n")


# Crear nodos
servidor = Nodo("Servidor")
cliente1 = Nodo("Cliente 1")
cliente2 = Nodo("Cliente 2")
cliente3 = Nodo("Cliente 3")

# Conexiones
servidor.agregar_conexion(cliente1)
servidor.agregar_conexion(cliente2)
servidor.agregar_conexion(cliente3)

cliente1.agregar_conexion(servidor)
cliente2.agregar_conexion(servidor)
cliente3.agregar_conexion(servidor)

# Mensaje
servidor.enviar_mensaje("Hola a todos")

# Simular reconexión
servidor.reconexion(cliente2)

# Reenvío mensaje     
servidor.enviar_mensaje("Hola de nuevo a todos")

# Procesar buffers
print(f"\n Procesando buffers...\n")
cliente1.procesar_buffer()
cliente2.procesar_buffer()
cliente3.procesar_buffer()