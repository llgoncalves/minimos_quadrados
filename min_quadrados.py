#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
# Método dos Mínimos Quadrados
def minimos_quadrados(grau, dados):
	dados = dados
	grau_polinomio = grau

	# A*X = B
	# Inicializando variáveis
	A = []
	for i in range(grau_polinomio + 1):
		A.append([0]*(grau_polinomio+1))

	X = [0]*(grau_polinomio+1)
	B = [[]]*(grau_polinomio + 1)

	# Montando o sistema
	for i in range(grau_polinomio + 1):
		for j in range(i, grau_polinomio + 1):
			x = 0

			for k in range(len(dados)):
				x += dados[k][0]**(grau_polinomio+1 - j -i)
			A[i][j] = x
			A[j][i] = x

	for i in range(grau_polinomio+1):
		soma  = 0
		for j in dados:
			soma += j[1]*j[0]**i
		B[grau_polinomio - i] = soma

	# Encontrando a solução do sistema
	X = np.linalg.solve(np.array(A), np.array(B))

	return A, B, X
