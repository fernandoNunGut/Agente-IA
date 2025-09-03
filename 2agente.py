# Agente de Diagnóstico Médico Básico con sinónimos
# Lenguaje: Python
# Tipo de agente: Reflexivo basado en reglas
# Autores: Bastian Burgos, Fernando Núñez, Matias Jara

def diagnostico(texto_usuario):
    """
    Recibe un texto libre del usuario y devuelve un diagnóstico básico
    basado en palabras clave detectadas (incluyendo sinónimos).
    """
    texto_usuario = texto_usuario.lower()

    # Diccionario de sinónimos -> síntoma "oficial"
    sinonimos = {
        "dolor de guata": "dolor abdominal",
        "dolor de estómago": "dolor abdominal",
        "gripe": "fiebre",
        "resfrío": "estornudos",
        "resfriado": "estornudos",
        "cabeza me late": "dolor de cabeza",
        "mareo": "náuseas",
        "congestionado": "congestión",
        "nariz tapada": "congestión"
    }

    # Lista de síntomas clave oficiales
    sintomas_clave = [
        "fiebre", "tos", "dolor de cabeza", "náuseas", 
        "dolor abdominal", "diarrea", "estornudos", "congestión"
    ]

    # Normalizar el texto sustituyendo sinónimos
    for sinonimo, sintoma_real in sinonimos.items():
        if sinonimo in texto_usuario:
            texto_usuario = texto_usuario.replace(sinonimo, sintoma_real)

    # Buscar síntomas detectados
    sintomas_detectados = [s for s in sintomas_clave if s in texto_usuario]

    if not sintomas_detectados:
        return "No se detectaron síntomas reconocidos. Intente describirlos de otra forma."

    # Reglas del agente
    reglas = {
        frozenset(["fiebre", "tos"]): "Posible gripe. Reposo, hidratación y consulta médica si los síntomas persisten.",
        frozenset(["dolor de cabeza", "náuseas"]): "Posible migraña. Evite la luz fuerte y descanse.",
        frozenset(["dolor abdominal", "diarrea"]): "Posible indigestión. Tome líquidos y evite comidas pesadas.",
        frozenset(["estornudos", "congestión"]): "Posible resfriado común. Descanse e hidrate.",
        frozenset(["fiebre"]): "Puede ser el inicio de una infección. Controle su temperatura y manténgase hidratado.",
        frozenset(["tos"]): "Puede tratarse de una irritación o resfriado. Vigile si persiste.",
        frozenset(["dolor de cabeza"]): "Puede ser estrés o fatiga. Descanse y manténgase hidratado."
    }

    # Buscar coincidencias exactas de reglas
    for clave, respuesta in reglas.items():
        if clave.issubset(sintomas_detectados):
            return respuesta

    # Si no hay coincidencia exacta
    return f"Se detectaron los síntomas: {', '.join(sintomas_detectados)}. Consulte a un médico para mayor precisión."


def menu():
    print("=== Agente de Diagnóstico Médico Básico ===")
    print("Describa sus síntomas en una frase (ej: Tengo tos y dolor de guata).")
    print("Escriba 'salir' para terminar.")
    print("--------------------------------------------")

    while True:
        entrada = input("\nSíntomas: ")

        if entrada.lower() == "salir":
            print("Agente finalizado. ¡Cuídese!")
            break

        resultado = diagnostico(entrada)
        print("Diagnóstico:", resultado)


# Ejecución del programa
if __name__ == "__main__":
    menu()
