import random

minus = "abcdefghijklmnñopqrstuvwxyz"
mayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numeros = "0123456789"

simbolos = "@$&#/)!?'*'"

miau = minus + mayus + numeros + simbolos

caracteres= 10
contra = "".join(random.sample(miau, caracteres))

print("Gracias por usar mi herramienta, te agradeceria que me siguieras en GitHub y otras redes. Si tienes alguna duda sobre algo de hacking ciber seguridad o algo más no dudes en hablarme por ig. Gracias por leer. Att: @R3Y  Tu contraseña es:", contra)
