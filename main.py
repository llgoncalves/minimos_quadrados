#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse, sys
from min_quadrados import minimos_quadrados, px

def main(grau, valor_x):
	dados = []
	# Ler valores do arquivo (x e f(x))
	with open("dados", "r") as f:
		for line in f:
			line = line.split('\t')
			dados.append([float(line[0]), float(line[1])])

	# Aplicando o Método dos Mínimos Quadrados
	A, B, X = minimos_quadrados(grau, dados)

	print "Dados de entrada:\n", dados
	print "\nA:\n", A
	print "\nB:\n", B
	print "\nX:\n", X

	if valor_x is not None:
		print "\np("+str(valor_x)+"):\n", px(valor_x, X)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-g", type=int, default=1,
	 					help="Definir grau do polinômio")
	parser.add_argument("-p", type=float, default=None,
						help="Valor de x, para calcular o p(x)")

	args = parser.parse_args()
	grau = args.g
	x = args.p
	main(grau, x)
