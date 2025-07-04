import pywhatkit as kit
import pandas as pd
import time

# 📂 Cargar el archivo Excel
archivo_excel = "numeros.xlsx"  # Asegúrate de que el archivo tiene este nombre
hoja = "Hoja1"  # Modificar si la hoja tiene otro nombre

# 📖 Leer el archivo y obtener los datos
df = pd.read_excel(archivo_excel, sheet_name=hoja, engine="openpyxl")

# 📌 Verificar nombres de columnas
df.columns = df.columns.str.strip()  # Eliminar espacios en los nombres de columnas

# Listas para almacenar nombres y números procesados
nombres_procesados = []
numeros = []

# 📌 Función mejorada para extraer el primer nombre correctamente
def extraer_nombre(nombre_completo):
    partes = nombre_completo.split()
    
    # Si el nombre inicia con "De la", "De los", "Del", etc., ignoramos eso y tomamos la siguiente palabra
    if partes[0].lower() in ["de", "del"]:
        return partes[2] if len(partes) > 2 else partes[1]  # Tomar el siguiente término
    elif partes[0].lower() == "de" and partes[1].lower() == "la":
        return partes[3] if len(partes) > 3 else partes[2]  # Casos como "De la Hoz Luisa"
    else:
        return partes[1] if len(partes) > 1 else partes[0]  # Tomar el primer nombre real

# 📌 Procesar cada fila del archivo
for _, row in df.iterrows():
    nombre_completo = str(row["NOMBRE"]).strip()
    numero = str(row["TELEFONO"]).strip()

    # Extraer el nombre correcto
    nombre = extraer_nombre(nombre_completo)

    # Agregar el prefijo internacional de Colombia si no lo tiene
    numero = numero if numero.startswith("+57") else f"+57{numero}"

    # Guardar en listas
    nombres_procesados.append(nombre)
    numeros.append(numero)

# ⏳ Intervalo de tiempo entre mensajes (segundos)
intervalo = 15  

# 📩 Enviar mensajes personalizados
for nombre, numero in zip(nombres_procesados, numeros):
    try:
        # ✉️ Mensaje personalizado
        mensaje = (f"¡Hola {nombre}, buen día! ☀️\n\n"
                   "Te escribe *Eduardo Pimienta Leon* de la *Universidad Americana*. 🎓\n\n"
                   "Para mí es un placer contactarte y ofrecerte mi asistencia para finalizar "
                   "el proceso de matrícula con la Institución. ✨\n\n"
                   "Luego de revisar nuestro sistema, me gustaría saber si ya tienes una fecha proyectada "
                   "para realizar tu matrícula o si ha surgido algún inconveniente que te lo impida. 📆\n\n"
                   "Estoy aquí para ayudarte y facilitar este proceso. No dudes en contarme si necesitas apoyo en algo. 🤝\n\n"
                   "Quedo atento a tu amable respuesta y te deseo un *feliz día*. 🌟\n\n"
                   "*Eduardo Pimienta Leon*\n"
                   "*Universidad Americana*")

        # 📲 Enviar mensaje a través de WhatsApp
        kit.sendwhatmsg_instantly(numero, mensaje, wait_time=15, tab_close=True)
        print(f"✅ Mensaje enviado a {nombre} ({numero})")
        
        # ⏳ Esperar antes de enviar el siguiente mensaje
        time.sleep(intervalo)

    except Exception as e:
        print(f"❌ Error enviando a {nombre} ({numero}): {e}")

print("✅ Todos los mensajes han sido enviados correctamente.")
