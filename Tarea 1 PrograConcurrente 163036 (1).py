#!/usr/bin/env python
# coding: utf-8

# Tarea 1 Progra Concurrente 
# Diego Rdz 163036
# 
# Version Recursiva

# In[3]:


def suma_recursiva(n):
    if n == 0:
        return 0
    else:
        return n + suma_recursiva(n - 1)

# Ejemplo de uso
n = 10
print(suma_recursiva(n))  # Salida: 55


# Versión con Ciclo

# In[4]:


def suma_con_ciclo(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

# Ejemplo de uso
n = 10
print(suma_con_ciclo(n))  # Salida: 55


# Pregunta 2: Una función que haga la misma suma, pero con la fórmula general (n * (n+1) / 2 )

# In[5]:


def suma_formula(n):
    return n * (n + 1) // 2  # Uso de // para división entera

# Ejemplo de uso
n = 10
print(suma_formula(n))  # Salida: 55


# Pregunta 3: Calcula el tiempo promedio que se tardan ambos cálculos para n=100. ¿Cuál fue más rápida?

# In[6]:


import time

# Función recursiva
def suma_recursiva(n):
    if n == 0:
        return 0
    else:
        return n + suma_recursiva(n - 1)

# Función con ciclo
def suma_con_ciclo(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

# Función con fórmula general
def suma_formula(n):
    return n * (n + 1) // 2

# Calcular tiempos para n = 100
n = 100
num_trials = 10000

# Medir tiempo para la función recursiva
start_time = time.time()
for _ in range(num_trials):
    suma_recursiva(n)
recursiva_time = (time.time() - start_time) / num_trials

# Medir tiempo para la función con ciclo
start_time = time.time()
for _ in range(num_trials):
    suma_con_ciclo(n)
ciclo_time = (time.time() - start_time) / num_trials

# Medir tiempo para la función con fórmula
start_time = time.time()
for _ in range(num_trials):
    suma_formula(n)
formula_time = (time.time() - start_time) / num_trials

print(f"Tiempo promedio (recursiva): {recursiva_time:.8f} segundos")
print(f"Tiempo promedio (ciclo): {ciclo_time:.8f} segundos")
print(f"Tiempo promedio (fórmula): {formula_time:.8f} segundos")


# In[ ]:




