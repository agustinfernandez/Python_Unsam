frase= 'Todos somos programadores'
palabras=frase.split()

traduccion=''
for palabra in palabras:
    
    if palabra[-1] == 'o':
        traduccion=traduccion+' '+palabra[0:-1]+'e'
        
    elif palabra[-2] =='o':
        traduccion=traduccion+' '+palabra[0:-2]+'es'
    else:
        traduccion=traduccion+' '+palabra 
    
    
    
frase_t = traduccion 

print(frase_t)
