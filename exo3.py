import math

def calculate_surface(i,j,k):
    return (2*(i*j) +2*(i*k)+ 2*(j*k))  

def calculate_surface_max_min(N):
    combinations = []
    for i in range(1,N):
        for j in range(1,N-i):
            k = math.floor(N/(i*j))
            if (i*j*k) == N:
                print('the combinations are :',i,j,k)
                surface = calculate_surface(i,j,k);
                print('the result is :',surface)
                combinations.append(surface) 
    max_surface = max(combinations)
    min_surface = min(combinations)

    
    
    return min_surface, max_surface

# Lecture de l'entrée
N = int(input())

# Calcul des surfaces minimale et maximale
min_surface, max_surface = calculate_surface_max_min(N)

# Affichage du résultat
print(min_surface, max_surface)
