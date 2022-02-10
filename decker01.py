#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:28:26 2022

@author: framas
"""
#se corresponde con la PROPUESTA 1: tenemos 8 programas ejecutandose a la vez con la función task
#no entran 2 a la vez en la sección crítica (por eso nuestro contador es 800), esto lo conseguimos gracias al turno. Cuando es el turno 
#del proceso 1 se mete en la crítica y mientras los demás están en la sección no crítica. Hay 8 procesos que se ejecutan 100 veces= contador 800
from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value, Array
N = 8 #hay 8 procesos
def task(common, tid, turn):
    a = 0
    for i in range(100):
        print(f'{tid}−{i}: Non−critical Section')
        a += 1
        print(f'{tid}−{i}: End of non−critical Section')
        while turn.value!=tid:
            pass
        print(f'{tid}−{i}: Critical section') #la sección crítica es lo que hace el programa que en este caso es aumentar el contador
        v = common.value + 1
        print(f'{tid}−{i}: Inside critical section')
        common.value = v
        print(f'{tid}−{i}: End of critical section')
        turn.value = (tid + 1) % N

def main():
    lp = []
    common = Value('i', 0)
    turn = Value('i', 0)
    for tid in range(N):
        lp.append(Process(target=task, args=(common, tid, turn))) #lista con los 8 procesos
    print (f"Valor inicial del contador {common.value}")
    for p in lp:
        p.start() #empiezan los procesos a la vez
    for p in lp:
        p.join() #espera a que acaben los 8 procesos para pasar al print 
    print (f"Valor final del contador {common.value}")
    print ("fin")

if __name__ == "__main__":
    main()