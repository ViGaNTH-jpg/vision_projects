# Este programa pide al usuario una cantidad en pesos mexicanos
# Tambien pide el porcentaje de iva y el porcentaje de propina
# El programa debe calcular el monto total a pagar por el usuario

subtotal = input("Subtotal(MXN)")
iva_txt = input("IVA(%) ej. 16: ")
propina_txt = input("Propina(%) ej. 10: ")

try

    # Metodo built team float - Convierte a un dato del tipo flotante
    subtotal = float (subtotal_txt)
    iva = float(iva_txt)
    propina = float(propina_txt)/100

except ValueError

    print("Entrada invalida, utiliza numeros webn")

monto_iva = subtotal*iva
monto_propina = subtotal*propina
total = subtotal+monto_propina+monto_iva

print("subtotal: {subtotal}")
print(f"IVA: {monto_iva}")
print(f"propina: {monto_propina}")
pritn(f"")

