import random

minus= "abcdefghijklmnopqrstuvwxyz"
mayus=minus.upper()
numeros="0123456789"
simbolos= "@()[]{}*,;/-_¿?.¡!$<#>&+%=€"
base=minus+mayus+numeros
longitud=12

muestra=random.sample (base, longitud)

password="".join(muestra)
print(password)