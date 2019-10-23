import sys


def print_results(quadros, tam, fifo, lru, opt ):
	print("%5d quadros, %7d refs: FIFO: %5d PFs, LRU: %5d PFs, OPT: %5d PFs" % (quadros, tam, fifo, lru, opt))

def fifo(quadros, input_array):
	memoria = []
	pos = 0
	pfs = 0
	# para cada valor de pagina lida
	for pagina in input_array:
		# se a pagina n esta na memora e se memoria não esta cheia
		if (len(memoria) < quadros  and pagina not in memoria):	
			memoria.append(pagina)
			pos += 1
			#proxima posição de array para FIFO
			pos = pos % quadros	
			pfs += 1
		# se memoria esta cheia e pagina esta na memoria n faz nada	
		elif(pagina in memoria):
			continue
		# se pagina n esta na memoria e memoria cheia tira o primeiro que entrou e bota o novo
		else:
			memoria[pos] = pagina
			pos += 1
			#proxima posição de array para FIFO
			pos = pos % quadros	
			pfs += 1
	return pfs


def lru(quadros, input_array):
	memoria = []
	temp = 0
	pfs = 0
	# dic que guarda pagina e ultima vez que foi acessada
	dic = {}
	for pagina in input_array:
		# se a pagina n esta na memora e se memoria não esta cheia
		if (len(memoria) < quadros  and pagina not in memoria):	
			memoria.append(pagina)
			# guarda o tempo que entrou na memoria
			dic[pagina] = temp
			pfs += 1
		# se memoria esta cheia e pagina esta na memoria
		elif(pagina in memoria):
			# guarda o ultimo acesso
			dic[pagina] = temp
		# se pagina n esta na memoria e memoria cheia tira o primeiro que entrou e bota o novo
		else:
			mim= -1
			p = 0
			# pega o item que n é acessado a mais tempo
			for item in dic:
				t = dic[item]
				if (mim < 0):
					p = item
					mim = t
				elif( mim > t):
					p = item
					mim = t
		 	# bota pagina na memoria no lugar do item que estava a mais tempo sem acesso
			memoria[memoria.index(p)] = pagina
			# retira pagina que saiu da memoria do dicionario 
			dic.pop(p)
			## guarda nova pagina no dicionario
			dic[pagina] = temp
			pfs +=1 	
		temp += 1
	return pfs


def opt(quadros, input_array):
	memoria = []
	pfs = 0
	dic = {}

	# gera dicionario com chave o numero da pagina e valor um array com os tempos de entrada de cada valor
	for i in range(len(input_array)):
		if (input_array[i] not in dic.keys()):
			temp = []
			temp.append(i)
			dic[input_array[i]] = temp
		else:
			temp = dic[input_array[i]]
			temp.append(i)
			dic[input_array[i]] = temp


	for pagina in input_array:
		# se a pagina n esta na memora e se memoria não esta cheia
		if (len(memoria) < quadros  and pagina not in memoria):	
			memoria.append(pagina)
			pfs += 1
            # remove do dicionario o tempo em que entrou
			dic[pagina] = dic[pagina][1:]

		# se memoria esta cheia e pagina esta na memoria
		elif(pagina in memoria):
			# verifica se vai aparecer de novo e altera o arry se sim
			if(len(dic[pagina]) > 0):
				dic[pagina] = dic[pagina][1:]
			# se n vai aparecer de novo, remove do dicionario
			else:
				dic.pop(item)
		else:
			maxi= -1
			p = 0
			for item in dic:
				if (item in memoria):
					# seleciona o item que vai remover da memoria
					if(len(dic[item]) > 0):
						oc = dic[item][0]
					else:
						oc = len(input_array) + 1
					if( maxi < oc):
						p = item
						maxi = oc
			# achidiona o novo item na memoria
			memoria[memoria.index(p)] = pagina
			# verifica se vai aparecer de novo e altera o arry se sim
			if(len(dic[pagina]) > 0):
				dic[pagina] = dic[pagina][1:]
			# se n vai aparecer de novo, remove do dicionario
			else:
				dic.pop(pagina)	

			pfs +=1 

	return pfs


def main():
	quadros = int(sys.argv[1])
	input_array = []
	for line in sys.stdin:
		input_array.append(int(line))
	
	print_results(quadros, len(input_array), fifo(quadros,input_array),lru(quadros,input_array), opt(quadros, input_array))



main()

