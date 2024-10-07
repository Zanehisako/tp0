Notes=[15,13,5,11,5,14,9,6,14,1,8,8,11,3,12,11,2,17,14,1,6,12,13,14,1]

#question 1
Notes_float = list(map(float,Notes))

print(Notes_float)

#question 2
def Moyen(notes:list):
    moyen = 0
    for i in notes:
        moyen += i
    return moyen / len(notes)
            
moyen = Moyen(Notes_float)
print("le resultat attendu:",moyen)

#question 3
def Variance(moyen:float,notes:list):
   moyens = []
   for i in notes:
      moyens.append((i - moyen)*(i - moyen)) 
   return Moyen(moyens)

print("la variance:",Variance(moyen,Notes_float))

#question 4
def Occurance(notes:list):
    #we turn the list into a set ie a list with no duplicates,notes.count is a methode objet so it called the methode on all the list members
    return max(set(notes),key=notes.count)
print(Occurance(Notes_float))

#question 5
def Sort(arr:list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#question 6
def Unique(arr:list):
    return list(set(arr))
Notes_float = Unique(Notes_float)
print("the sorted List:")
print(Notes_float)
