'''
  Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información: cantidad total de
  preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente. Se pide confeccionar un programa
  que ingrese los dos datos por teclado e informe el nivel del mismo según el porcentaje de respuestas correctas que ha
  obtenido, y sabiendo que:

  Nivel máximo: Porcentaje >= 90%.
	Nivel medio: Porcentaje >= 75% y < 90%.
	Nivel regular: Porcentaje >= 50% y < 75%.
	Fuera de nivel: Porcentaje < 50%
'''

preguntas_realizadas = int(input('Preguntas Realizadas: '))
preguntas_correctas = int(input('Preguntas Correctas: '))

porcentaje_aciertos = (preguntas_correctas / preguntas_realizadas) * 100

if porcentaje_aciertos >= 90:
    # Con esta notación, mostraremos los decimales con DOS CIFRAS
    print(f'{porcentaje_aciertos:.2f}% acertado: nivel MÁXIMO')
elif porcentaje_aciertos >= 75 and porcentaje_aciertos < 90:
    print(f'{porcentaje_aciertos:.2f}% acertado: nivel MEDIO')
elif porcentaje_aciertos >= 50 and porcentaje_aciertos < 75:
    print(f'{porcentaje_aciertos:.2f}% acertado: nivel REGULAR')
elif porcentaje_aciertos < 50:
    print(f'{porcentaje_aciertos:.2f}% acertado: FUERA DE NIVEL')
