def diagnostico_objetivo():
    """
    Agente de diagnóstico basado en objetivos.
    Hace todas las preguntas primero y luego evalúa los síntomas detectados
    para entregar el/los posibles diagnósticos.
    """

    print("---------------------------------------------------------------------------------------|")
    print("============= Agente de Diagnóstico Médico (Basado en Objetivos) ======================|")
    print("Responda con 'sí' o 'no'.                                                              |")
    print("Escriba 'salir' para terminar en cualquier momento.                                    |")
    print("---------------------------------------------------------------------------------------|\n")

    objetivo = "dar un diagnóstico probable"
    sintomas = []

    Ask = [
        ("Tiene fiebre?", "fiebre"),
        ("Tiene tos?", "tos"),
        ("Le duele la cabeza?", "dolor de cabeza"),
        ("Siente náuseas o mareo?", "náuseas"),
        ("Tiene dolor abdominal?", "dolor abdominal"),
        ("Ha tenido diarrea?", "diarrea"),
        ("Está con la nariz tapada o congestión?", "congestión"),
        ("Ha tenido estornudos frecuentes?", "estornudos"),
    ]

    reglamento = {
        frozenset(["fiebre", "tos"]): "Posible gripe. Reposo, hidratación y control médico si persiste.",
        frozenset(["dolor de cabeza", "náuseas"]): "Posible migraña. Evite la luz fuerte y descanse.",
        frozenset(["dolor abdominal", "diarrea"]): "Posible indigestión. Tome líquidos y evite comidas pesadas.",
        frozenset(["estornudos", "congestión"]): "Posible resfriado común. Descanse e hidrate.",
        frozenset(["fiebre"]): "Puede ser inicio de una infección. Controle temperatura y manténgase hidratado.",
        frozenset(["tos"]): "Podría tratarse de irritación o resfriado. Vigile si persiste.",
        frozenset(["dolor de cabeza"]): "Puede ser estrés o fatiga. Descanse y beba agua."
    }

    # Ciclo while que hace todas las preguntas primero
    i = 0
    while i < len(Ask):
        pregunta, sintoma = Ask[i]
        respuesta = input(pregunta + " ").strip().lower()

        if "salir" in respuesta:
            print("Agente finalizado. ¡Cuídese!")
            return

        if "si" in respuesta or "sí" in respuesta or "yes" in respuesta or "SI" in respuesta or "Si" in respuesta or "Sí" in respuesta:
            sintomas.append(sintoma)
        elif "no" in respuesta or "NO" in respuesta or "No" in respuesta:
            pass  # no hace nada
        else:
            print("Respuesta no reconocida, se tomará como 'no'.")
        
        i += 1  # pasar a la siguiente pregunta

    # Una vez terminadas todas las preguntas → evaluar diagnósticos
    diagnosticos = []
    for clave, diag in reglamento.items():
        if clave.issubset(sintomas):
            diagnosticos.append(diag)

    # Mostrar resultados finales
    if diagnosticos:
        print("\n✅ Diagnósticos alcanzados:")
        for d in diagnosticos:
            print(" -", d)
        print("Síntomas detectados:", ", ".join(sintomas))
        print("Objetivo cumplido:", objetivo)
    elif sintomas:
        print("\nSe detectaron los síntomas:", ", ".join(sintomas))
        print("No se alcanzó un diagnóstico único. Consulte a un médico para mayor precisión.")
    else:
        print("\nNo se detectaron síntomas. Intente nuevamente.(Posible estado de salud = Saludable )")


# Ejecución del programa
if __name__ == "__main__":
    diagnostico_objetivo()