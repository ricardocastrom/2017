def aristas(lista):
    return aristaAux(lista[0],lista[1:],0)
def aristaAux(numero,lista,contador):
    # calcula las aristas de la primera iteración,manda a llamar la que dibuja el camino y
    #llama la funcion con el resto de la lista
    aristasTotales=[]
    contador=1
    if(lista==[]):
        return
    aristasTotales.append(lista[0])
   # print(lista)
    while contador<= lista[0][1]:
    #    print(lista,contador)
        aristasTotales.append(lista[1])
        lista.remove(lista[1])
        contador=contador+1
    #print(lista)
    respuesta=aristasTotales.append( lista[1])
    lista.remove(lista[1])
    lista.remove(lista[0])
    #print([aristasTotales,lista])
    printCamino(aristasTotales[1:-1],aristasTotales[-1],0,[],[],aristasTotales[-1],aristasTotales[0][0])
    if(contador==numero):
        return
    else:
        print(" ")
        return aristaAux(numero,lista,contador+1)        

#imprime los nodos con camino
def printCamino(lista,numero,suma,listaRespuestas,Totales,numero2,nodos):
    if (lista==[]):
        return funx(Totales,numero2,nodos);
    else:
        contador=0
        tamaño=len(lista)
        listaCaminos=[]
        while contador<tamaño:
            if (numero in lista[contador] and ((lista[contador][0] in listaRespuestas)==False or (lista[contador][1] in listaRespuestas)==False)  ):
                print(lista[contador],suma+6)
                listaCaminos.append(lista[contador])
                lista.remove(lista[contador])
                contador=contador-1
                tamaño=tamaño-1
                listaRespuestas=sumaRespuestas(listaRespuestas,respuestas(listaCaminos,numero))
                Totales=Totales+listaRespuestas
            elif((lista[contador][0] in listaRespuestas)==True and (lista[contador][1] in listaRespuestas)==True):
                lista.remove(lista[contador])
                contador=contador-1
                tamaño=tamaño-1
            elif(listaRespuestas==[] and Totales!=[]):
                return funx(Totales,numero2,nodos);
            contador=contador+1
    
   
    #print(listaRespuestas,Totales)
   
    return printCamino(lista,listaRespuestas[0],suma+6,listaRespuestas[1:],Totales,numero2,nodos)

#Imprime los nodos sin camino
def funx(Totales, numero,nodos):
    contador=1

    while contador<=nodos:
      #  print(nodos,Totales,contador)
        if((contador in Totales)==False and contador!=numero):
            print([numero,contador],"-1")
        contador=contador+1
def respuestas(lista,numero):
    contador=0
    tamaño=len(lista)
    listaRespuestas=[]
    while contador<tamaño:
        if (lista[contador][0]==numero):
            listaRespuestas.append(lista[contador][1])
        elif(lista[contador][1]==numero):
            listaRespuestas.append(lista[contador][0])
        contador=contador+1
   
    return listaRespuestas

def sumaRespuestas(lista1,lista2):
    contador=0
    tamaño=len(lista2)
    while tamaño>contador:
       # print(lista2[contador])
        if((lista2[contador] in lista1) == False):
            lista1.append(lista2[contador])
        contador=contador+1
   # print(lista1)
    return lista1
