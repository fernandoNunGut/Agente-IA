# Agente-IA
1. Definición del problema y entorno

El agente debe simular un asistente médico básico que, en base a síntomas que el paciente ingrese, entregue un diagnóstico preliminar o una recomendación médica inicial.

Ejemplo de entorno:

El usuario (paciente) introduce síntomas: fiebre, tos, dolor de cabeza, dolor abdominal, etc.

El agente analiza los síntomas con sus reglas y devuelve un diagnóstico probable: gripe, resfriado común, migraña, indigestión, etc.

2. Definición PEAS

Performance (Medida de desempeño): porcentaje de diagnósticos correctos respecto a un conjunto de casos simulados, rapidez de respuesta, claridad de la recomendación.

Environment (Entorno): pacientes virtuales que entregan síntomas.

Actuators (Actuadores): salida de texto con diagnóstico y recomendación.

Sensors (Sensores): entrada de texto con síntomas.
