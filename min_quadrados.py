dados = []
grau_polinomio = 1

# A*X = B 
A = [[0]*(grau_polinomio + 1)]*(grau_polinomio + 1)
X = [0]*grau_polinomio
B = [[]]*(grau_polinomio + 1)

with open("dados_1", "r") as f:
	for line in f:
		line = line.split('\t')
		dados.append([float(line[0]), float(line[1])])
	
for i in range(grau_polinomio + 1):
	for j in range(i, grau_polinomio + 1):
		x = 0
		for k in range(len(dados)):
			x += dados[k][0]**(grau_polinomio + 1 - j -i)
		
		A[i][j] = x
		A[j][i] = x

for i in range(grau_polinomio+1):
	soma  = 0 
	for j in dados:
		soma += j[1]*j[0]**i
	B[grau_polinomio - i] = soma

print "Dados de entrada:\n",dados
print "\nA:\n", A 
print "\nB:\n", B	

