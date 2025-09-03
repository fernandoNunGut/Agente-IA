
# Agente de Diagnóstico Médico Básico
# Lenguaje: Python
# Tipo de agente: Reflexivo basado en reglas
# Autores: Bastian Burgos, Fernando Núñez, Matias Jara


def diagnostico(sintomas):
    """
    Función principal del agente.
    Recibe una lista de síntomas y devuelve un diagnóstico básico.
    """
    # Normalizamos a minúsculas
    sintomas = [s.lower() for s in sintomas]

    # Reglas del agente
    if "fiebre" in sintomas and "tos" in sintomas:
        return "Posible gripe. Reposo, hidratación y consulta médica si los síntomas persisten."
    
    elif "dolor de cabeza" in sintomas and "náuseas" in sintomas:
        return "Posible migraña. Evite la luz fuerte y descanse."
    
    elif "dolor abdominal" in sintomas and "diarrea" in sintomas:
        return "Posible indigestión. Tome líquidos y evite comidas pesadas."
    
    elif "estornudos" in sintomas and "congestión" in sintomas:
        return "Posible resfriado común. Descanse e hidrate."
    
    else:
        return "No se puede determinar un diagnóstico claro. Consulte a un médico."

def menu():
    print("=== Agente de Diagnóstico Médico Básico ===")
    print("Ingrese los síntomas separados por comas (ej: fiebre, tos, dolor de cabeza).")
    print("Escriba 'salir' para terminar.")
    print("--------------------------------------------")

    while True:
        entrada = input("\nSíntomas: ")

        if entrada.lower() == "salir":
            print("Agente finalizado. ¡Cuídese!")
            break

        # Convertir la entrada en lista de síntomas
        sintomas = [s.strip() for s in entrada.split(",")]

        # Obtener diagnóstico
        resultado = diagnostico(sintomas)
        print("Diagnóstico:", resultado)

# Ejecución del programa
if __name__ == "__main__":
    menu()