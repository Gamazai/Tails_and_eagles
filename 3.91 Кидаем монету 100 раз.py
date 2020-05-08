#Кидаем монету 100 раз
broski = int(input("Сколько раз вы хотите кинуть монету? :: "))
print ("\tСейчас мы кинем монету", broski, "раз и узнаем сколько выпало орлов и решек")
import random
tails=0
eagles=0
cast=0
attempt=0


while attempt < broski:
    cast=random.randint(1,2)
    #print(cast)
    if cast == 1:
        print(attempt+1, ": Решка")
        tails +=1
    if cast==2:
        print(attempt+1, ": Орёл")
        eagles +=1

    attempt += 1

Dolia_tails = tails/broski
Dolia_eagles = eagles/broski

print("Мы кинули монету", broski, " раз и у нас выпало", "Решек: ", tails, "Орлов: ",
eagles)

print("Решка:", Dolia_tails*100, "%")
print("Орёл:", Dolia_eagles*100, "%")


input("\n\n")
