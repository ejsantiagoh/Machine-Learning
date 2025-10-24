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

# mensajes = [{"role": "system","content":system_rol}]

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self,polaridad):
        if polaridad > -0.8 and polaridad <=-0.3:
            return "\x1b[1;31m" + "Negativo" +"\x1b[0;37m"
        elif polaridad > -0.3 and polaridad <-0.1:
            return "\x1b[1;31m" + "Algo Negativo" +"\x1b[0;37m"
        elif polaridad >= -0.1 and polaridad <=0.1:
            return "\x1b[1;33m" + "Neutral" +"\x1b[0;37m"
        elif polaridad >= 0.1 and polaridad <=0.4:
            return "\x1b[1;32m" + "Algo positivo" +"\x1b[0;37m"
        elif polaridad >= 0.4 and polaridad <=0.9:
            return "\x1b[1;32m" + "Positivo" +"\x1b[0;37m"
        elif polaridad > 0.9:
            return "\x1b[1;32m" + "Muy Positivo" +"\x1b[0;37m"
        else: 
            return "\x1b[1;31m" + "Muy Negativo" +"\x1b[0;37m"
        
analizador = AnalizadorDeSentimientos()
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
