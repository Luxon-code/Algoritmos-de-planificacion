def SJN(n, arrival_time, burst_time):
    # Inicializar listas y variables
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completed = [False] * n
    total_waiting_time = 0
    total_turnaround_time = 0
    time = 0
    completed_processes = 0

    while completed_processes < n:
        # Seleccionar el siguiente proceso con el menor burst time
        min_burst = float('inf')
        current_process = -1
        for i in range(n):
            # Seleccionar procesos que hayan llegado y no estén completados
            if arrival_time[i] <= time and not completed[i] and burst_time[i] < min_burst:
                min_burst = burst_time[i]
                current_process = i

        if current_process == -1:
            # Incrementar tiempo si no hay procesos disponibles
            time += 1
            continue

        # Calcular tiempos para el proceso seleccionado
        waiting_time[current_process] = time - arrival_time[current_process]
        turnaround_time[current_process] = waiting_time[current_process] + burst_time[current_process]
        time += burst_time[current_process]
        completed[current_process] = True
        completed_processes += 1
        total_waiting_time += waiting_time[current_process]
        total_turnaround_time += turnaround_time[current_process]

    # Imprimir resultados
    print("Proceso\tLlegada\tDuración\tEspera\tRetorno")
    for i in range(n):
        print(f"{i+1}\t{arrival_time[i]}\t{burst_time[i]}\t\t{waiting_time[i]}\t{turnaround_time[i]}")
    print(f"Tiempo de espera promedio: {total_waiting_time / n:.2f}")
    print(f"Tiempo de retorno promedio: {total_turnaround_time / n:.2f}")

# Ejemplo de uso del algoritmo SJN (Shortest Job Next)
print("algoritmo SJN (Shortest Job Next)".upper())
n = 4
arrival_time = [0, 4, 10, 12]   # Tiempos de llegada espaciados
burst_time = [15, 5, 8, 12]     # Tiempos de ejecución largos
SJN(n, arrival_time, burst_time)
