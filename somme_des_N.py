def Init(Nomber_Carre:int,Carres:list):
    for i in range(Nomber_Carre):
        carre = (i+1)*2;
        Carres.append(carre)

def Surface(n):
    return n*n

def SommeCarres(Carres:list):
    result = 0
    for i in Carres:
        result += Surface(i)

    return result
        


print("Enter Le nomber des carres:")
Nomber_Carre = int(input())

Carres = []

Init(Nomber_Carre,Carres)
print("les Carres:",Carres)

print("Result :",SommeCarres(Carres) % 1000000007)



