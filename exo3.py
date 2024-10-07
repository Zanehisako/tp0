import math

def calculate_surface(N):
    # Maximiser la surface : forcer une dimension à être 1
    max_surface = 2 * (N + N + 1)
    
    # Minimiser la surface : chercher les dimensions proches
    min_surface = float('inf')
    
    for a in range(1, int(math.pow(N, 1/3)) + 1):
        if N % a == 0:
            for b in range(a, int(math.sqrt(N // a)) + 1):
                if (N // a) % b == 0:
                    c = N // (a * b)
                    surface = 2 * (a*b + a*c + b*c)
                    min_surface = min(min_surface, surface)
    
    return min_surface, max_surface

# Lecture de l'entrée
N = int(input())

# Calcul des surfaces minimale et maximale
min_surface, max_surface = calculate_surface(N)

# Affichage du résultat
print(min_surface, max_surface)
