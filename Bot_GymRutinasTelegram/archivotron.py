
# archivotron.py

def busca_arreglo(mensaje):
    mensaje = mensaje.lower()

    rutinas = {
        "pecho": "🏋️ Rutina de Pecho:\n- Press banca 4x10\n- Press inclinado 4x12\n- Aperturas con mancuernas 4x15",
        "espalda": "🏋️ Rutina de Espalda:\n- Jalón al pecho 4x12\n- Remo con barra 4x10\n- Peso muerto 4x8",
        "piernas": "🏋️ Rutina de Piernas:\n- Sentadillas 4x10\n- Prensa 4x12\n- Extensiones de cuádriceps 4x15",
        "biceps": "💪 Rutina de Bíceps:\n- Curl con barra 4x12\n- Curl alterno 4x10\n- Curl martillo 4x12",
        "triceps": "💪 Rutina de Tríceps:\n- Press francés 4x10\n- Fondos 4x12\n- Patada de tríceps 4x12",
        "hombros": "🏋️ Rutina de Hombros:\n- Press militar 4x10\n- Elevaciones laterales 4x12\n- Pájaros 4x12",
    }

    for clave in rutinas:
        if clave in mensaje:
            return rutinas[clave]

    return "Lo siento, no entendí. Escribe 'pecho', 'espalda', 'piernas', 'biceps', 'triceps' o 'hombros'."
