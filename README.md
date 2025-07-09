# Automatización de Mensajes de WhatsApp con Python

Este script permite enviar mensajes de WhatsApp de forma automática y personalizada a una lista de contactos almacenada en un archivo Excel. Utiliza la biblioteca `pywhatkit` junto con `pandas` para procesar y automatizar el flujo de trabajo.

---

## Características

- Lee un archivo Excel (`numeros.xlsx`) con columnas `NOMBRE` y `TELEFONO`.
- Extrae el primer nombre del campo `NOMBRE` para personalizar el mensaje.
- Agrega automáticamente el prefijo internacional colombiano `+57` a los números que no lo tengan.
- Envía mensajes personalizados con tu firma e información institucional.
- Define un intervalo entre envíos para evitar bloqueos por actividad sospechosa.
- Imprime logs de éxito o error por cada intento de envío.

---

## Requisitos

- Python 3.8 o superior
- Navegador Google Chrome (predeterminado)
- Cuenta activa de WhatsApp vinculada a WhatsApp Web

---

## Instalación

1. Clona este repositorio o descarga el script.
2. Instala las dependencias necesarias:

```bash
pip install pywhatkit pandas openpyxl
```

3. Asegúrate de tener un archivo llamado `numeros.xlsx` con al menos las siguientes columnas:

| NOMBRE           | TELEFONO    |
|------------------|-------------|
| De la Hoz Luisa  | 3001234567  |
| Del Río Juan     | 3207654321  |

Puedes crear este archivo con Excel o Google Sheets, asegurándote de que el nombre de la hoja sea `"Hoja1"` (o modificar el script si usas otro nombre).

---

## Uso

Al ejecutar el script:

- Se abrirá WhatsApp Web en el navegador.
- Escanea el código QR con tu celular si es necesario.
- El mensaje será enviado automáticamente.
- Se espera 15 segundos entre cada mensaje (puedes modificarlo en el parámetro `intervalo`).

---

## Formato del Mensaje

El mensaje enviado tiene un tono cordial e institucional, como el siguiente:

```
¡Hola Luisa, buen día! ☀️

Te escribe Eduardo Pimienta Leon de la Universidad Americana. 🎓

Para mí es un placer contactarte y ofrecerte mi asistencia para finalizar
el proceso de matrícula con la Institución. ✨

Luego de revisar nuestro sistema, me gustaría saber si ya tienes una fecha proyectada
para realizar tu matrícula o si ha surgido algún inconveniente que te lo impida. 📆

Estoy aquí para ayudarte y facilitar este proceso. No dudes en contarme si necesitas apoyo en algo. 🤝

Quedo atento a tu amable respuesta y te deseo un feliz día. 🌟

Eduardo Pimienta Leon  
Universidad Americana
```

Este mensaje puede personalizarse en el script directamente en la sección donde se define la variable `mensaje`.

---

## Posibles Problemas

### El mensaje no se envía

- Asegúrate de estar conectado a Internet.
- WhatsApp Web debe estar abierto y con sesión iniciada.
- Algunos navegadores no soportan correctamente la automatización (usa preferiblemente Chrome).

### Formato de número incorrecto

- Verifica que los números telefónicos no contengan espacios, guiones ni paréntesis.
- Si no tienen `+57`, el script lo agrega automáticamente.

### Tiempo de espera insuficiente

- Si el sistema es lento o la conexión es débil, incrementa el valor de `wait_time` o `intervalo` en el script.

### Bloqueo por actividad sospechosa

- WhatsApp puede limitar el número de mensajes enviados seguidos.  
  Se recomienda no enviar cientos de mensajes en un solo lote sin intervalos prolongados.

### Error en el nombre

- El script intenta manejar casos como “De la Hoz” o “Del Río”,  
  pero puede fallar en estructuras de nombres no comunes. Revísalos manualmente si es crítico.

---

## Personalización

Puedes modificar fácilmente el contenido del mensaje, cambiar el remitente o ajustar el tiempo de espera entre mensajes editando las siguientes líneas del script:

```python
intervalo = 15  # segundos entre mensajes
wait_time = 15  # segundos de espera para cargar el chat
```

También puedes cambiar el cuerpo del mensaje para ajustarlo a otros contextos (eventos, recordatorios, encuestas, promociones, etc.).

---

## Plantilla del archivo `numeros.xlsx`

Aquí tienes un ejemplo del contenido mínimo que debes incluir en tu archivo Excel (`numeros.xlsx`):

| NOMBRE           | TELEFONO     |
|------------------|--------------|
| De la Hoz Luisa  | 3001234567   |
| Del Río Juan     | 3207654321   |
| Camargo Sandra   | +573003332222 |
| González Carlos  | 3011111111   |

> Asegúrate de que los nombres de las columnas estén escritos exactamente como `NOMBRE` y `TELEFONO`, sin espacios extras.

---

## Autor

**Eduardo Pimienta Leon**  
Docente | Universidad Americana  
📧 eduardopimienta@americana.edu.co
