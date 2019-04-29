a=int(input('Masukkan angka :'))
x=[]
if type(a)==int:
    x.append('Bulat')
    if a>=0:
        x.append('Cacah')
        if a!=0:
            x.append('Asli')
            if a%2==0:
                x.append('Genap')
                if a==2:
                    x.append('Prima')
                else:
                    x.append('Komposit')  
                
            else:
                x.append('Ganjil')
                for i  in range (2,a):
                    if a%i!=0:
                        i+=1
                        if i>a-1:
                            x.append('Prima')
                    else :
                        x.append('Komposit')
                        break
                  
        else:
            x.append('Nol')

    else :
        x.append('Negatif')
else:
    print('Karakter yang anda masukkan bukan angka')
print(x)