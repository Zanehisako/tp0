def distribute_tasks(servers:list, k):
    # Trier les serveurs par charge croissante
    servers.sort()
    
    for _ in range(k):
        # Ajouter une tâche au serveur le moins chargé
        servers[0] += 1
        # Réinsérer le serveur à sa place correcte
        i = 0
        while i < len(servers) - 1 and servers[i] > servers[i + 1]:
            servers[i], servers[i + 1] = servers[i + 1], servers[i]
            i += 1
    
    return servers

def calculate_imbalance(servers):
    return max(servers) - min(servers)

def load_balance(N, initial_loads, k):
    servers:list = distribute_tasks(initial_loads, k)
    servers.reverse()
    desequilibre = calculate_imbalance(servers)
    return servers,desequilibre 

print("Entre le nomber des servers:")
N = int(input())
print("le nombre de travaux à planifier:")
K = int(input())
charges = []
for i in range(N):
   print("enter la charge:")
   charge = int(input())
   charges.append(charge) 

distrubutionFinal,desequilibre = load_balance(N,charges,K)
print("Distrubution final des charges:",distrubutionFinal)
print("Distrubution final des charges:",desequilibre)

