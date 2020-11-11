# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca
#1.8 Adelantos
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
pago_inicial = 2684.11
adelanto=1000
total_pagado = 0.0
mes=0


while saldo > 0:
    
    if mes<12:
        pago_mensual=pago_inicial+adelanto
    else:
        pago_mensual=pago_inicial
    
    saldo = saldo * (1+tasa/12) - pago_mensual
    print(pago_mensual)
    total_pagado = total_pagado + pago_mensual
    mes=mes+1
    print(mes)
    

   
print('Total pagado', round(total_pagado, 2), 'Meses', mes)

#1.9 Calculadora de adelantos

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
pago_inicial = 2684.11
total_pagado = 0.0
mes=0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000


while saldo > 0:
    
    if mes>pago_extra_mes_comienzo and mes<pago_extra_mes_fin: 
        pago_mensual=pago_inicial+pago_extra
    else:
        pago_mensual=pago_inicial
    
    saldo = saldo * (1+tasa/12) - pago_mensual
    #print(pago_mensual)
    total_pagado = total_pagado + pago_mensual
    mes=mes+1
    

   
print('Total pagado', round(total_pagado, 2), 'Meses', mes)

#1.10 Tablas

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
pago_inicial = 2684.11
total_pagado = 0.0
mes=0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000


while saldo > 0:
    
    if mes>pago_extra_mes_comienzo and mes<pago_extra_mes_fin: 
        pago_mensual=pago_inicial+pago_extra
    else:
        pago_mensual=pago_inicial
    
    saldo = saldo * (1+tasa/12) - pago_mensual
    #print(pago_mensual)
    total_pagado = total_pagado + pago_mensual
    print(mes, round(total_pagado, 2), round(saldo,2))
    mes=mes+1
    

print('Total pagado:', round(total_pagado, 2))
print('Meses:', mes)

#1.11 Bonus



saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
pago_inicial = 2684.11
total_pagado = 0.0
mes=0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000


while saldo > 0:
    
    if mes>pago_extra_mes_comienzo and mes<pago_extra_mes_fin: 
        pago_mensual=pago_inicial+pago_extra
        
    elif pago_mensual>saldo:
        pago_mensual=saldo * (1+tasa/12)
        
    else:
        
        pago_mensual=pago_inicial
    
   
    saldo = saldo * (1+tasa/12) - pago_mensual
    
    #print(pago_mensual)
    
    total_pagado = total_pagado + pago_mensual
    
    print(mes, round(total_pagado, 2), round(saldo,2))
    
    mes=mes+1
    
#print('Total pagado:', round(total_pagado, 2))
#print('Meses:', mes)

print(f'Total pagado: {total_pagado} en {mes} meses')






