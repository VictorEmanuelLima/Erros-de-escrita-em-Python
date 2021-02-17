import re
import math
def le_textos():
    texto = input("Digite o texto ")
    return texto

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

#implementacao da algoritmo busca binaria de forma recursiva
def calcula_erros(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sen = separa_sentencas(texto)
    nusen = 0
    caras = 0
    fras = []
  
    
    n_f= 0
    for a in range(len(sen)):       
        f_aux = separa_frases(sen[a])
        fras.append(f_aux)
        nusen += 1
        caras += len(sen[a])

    tp2 = [] 
    caraf =0
    n_f= 0
    for a in range(len(fras)):
        for b in range(len(fras[a])):
            pala_a = separa_palavras(fras[a][b])
            tp2.append(pala_a)
            caraf += len(fras[a][b])
            n_f += 1
 

    carap = 0
    tp3 = []
    for a in range(len(tp2)):
        for b in range(len(tp2[a])):
            tp3.append(tp2[a][b])
    tp2 = tp3[:]
    np = len(tp2)
    palavras_erradas = []
    for a in tp2:
        busca = Busca_binaria(dicio, a)
        if busca == False:
            palavras_erradas.append(a)
    if len(palavras_erradas) == 0:
        return 'Sem erros'
    for i in palavras_erradas:
        if i in vogais:
            palavras_erradas.remove(i)
    for c in palavras_erradas:
        if c in caracteres:
            palavras_erradas.remove(c)
    for j in palavras_erradas:
        aux = j.lower()
        busca2 = Busca_binaria(dicio, aux)
        if busca2 != False:
            palavras_erradas.remove(j)
    resolver = (math.sqrt(len(palavras_erradas)) // 1) + 1 # implementei isso pois estava com erro ao reconhecer numeros. Declarei a varialvel com nome de 'resolver' pois ainda está por resolver, rs.
    while resolver >= 1:
        for k in palavras_erradas:
            if k.isdigit():
                palavras_erradas.remove(k)
        resolver -= 1
    resolver = (math.sqrt(len(palavras_erradas)) // 1)
    while resolver >= 1:
        for j in palavras_erradas:
            aux = j.lower()
            busca2 = Busca_binaria(dicio, aux)
            if busca2 != False:
                palavras_erradas.remove(j)
        resolver -= 1                                      # 
    if len(palavras_erradas) == 0:
        return 'Sem erros'
    return palavras_erradas
    #pass

    
def Busca_binaria(lista, elemento, min=0, max=None):
    if max == None:
        max = len(lista)-1
    if max < min:
        return False
    else:
        meio = min + (max-min)//2
    if lista[meio] > elemento:
        return Busca_binaria(lista, elemento, min, meio-1)
    elif lista[meio] < elemento:
        return Busca_binaria(lista, elemento, meio+1, max)
    else:
        return meio

def main():
    i = 's'
    while i=='s' or i=='S':
        texto = le_textos()
        res = calcula_erros(texto)
        print('Resultado - ', res)
        i = input('deseja continua? s/n: ')
        

import palavras
vogais = ['A','E','I','O','U','a','e','i','o','u']
caracteres = ['-','_','"',"'",'^','~', '=', '+', ';', ':',',','.','?','/']
dicio = palavras.dicio()
dicio = separa_palavras(dicio) # total de palavras em português - 261800
print("----------Criador - Victor Emanuel Sousa Lima-------------")
print("-------Ultima modificação - 01/02/2021 por Victor Emanuel-------")
print(" ")
print(" ")
print("----O algoritmo devolve as palavras erradas de um texto lido------")
print("-----------total de palavras em português - 261800----------------")
print(" ")
print(" ")
main()
