listaPosiciones=[]
def botClean(lista):
    posicionBot=[0,0]
    
    tamaño= 5
    contado=0
    while (contador<tamaño):
        contador2=0
        while(contador2<tamaño):
            if(lista[contador][contador2]=="d"):
                listaPosiciones.append([contador,contador2])
            contador2=contador2+1
        contador=contador+1
    
    while(listaPosiciones!=[]):
        caminar(posicionBot,MasCercano(bot,listaPosiciones))

def MasCercano(bot,dirty):
    tamaño=len(dirty)
    contador=1
    cercano=dirty[0]
    while(contador<tamaño):
        
        if(abs(cercano[0]-bot[0])+abs(cercano[1]-bot[1])> abs(dirty[contador][0]-bot[0])+abs(dirty[contador][1]-bot[1])):
            cercano=dirty[contador]
        contador=contador+1
    return cercano
        

def caminar(bot,cercano):
    tamano=5
 
    while(tamano!=0):
        if(bot[0]>cercano[0]):
            bot[0]=bot[0]-1
            print('Up')
            tamano=abs(bot[0]-cercano[0])
            imprimir(bot,listaPosiciones)
        elif (bot[0]<cercano[0]):
            bot[0]=bot[0]+1
            print('Down')
            tamano=abs(bot[0]-cercano[0])
            imprimir(bot,listaPosiciones)
    tamano=abs(bot[1]-cercano[1])
    
    while(tamano!=0):
        if(bot[1]>cercano[1]):
            bot[1]=bot[1]-1
            print('left')
            tamano=abs(bot[1]-cercano[1])
            imprimir(bot,listaPosiciones)
        elif (bot[1]<cercano[1]):
            bot[1]=bot[1]+1
            print('right')
            tamano=abs(bot[1]-cercano[1])
            imprimir(bot,listaPosiciones)
    listaPosiciones.remove(cercano)

def imprimir(bot,listaPosiciones):
    contador=0
    while (contador<5):
        contador2=0
        while(contador2<5):
            if(contador1==bot[0] and contador2==bot[1]):
                print("b ")
            elif([contador,contador2] in listaPosiciones):
                print("d ")
            else:
                print("- ")
