horas_trabajadas = 48
tarifa_por_hora = 5000
porcentaje_retencion = 12.5


salario_bruto = horas_trabajadas * tarifa_por_hora

retencion_fuente = salario_bruto * porcentaje_retencion / 100

salario_neto = salario_bruto - retencion_fuente
print("Cálculo de salario de un empleado")
print("--")
print(f"Horas trabajadas: {round(horas_trabajadas, 2)} horas")
print(f"Tarifa por hora: ${tarifa_por_hora}")
print(f"Salario bruto: ${salario_bruto}")
print(f"Porcentaje de retención: {porcentaje_retencion}%")
print(f"Retención en la fuente: ${round(retencion_fuente)}")
print(f"Salario neto: ${round(salario_neto)}")
