def FCFS(n, arrival_time, burst_time):
    # Inicializar listas para tiempos de espera y tiempos de retorno
    waiting_time = [0] * n
    turnaround_time = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0

    # Calcular los tiempos de espera
    for i in range(1, n):
        # El tiempo de espera para cada proceso es el tiempo de burst del proceso anterior 
        # más el tiempo de espera acumulado del proceso anterior
        waiting_time[i] = burst_time[i - 1] + waiting_time[i - 1]

    # Calcular los tiempos de retorno y sumar tiempos totales
    for i in range(n):
        # El tiempo de retorno de un proceso es su tiempo de burst más su tiempo de espera
        turnaround_time[i] = burst_time[i] + waiting_time[i]
        total_waiting_time += waiting_time[i]        # Acumula el tiempo de espera total
        total_turnaround_time += turnaround_time[i]  # Acumula el tiempo de retorno total

    # Imprimir los resultados
    print("Proceso\tLlegada\tDuración\tEspera\tRetorno")
    for i in range(n):
        print(f"{i+1}\t{arrival_time[i]}\t{burst_time[i]}\t\t{waiting_time[i]}\t{turnaround_time[i]}")
    print(f"Tiempo de espera promedio: {total_waiting_time / n:.2f}")
    print(f"Tiempo de retorno promedio: {total_turnaround_time / n:.2f}")

# Ejemplo de uso del algoritmo FCFS (First-Come, First-Served)
print("algoritmo FCFS (First-Come, First-Served)".upper())
n = 4
arrival_time = [0, 4, 10, 12]   # Tiempos de llegada espaciados
burst_time = [15, 5, 8, 12]     # Tiempos de ejecución largos
FCFS(n, arrival_time, burst_time)
