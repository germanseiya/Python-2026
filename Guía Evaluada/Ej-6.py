"""6. Simular el comportamiento de un reloj digital, imprimiendo la hora, minutos y segundos
de un día desde las 00:00:00 horas hasta las 23:59:59 horas."""

from colorama import init, Fore
import time
init()

print(Fore.GREEN + "========================================")
print("          RELOJ DIGITAL SIMULADO        ")
print("========================================\n" + Fore.RESET)

for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
            print(Fore.CYAN + f"{hora:02d}:{minuto:02d}:{segundo:02d}" + Fore.RESET)
            time.sleep(1)
            