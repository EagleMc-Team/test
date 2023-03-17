from numpy import array 

def Saisie1():
    ch = input("ch: ")
    while not (len(ch)>0 and 65<=ord(ch[0])<=90):
        ch = input("ch: ")
    return ch
def saisie2():
    n = -1
    while not 5<=n<=10:
        n = int(input("Donner N: "))
    return n
def remplir(T,chlen):
    for i in range(len(T)):
        chn = input("Donner N(chaine) dans T["+str(i)+"]: ")
        while not (len(chn) == chlen and 65<=ord(chn[0])<=90):
            chn = input("Donner N(chaine) dans T["+str(i)+"]: ")
        T[i] = chn
def commun(ch1,ch2):
    nb=0
    for i in range(len(ch1)):
        if ch1[i] == ch2[i]:
            nb = nb+1
    return nb
def affiche(ch1,T):
    for i in range(len(T)):
        s = (commun(ch1,T[i])/len(ch1) )* 100
        print("pour mot1 = ",ch1," et mot2 = ",T[i])
        print("le degré de ressemblance DR=(",(commun(ch1,T[i])) , "/",len(ch1),")*100 = ",s)

#-----------------------------------------

ch = Saisie1()
T = array([str]*saisie2())
remplir(T, len(ch))
affiche(ch,T)




#hiii
