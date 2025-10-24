import google.generativeai as genai
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Leer la clave
api_key = os.getenv("GEMINI_API_KEY")

# Confirmar (opcional)
print("API Key cargada correctamente" if api_key else "Error: no se cargó la API Key")

# Asignar clave a la librería openai
genai.configure(api_key=api_key)
# genai.configure = api_key

system_rol = '''Haz de cuenta que es un analizador de sentimientos.
Yo le paso sentimientos y usted analiza el sentimiento de los mensajes y me das una respuesta con al menos un caracter y como maximo 4 caracteres SOLO RESPUESTA NUMÉRICAS.donde -1 es negatividad maxima, 0 es neutral y 1 es positividad maxima. (Puede responder solo con ints o floats)'''

# Crear el modelo de Gemini
model = genai.GenerativeModel("gemini-2.5-flash")

class Sentimiento:
    def __init__(self,nombre,color):
        self.nombre = nombre
        self.color = color
        
    def __str__(self):
        return  "\x1b[1;{}m{}\x1b[0;37m".format(self.color,self.nombre)
    


class AnalizadorDeSentimientos:
    def __init__(self,rangos):
        self.rangos = rangos
        
    def analizar_sentimiento(self,polaridad):
        for rango, sentimiento in self.rangos:
            if rango[0] < polaridad <= rango [1]:
                return sentimiento
        return Sentimiento ("Muy Negativo","31")

rangos = [
    ((-0.6,-0.3), Sentimiento ("Negativo","31")),
    ((-0.3,-0.1), Sentimiento ("Algo negativo","31")),
    ((-0.1,0.1), Sentimiento ("Neutral","33")),
    ((0.1,0.4), Sentimiento ("Algo positivo","32")),
    ((0.4,0.9), Sentimiento ("Positivo","32")),
    ((0.9,1), Sentimiento ("Muy positivo","32"))
]
        
        
analizador = AnalizadorDeSentimientos(rangos)
# resultado = analizador.analizar_sentimiento(0.95)
# print(resultado)

while True:
    user_prompt = input("\x1b[1;33m" + "\nDigame algo: " +"\x1b[0;37m")
    
    # Unir la instrucción del sistema con la entrada del usuario
    prompt_completo = f"{system_rol}\nTexto: {user_prompt}"

    # Generar la respuesta de Gemini
    respuesta = model.generate_content(prompt_completo).text.strip()

    try:
        # Convertir a número
        sentimiento = analizador.analizar_sentimiento(float(respuesta))
        print(sentimiento)
    except ValueError:
        print("\x1b[1;31m" + f"Respuesta inválida del modelo: {respuesta}" + "\x1b[0;37m")