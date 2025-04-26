import random
import math
import matplotlib.pyplot as plt
import sys

rojos = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
negros = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
fibo = []

def gen_fibo(n):
    f1 = 1
    fn = 1
    fibo.append(fn)
    for _ in range(n+1):
        aux = fn
        fn = fn+f1
        f1 = aux
        fibo.append(fn)
        
    
#####################################################################

#Parolis (metodo aplicado por el grupo)       

def Paroli_Infinito(cant_tiradas,cant_corridas):
    flujos = []
    frecuencias = [0 for _ in range(cant_tiradas+1)]
    for i in range(cant_corridas):
        apuesta = 1
        banca = 0
        flujo = [banca]
        cantidad_tir = 0
        victorias = 0
        for j in range(cant_tiradas):
            banca = banca - apuesta
            flujo.append(banca)
            cantidad_tir+=1
            res = random.randint(0,36)
            if (res in rojos):
                banca = banca + (apuesta*2)
                if (victorias < 3) : 
                    apuesta = 2*apuesta
                    victorias += 1
                frecuencias[cantidad_tir] += 1
                cantidad_tir = 0
            else:
                victorias = 0
                apuesta = 1
        flujos.append(flujo)
    for i in range(cant_tiradas+1):
        frecuencias[i] /= cant_tiradas
        frecuencias[i] /= cant_corridas
    graficar_apuesta(flujos,cant_tiradas,0)
    graficar_frecuencia(frecuencias,cant_tiradas)


def Paroli_Finito(cant_tiradas,cant_corridas):
    flujos = []
    for i in range(cant_corridas):
        apuesta = 1
        banca = 150
        flujo = [banca]
        cantidad_tir = 0
        victorias = 0
        for j in range(cant_tiradas):
            if (apuesta > banca):
                flujo.append(0)
                continue
            banca = banca - apuesta
            flujo.append(banca)
            cantidad_tir+=1
            res = random.randint(0,36)
            if (res in rojos):
                banca = banca + (apuesta*2)
                if (victorias < 3) : 
                    apuesta = 2*apuesta
                    victorias += 1
                cantidad_tir = 0
            else:
                victorias = 0
                apuesta = 1
        flujos.append(flujo)
    graficar_apuesta(flujos,cant_tiradas,150)

    

    
#####################################################################

#Fibonaccis
def Fibonacci_Infinito(cant_tiradas,cant_corridas):
    gen_fibo(cant_tiradas)
    flujos = []
    frecuencias = [0 for _ in range(cant_tiradas+1)]
    for i in range(cant_corridas):
        contador = 0
        apuesta = fibo[contador]
        banca = 0
        flujo = [banca]
        cantidad_tir = 0
        for j in range(cant_tiradas):
            apuesta = fibo[contador]
            banca = banca - apuesta
            flujo.append(banca)
            cantidad_tir += 1
            res = random.randint(0,36)
            if (res in rojos):
                banca = banca + (2*apuesta)
                frecuencias[cantidad_tir] += 1
                cantidad_tir = 0
                contador = max(0,contador-2)
            else:
                contador += 1 
        flujos.append(flujo)
    for i in range(cant_tiradas+1):
        frecuencias[i] /= cant_tiradas
        frecuencias[i] /= cant_corridas
    graficar_apuesta(flujos,cant_tiradas,0)
    graficar_frecuencia(frecuencias,cant_tiradas)
    

def Fibonacci_Finito(cant_tiradas,cant_corridas):
    gen_fibo(cant_tiradas)
    flujos = []
    for i in range(cant_corridas):
        contador = 0
        apuesta = fibo[contador]
        banca = 150
        flujo = [banca]
        cantidad_tir = 0
        for j in range(cant_tiradas):
            apuesta = fibo[contador]
            if (apuesta > banca):
                flujo.append(0)
                continue
            banca = banca - apuesta
            flujo.append(banca)
            cantidad_tir += 1
            res = random.randint(0,36)
            if (res in rojos):
                banca = banca + (2*apuesta)
                cantidad_tir = 0
                contador = max(0,contador-2)
            else:
                contador += 1 
        flujos.append(flujo)
    graficar_apuesta(flujos,cant_tiradas,150)
            
            
#####################################################################

#D'alamberts
def DAlambert_Infinito(cant_tiradas,cant_corridas):
    flujos = []
    frecuencias = [0 for _ in range(cant_tiradas+1)]
    for i in range(cant_corridas):
        apuesta = 1
        banca = 0
        flujo = [banca]
        cantidad_tir = 0
        for j in range(cant_tiradas):
            banca = banca - apuesta
            flujo.append(banca)
            cantidad_tir += 1
            res = random.randint(0,36)
            if (res in rojos):
                banca = banca + (2*apuesta)
                frecuencias[cantidad_tir] += 1
                cantidad_tir = 0
                if apuesta > 1:
                    apuesta -= 1
            else:
                apuesta += 1
        flujos.append(flujo)
    for i in range(cant_tiradas+1):
        frecuencias[i] /= cant_tiradas
        frecuencias[i] /= cant_corridas
    graficar_apuesta(flujos,cant_tiradas,0)
    graficar_frecuencia(frecuencias,cant_tiradas)

        
