#2. Implemente un programa para convertir un número decimal a hexadecimal
#ejm. el número 8642 en forma hexadecimal es: 21C2#def decimal_a_hexadecimal(decimal)
def convertir_a_hexadecimal(valor):
    valor =str (valor)
    equivalencias = { "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",}
    if valor  in equivalencias:
        return equivalencias[valor]
    else:
        return valor 
print(convertir_a_hexadecimal(15))
