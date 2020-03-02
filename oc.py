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
   print(sys.argv[1])
