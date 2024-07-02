# Micropython: NO.6
# Juego del ahorcado
import random
def word_selector (*args):
    return random.choice(args)
words = [
    "abundancia", "accesorio", "actividad", "acuario", "admirable", "adolescente", "advertencia", "afortunado", "agradable", "agricultura",
    "albahaca", "alcachofa", "alegría", "alfabeto", "alimento", "alquiler", "amabilidad", "análisis", "aniversario", "anónimo",
    "antropología", "apreciar", "aprender", "aprobación", "arácnido", "arcoíris", "aromático", "arquitectura", "articulación", "asombroso",
    "astronomía", "atardecer", "aterrizar", "atleta", "atmósfera", "auditorio", "autobús", "aventura", "avión", "bailarina",
    "belleza", "biblioteca", "biodiversidad", "brillante", "cálido", "callejón", "caminante", "campamento", "canción", "candidato",
    "característica", "catástrofe", "celebración", "ceremonia", "científico", "circuito", "circunstancia", "clásico", "clorofila", "cocinero",
    "coherente", "colectivo", "colibrí", "colisión", "combinación", "comedia", "compañero", "competencia", "complejidad", "comunicación",
    "conferencia", "confianza", "conmovedor", "consecuencia", "construcción", "contemplar", "contenido", "continente", "corazón", "creatividad",
    "cuidadoso", "curiosidad", "debilidad", "declaración", "definición", "delicado", "democracia", "desarrollar", "descubrimiento", "desigualdad",
    "determinación", "dificultad", "dinámico", "dinosaurio", "discusión", "diseñar", "distinguido", "diversidad", "ecología", "educación",
    "eficiencia", "elaboración", "eléctrico", "elegante", "elocuencia", "emoción", "encantador", "enciclopedia", "energía", "enigmático",
    "entusiasmo", "equilibrio", "escenario", "escritor", "espectáculo", "esperanza", "estudiante", "eternidad", "evidencia", "exagerado",
    "excelencia", "experiencia", "extraordinario", "fascinante", "filosofía", "fotografía", "fragancia", "fuego", "función", "generosidad",
    "glaciar", "gratitud", "hábito", "habilidad", "helicóptero", "heroína", "historia", "hogar", "horizontal", "hospitalidad",
    "idea", "identidad", "ilusión", "imaginación", "impresionante", "incidente", "increíble", "independencia", "información", "inmensidad",
    "innovación", "inspiración", "inteligencia", "interesante", "invierno", "investigación", "jardinería", "justicia", "laboratorio", "libertad"
]

def word_length(length_word):
    display_word = "-" * len(length_word)
    return print (display_word)


def player_life():
    life = ' ❤️ '
    player_healt = life * 6
    return player_healt

def word_selected (selected_word, guessed_letter):
    display = ""
    for letter in selected_word:
        if letter in guessed_letter:
            display += letter
        else:
            display += "-"
    return display

def letter_hit (selected_word, player_health, guesseds_letter):
    while len(player_health) > 0:
        display = word_selected(selected_word, guesseds_letter)
        print(f"Palabra: {display}")
        print(f"Vidas: {' '.join(player_health)}")

        if '-' not in display:
            print("¡Felicidades! ¡Ganaste!")
            return

        letter_guess = input("Adivina una letra: ").lower()

        if letter_guess in guesseds_letter:
            print("Ya adivinaste esa letra")
            continue

        guesseds_letter.append(letter_guess)

        if letter_guess in selected_word:
            print(f"¡Adivinaste! {letter_guess} está en la palabra")
        else:
            player_health.pop()
            print(f"¡Fallaste! {letter_guess} no está en la palabra")

    print(f"¡Oh no! Te quedaste sin vidas. La palabra era: '{selected_word}'!")

selected_word = word_selector(*words)
player_health = player_life()
guesseds_letter = []
print("¡Bienvenido al juego del ahorcado!")
letter_hit(selected_word, player_health, guesseds_letter)
