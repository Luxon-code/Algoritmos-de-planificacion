def RoundRobin(n, arrival_time, burst_time, quantum):
    remaining_time = burst_time[:]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0
    time = 0

    while True:
        done = True
        for i in range(n):
            if remaining_time[i] > 0:
                done = False
                # Proceso tiene tiempo de burst mayor que el quantum
                if remaining_time[i] > quantum:
                    time += quantum
                    remaining_time[i] -= quantum
                else:
                    # Proceso termina en esta ronda
                    time += remaining_time[i]
                    waiting_time[i] = time - burst_time[i] - arrival_time[i]
                    turnaround_time[i] = waiting_time[i] + burst_time[i]
                    total_waiting_time += waiting_time[i]
                    total_turnaround_time += turnaround_time[i]
                    remaining_time[i] = 0
        if done:
            break

    # Imprimir resultados
    print("Proceso\tLlegada\tDuración\tEspera\tRetorno")
    for i in range(n):
        print(f"{i+1}\t{arrival_time[i]}\t{burst_time[i]}\t\t{waiting_time[i]}\t{turnaround_time[i]}")
    print(f"Tiempo de espera promedio: {total_waiting_time / n:.2f}")
    print(f"Tiempo de retorno promedio: {total_turnaround_time / n:.2f}")

# Ejemplo de uso del algoritmo RR (Round Robin)
print("Algoritmo RR (Round Robin)".upper())
n = 3
arrival_time = [0, 1, 2]
burst_time = [10, 5, 8]
quantum = 4
RoundRobin(n, arrival_time, burst_time, quantum)
