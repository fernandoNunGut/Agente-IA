# Agente-IA

1. Definición del problema y entorno

El agente debe simular un asistente médico básico que, en base a síntomas que el paciente ingrese, entregue un diagnóstico preliminar o una recomendación médica inicial.
Ejemplo de entorno:
El usuario (paciente) introduce síntomas: fiebre, tos, dolor de cabeza, dolor abdominal, etc.
El agente analiza los síntomas con sus reglas y devuelve un diagnóstico probable: gripe, resfriado común, migraña, indigestión, etc.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

2. Definición PEAS

Performance (Medida de desempeño): porcentaje de diagnósticos correctos respecto a un conjunto de casos simulados, rapidez de respuesta, claridad de la recomendación.
Environment (Entorno): pacientes virtuales que entregan síntomas.
Actuators (Actuadores): salida de texto con diagnóstico y recomendación.
Sensors (Sensores): entrada de texto con síntomas.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

3. Tipos de agente
Usaremos un Agente Reflexivo Basado en Reglas:
- Es simple de programar.
- Usa condiciones del tipo "si -> sintoma -> estonces -> diasnogtico".
- Cumple con lo pedido en la tarea.

Ejemplos:
if "fiebre" in sintomas and "tos" in sintomas:
  return "Posible gripe"
elif "dolor de cabeza" in sintomas and "nauseas" in sintomas:
  return "posible migraña"
elif "dolor abdominal" in sintoma and "diarrea" in sintomas:
  return " Posible indigestion"
else:
return "consulta medica recomendada"

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

4. Ejemplo de interacción
  usuario: tengo fiebre y tos
  Agente: Diagnostico Pronblable: Gripe, Se recomienda reposo, hidratacion y consultar a un medico si los sintomas persisten.

  Usuario: Me duele la cabeza y tengo náuseas
  Agente: Diagnostico problable: Migraña. Evite la luz fuerte, descanse y consulte a un médico si los síntomas son severos.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

5. Reflexion sobre el desempeño y mejoras
   - El agenete funciona bien con casos simples, pero es limitado porque solo responde a las reglas predefinidas.
   - Mejoras futuras:
       - Integrar un modelo de ML para clasificar sintomas.
       - Usar un enfoque basado en objetos ( por ejemplo, recomendar examenes o pasos a segir).
       - Incorporar un historial de síntomas para decisiones mas personalizadas.
    
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
