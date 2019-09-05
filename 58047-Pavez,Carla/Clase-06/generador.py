import random
def generador(minimo,maximo):
    return random.randint(minimo,maximo)
if __name__ == "__main__":
    print(generador(1,20))
   # a=generador(1,100)
   # b=generador(5,10)
   # print(str(a)+" "+str(b))