def DAlambert_Finito(cant_tiradas,cant_corridas):
    flujos = []
    for i in range(cant_corridas):
        apuesta = 1
        banca = 150
        flujo = [banca]
        cantidad_tir = 0
        for j in range(cant_tiradas):
            if apuesta > banca:
                flujo.append(0)
                continue
            banca -= apuesta
            flujo.append(banca)
            cantidad_tir += 1
            res = random.randint(0,36)
            if (res in rojos):
                banca = banca + (apuesta*2)
                cantidad_tir = 0
                apuesta = max(1,apuesta-1)
            else:
                apuesta += 1
        flujos.append(flujo)
    graficar_apuesta(flujos,cant_tiradas,150)
    
                
#####################################################################

#Martingalas
def MartinGala_Infinito(cant_tiradas,cant_corridas):
    flujos = []
    frecuencias = [0 for _ in range(cant_tiradas+1)]
    for i in range(cant_corridas):
        apuesta = 1
        banca = 0
        flujo = [banca]
        cantidad_tir = 0
        for j in range(cant_tiradas):
            banca = banca - apuesta
            flujo.append(banca)
            cantidad_tir+=1
            res = random.randint(0,36)
            if (res in rojos):
                banca = banca + (apuesta*2)
                apuesta = 1
                frecuencias[cantidad_tir] += 1
                cantidad_tir = 0
            else:
                apuesta = apuesta*2
        flujos.append(flujo)
    for i in range(cant_tiradas+1):
        frecuencias[i] /= cant_tiradas
        frecuencias[i] /= cant_corridas
    graficar_apuesta(flujos,cant_tiradas,0)
    graficar_frecuencia(frecuencias,cant_tiradas)


def MartinGala_Finito(cant_tiradas,cant_corridas):
    flujos = []
    for i in range(cant_corridas):
        apuesta = 1
        banca = 150
        flujo = [banca]
        cantidad_tir = 0
        for j in range(cant_tiradas):
            if (apuesta > banca):
                flujo.append(0)
                continue
            banca = banca - apuesta
            flujo.append(banca)
            cantidad_tir+=1
            res = random.randint(0,36)
            if (res in rojos):
                banca = banca + (apuesta*2)
                apuesta = 1
                cantidad_tir = 0
            else:
                apuesta = apuesta*2
        flujos.append(flujo)
    graficar_apuesta(flujos,cant_tiradas,150)
                

def graficar_apuesta(flujos,cant_jugadas,ini):
    numero_jugada = [i+1 for i in range(cant_jugadas+1)]
    banca = [ini for i in range(cant_jugadas+1)]
    plt.plot(figsize=(25, 10))
    cant = 1
    for flu in flujos:
        plt.plot(numero_jugada,flu,linestyle='-',label=f'Flujo Caja {cant}')
        cant += 1
    plt.plot(numero_jugada,banca,linestyle='-.',label='Flujo Caja Inicial')
    plt.title('Flujo de caja')
    plt.xlabel('Numero Jugada')
    plt.ylabel('Cantidad de Capital')
    plt.legend()

    plt.tight_layout()
    plt.show()
        
def graficar_frecuencia(frecuencias,cant_jugadas):
    ini = -1
    for i in range(cant_jugadas-1,0,-1):
        if frecuencias[i] != 0: 
            ini = i
            break
    frecu = [frecuencias[i] for i in range(ini+1)]
    print(ini)
    numero_jugada = [i+1 for i in range(ini+1)]
    plt.plot(figsize=(25, 10))
    plt.bar(x=numero_jugada,height=frecu)
    plt.title('Frecuencia relativa de obtener la apuesta favorable segun n')
    plt.xlabel('Numero Jugada')
    plt.ylabel('Frecuencia Relativa')
    plt.legend()

    plt.tight_layout()
    plt.show()

##Ingreso de los parametros por consola
##python tp1.2.py -c XX -n YY -e ZZ -s W -a V
if (len(sys.argv)!= 9 or sys.argv[1] != "-c" or sys.argv[3] != "-n" or sys.argv[5] != "-s" or sys.argv[7] != "-a"):
    print("Uso: python tp1.py -c <cant_corridas> -n <cant_tiradas> -s <estrategia_elegida> -a <tipo_de_capital>")
    sys.exit(1)

cant_corridas = int(sys.argv[2])
cant_tiradas = int(sys.argv[4])
estrategia = sys.argv[6]
capital = sys.argv[8]

if (capital == "i"):
    if (estrategia == "m"): MartinGala_Infinito(cant_tiradas,cant_corridas)
    if (estrategia == "d"): DAlambert_Infinito(cant_tiradas,cant_corridas)
    if (estrategia == "f"): Fibonacci_Infinito(cant_tiradas,cant_corridas)
    if (estrategia == "o"): Paroli_Infinito(cant_tiradas,cant_corridas)
elif (capital == "f"):
    if (estrategia == "m"): MartinGala_Finito(cant_tiradas,cant_corridas)
    if (estrategia == "d"): DAlambert_Finito(cant_tiradas,cant_corridas)
    if (estrategia == "f"): Fibonacci_Finito(cant_tiradas,cant_corridas)
    if (estrategia == "o"): Paroli_Finito(cant_tiradas,cant_corridas)