def diagnostico_objetivo():
    """
    Agente de diagnóstico basado en objetivos.
    La interacción es guiada con preguntas de 'sí' o 'no' hasta cumplir el objetivo:
    entregar un diagnóstico probable al usuario.
    """

    print("=== Agente de Diagnóstico Médico (Basado en Objetivos) ===")
    print("Responda 'sí' o 'no' a las preguntas.")
    print("Escriba 'salir' para terminar en cualquier momento.")
    print("----------------------------------------------------------\n")

    objetivo = "dar un diagnóstico probable"
    sintomas = []

    # Lista de preguntas para alcanzar el objetivo
    preguntas = [
        ("¿Tiene fiebre?", "fiebre"),
        ("¿Tiene tos?", "tos"),
        ("¿Le duele la cabeza?", "dolor de cabeza"),
        ("¿Siente náuseas o mareo?", "náuseas"),
        ("¿Tiene dolor abdominal?", "dolor abdominal"),
        ("¿Ha tenido diarrea?", "diarrea"),
        ("¿Está con la nariz tapada o congestión?", "congestión"),
        ("¿Ha tenido estornudos frecuentes?", "estornudos"),
    ]

    # Reglas de diagnóstico (objetivos secundarios)
    reglas = {
        frozenset(["fiebre", "tos"]): "Posible gripe. Reposo, hidratación y control médico si persiste.",
        frozenset(["dolor de cabeza", "náuseas"]): "Posible migraña. Evite la luz fuerte y descanse.",
        frozenset(["dolor abdominal", "diarrea"]): "Posible indigestión. Tome líquidos y evite comidas pesadas.",
        frozenset(["estornudos", "congestión"]): "Posible resfriado común. Descanse e hidrate.",
        frozenset(["fiebre"]): "Puede ser inicio de una infección. Controle temperatura y manténgase hidratado.",
        frozenset(["tos"]): "Podría tratarse de irritación o resfriado. Vigile si persiste.",
        frozenset(["dolor de cabeza"]): "Puede ser estrés o fatiga. Descanse y beba agua."
    }

    # Hacer preguntas secuenciales
    for pregunta, sintoma in preguntas:
        respuesta = input(pregunta + " ").strip().lower()

        if respuesta == "salir":
            print("Agente finalizado. ¡Cuídese!")
            return

        if respuesta == "sí":
            sintomas.append(sintoma)

        # Verificar si ya se puede alcanzar el objetivo (algún diagnóstico)
        for clave, diag in reglas.items():
            if clave.issubset(sintomas):
                print("\n✅ Diagnóstico alcanzado:", diag)
                print("Síntomas detectados:", ", ".join(sintomas))
                print("Objetivo cumplido:", objetivo)
                return

    # Si terminó sin cumplir objetivo claro
    if sintomas:
        print("\nSe detectaron los síntomas:", ", ".join(sintomas))
        print("No se alcanzó un diagnóstico único. Consulte a un médico para mayor precisión.")
    else:
        print("\nNo se detectaron síntomas. Intente nuevamente.")


# Ejecución del programa
if __name__ == "__main__":
    diagnostico_objetivo()