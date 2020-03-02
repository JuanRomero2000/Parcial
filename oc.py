import sys 

def revisar_argumentos():

    for argumento in sys.argv[1:len(sys.argv)]:
        if validar_formato_argumentos(argumento) == False:
            return False
    return True

def validar_formato_argumentos(argumento):

    if (argumento[0] == "{" and argumento.count("{")==1 and argumento.count("}") == 1 and argumento.rfind("}")==len(argumento)-1) and argumento.count(",,")==0:
        
        return True

    else:
        return False

if revisar_argumentos() == False:
    print("\nError en los argumentos")
    exit()
else:
   print("\nArgumentos validos\n")

argumento1 = sys.argv[1].replace('{','').replace('}','').replace(',',' ')
argumento2 = sys.argv[2].replace('{','').replace('}','').replace(',',' ')

conjunto1 = set(argumento1.split())
conjunto2 = set(argumento2.split())

def union(conjunto1,conjunto2):
    print(conjunto1 | conjunto2)

