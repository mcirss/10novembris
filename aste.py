def lasit_datni():
    #PAjautāsim ievadit datnes  nosaukumu
    datnes_nosaukums=input("Ievadit datnes nosaukumu: ")
    try:
    #Kā ieladēt datnes saturu?
        with open(datnes_nosaukums,'r') as ff:
            saturs=ff.read()
            #print(saturs) pārliecinas par to ka datne ir skaitli>
            print(f"Simbolu skaits datnē ir {len(saturs)}")

            print(f"Pirmie desmit simboli ir:{saturs[:10]}")
    except FileNotFoundError:
        print("Datne nav atrasta!") 
    except ValueError:
        print("Datu kļūda!")
        #izvada pirmo un pedejo simbolu
        print(f"Īzvadi pirmo un pedejo simbolu: {saturs[0]} un {saturs[-1]}")



if __name__=="__main__":
    lasit_datni()