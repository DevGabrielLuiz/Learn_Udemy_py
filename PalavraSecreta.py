palavra_secreta = 'arroz'
palavra_digitada = f'{'*'*len(palavra_secreta)}'
letra=0
print(palavra_digitada)
while len(palavra_secreta)!=len(palavra_digitada) :
    palavra_digitada=input('Digite uma letra') 
    if letra in palavra_secreta:
        palavra_digitada+=palavra_secreta[letra]
    
    print(f'{palavra_digitada}')
    pass