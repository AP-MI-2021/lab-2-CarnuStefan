'''
6. Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime. De exemplu, `233` este superprim,
 deoarece `2`, `23` și `233` sunt toate prime, dar `237` nu este superprim, deoarece `237` nu este prim. 
    - Funcția principală: `is_superprime(n) -> bool`
    - Funcția de test: `test_is_superprime()`
'''
def is_prime(n):
  if (n<2): return False
  for i in range(2,n//2):
      if(n%i==0):return False
  return True

def is_superprime(n):
    while (n):
        if is_prime(n)== False: return False
        n=n//10
    return True

def test_is_superprime():
    assert is_superprime(233) == True 
    assert is_superprime(237) == False

test_is_superprime()

'''
13. Transformă o temperatură dată într-o scară dată (`K`, `F` sau `C`) într-o altă scară dată. De exemplu: `300 K C` -> `26.85`.
    - Funcția principală: `get_temp(temp: float, from: str, to: str) -> float`
    - Funcția de test: `test_get_temp()`
'''

def get_temp(temp:float,fro:str,to:str):
    if (fro == "K")|(fro=="k"):
        if (to =="C")| (to=="c"):temp=temp-273.15
        if (to =="F")| (to=="f"):temp=(temp-273.15)*9/5+32
    if (fro == "C")|(fro=="c"):
        if (to =="K")| (to=="k"):temp=temp+273.15
        if (to =="F")| (to=="f"):temp=temp*9/5+32
    if (fro == "F")|(fro=="f"):
        if (to =="K")| (to=="k"):(temp-32)*5/9+273.15
        if (to =="C")| (to=="c"):(temp-32)*5/9
    return round(temp,2)

def test_get_temp():
    assert get_temp(300,"K","C")==26.85
    assert get_temp(0,"c","F")==32
    assert get_temp(273.15,"K","f")==32

test_get_temp()

'''
 Calculează combinări de `n` luate câte `k` (`n` și `k` date).
    - Funcția principală: `get_n_choose_k(n: int, k: int) -> int`
    - Funcția de test: `test_get_n_choose_k()`
'''
def get_n_choose_k(n:int,k:int):
    if(k>n):return None
    n_factorial=1
    k_factorial=1
    diferenta=n-k
    diferenta_factorial=1
    for i in range (1,n+1,1): 
        n_factorial=n_factorial*i
        print (i)
    for j in range (1,k+1,1): 
        k_factorial=k_factorial*j
        print(j)
    for l in range (1,diferenta+1,1):
        diferenta_factorial=diferenta_factorial*l
        print (l)
    combinare=n_factorial//(k_factorial*diferenta_factorial)
    return combinare

def test_get_n_choose_k():
   assert get_n_choose_k(52,5)==2598960
   assert get_n_choose_k(10,0)==1
   assert get_n_choose_k(234,1)==234
   assert get_n_choose_k(24,24)==1
   assert get_n_choose_k(2,345)==None

test_get_n_choose_k()

def main():
    while True:
        print("Meniu\n")
        print("Rulati Problema 6-Superprim: 1")
        print("Rulati Problema 13-Temperatura: 2")
        print("Rulati Problema 10-Combinari de n luate cate k: 3")
        print("Inchide:x \n")
        varianta=input('Alegeti optiunea:')

        if varianta=='1':
            nr=int(input("Introduceti numarul care trebuie verificat: "))
            if is_superprime(nr): print(f"Numarul {nr} este superprim \n")
            else: print(f"Numarul {nr} este superprim \n")
        elif varianta=='2':
            linie_date=input("Introduceti temperatura, unitatea de temperatura in care este reprezentata si unitatea de temperatura in care trebuie transformata: ")
            temp,gr1,gr2=linie_date.split(" ")
            temp= float(temp)
            print (get_temp(temp,gr1,gr2))
        elif varianta=='3':
            n=int(input("Introduceti n :"))
            k=int(input("Introduceti k :"))
            combinare=get_n_choose_k(n,k)
            print(f"Rezultatul combinarilor de {n} luate cate {k} este {combinare}")
        elif varianta=='x':break

if __name__ == '__main__':
    main()
