import nltk
from nltk.chat.util import Chat, reflections

# Definir patrones de entrada y respuestas correspondientes
pares = [
    [
        r"mi nombre es (.*)",
        [
            "Hola %1, ¿cómo estás?",
        ],
    ],
    [
        r"¿cuál es tu nombre\??",
        [
            "Mi nombre es Jarvis.",
        ],
    ],
    [
        r"¿cómo estás\??",
        [
            "Estoy bien, gracias.",
            "¡Muy bien! ¿Y tú?",
        ],
    ],
    [
        r"quit",
        [
            "Hasta luego. Fue un placer ayudarte.",
        ],
    ],
]


def chatbot():
    print("Hola, soy Jarvis. ¿En qué puedo ayudarte hoy?")
    chat = Chat(pares, reflections)
    chat.converse()


if __name__ == "__main__":
    chatbot()
