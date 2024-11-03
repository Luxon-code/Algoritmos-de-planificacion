def RoundRobin(n, arrival_time, burst_time, quantum):
    # Copia de tiempos de burst restantes para cada proceso
    remaining_time = burst_time[:]
    # Lista para almacenar el tiempo de espera de cada proceso
    waiting_time = [0] * n
    # Lista para almacenar el tiempo de retorno (turnaround) de cada proceso
    turnaround_time = [0] * n
    # Variables para acumular el tiempo total de espera y de retorno
    total_waiting_time = 0
    total_turnaround_time = 0
    # Variable de tiempo actual en la simulación
    time = 0

    # Bucle principal para ejecutar los procesos en rondas
    while True:
        # Marcador para verificar si todos los procesos han terminado
        done = True

        # Iterar sobre cada proceso
        for i in range(n):
            # Si el proceso aún tiene tiempo de ejecución restante
            if remaining_time[i] > 0:
                done = False  # Aún queda al menos un proceso por terminar

                # Si el tiempo de burst restante es mayor que el quantum
                if remaining_time[i] > quantum:
                    # Incrementar el tiempo actual con el quantum
                    time += quantum
                    # Reducir el tiempo restante del proceso en el quantum
                    remaining_time[i] -= quantum
                else:
                    # El proceso terminará en esta ronda
                    time += remaining_time[i]  # Incrementar el tiempo con el tiempo restante
                    # Calcular el tiempo de espera: tiempo actual - burst inicial - tiempo de llegada
                    waiting_time[i] = time - burst_time[i] - arrival_time[i]
                    # Calcular el tiempo de retorno: tiempo de espera + burst original
                    turnaround_time[i] = waiting_time[i] + burst_time[i]
                    # Acumular los tiempos totales de espera y retorno
                    total_waiting_time += waiting_time[i]
                    total_turnaround_time += turnaround_time[i]
                    # Marcar el proceso como terminado
                    remaining_time[i] = 0

        # Si todos los procesos están terminados, salir del bucle
        if done:
            break

    # Imprimir los resultados de cada proceso
    print("Proceso\tLlegada\tDuración\tEspera\tRetorno")
    for i in range(n):
        print(f"{i+1}\t{arrival_time[i]}\t{burst_time[i]}\t\t{waiting_time[i]}\t{turnaround_time[i]}")

    # Calcular e imprimir los promedios de tiempo de espera y tiempo de retorno
    print(f"Tiempo de espera promedio: {total_waiting_time / n:.2f}")
    print(f"Tiempo de retorno promedio: {total_turnaround_time / n:.2f}")


# Ejemplo de uso del algoritmo RR (Round Robin)
print("Algoritmo RR (Round Robin)".upper())
n = 4
arrival_time = [0, 4, 10, 12]   # Tiempos de llegada espaciados
burst_time = [15, 5, 8, 12]     # Tiempos de ejecución largos
quantum = 3                      # Quantum para el algoritmo RR
RoundRobin(n, arrival_time, burst_time, quantum)
