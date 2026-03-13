# 📚 LibraryQuoteBot – Discord Bot de Fragmentos de Libros

LibraryQuoteBot es un bot de Discord que busca **libros reales en internet** y extrae **fragmentos aleatorios** para compartirlos en un servidor.

El bot utiliza libros de dominio público disponibles en **Project Gutenberg** y la API de **Gutendex** para buscar textos automáticamente.

Con este bot puedes explorar literatura, ciencia, filosofía y muchos otros temas directamente desde Discord.

---

# ✨ Características

* 📚 Busca libros en internet por tema
* 🔎 Descarga textos completos de dominio público
* 🎲 Extrae fragmentos aleatorios de los libros
* 💬 Envía los fragmentos en formato embed en Discord
* ⚡ Funciona con comandos simples

---

# 🧰 Tecnologías utilizadas

Este proyecto utiliza las siguientes librerías y servicios:

### Python

* **discord.py**
  Librería para crear bots de Discord y manejar eventos y comandos.

* **requests**
  Permite hacer solicitudes HTTP para descargar datos desde internet.

* **python-dotenv**
  Permite cargar variables de entorno desde un archivo `.env`.

### APIs

* **Gutendex API**
  API pública que permite buscar libros disponibles en Project Gutenberg.

* **Project Gutenberg**
  Biblioteca digital con más de 70,000 libros de dominio público.

---

# 📦 Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/Almarm-r/creazybook.git
cd creazybook
```

---

## 2. Crear entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
```

Activar entorno virtual:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3. Instalar dependencias

```bash
pip install discord.py requests python-dotenv
```

---

# 🔑 Configuración del Bot

## 1. Crear una aplicación en Discord

Ir al portal de desarrolladores:

https://discord.com/developers/applications

1. Crear una nueva aplicación
2. Ir a la sección **Bot**
3. Crear un bot
4. Copiar el **Token**

---

## 2. Crear archivo `.env`

En la carpeta del proyecto crear un archivo llamado:

```
.env
```

Contenido:

```
DISCORD_TOKEN=tu_token_aqui
```

---

# ▶️ Ejecutar el bot

En la terminal:

```bash
python bot.py
```

Si todo funciona correctamente aparecerá:

```
Bot conectado como NombreDelBot
```

---

# 💬 Comandos disponibles

## !buscar

Busca un libro en internet relacionado con el tema indicado y devuelve un fragmento aleatorio.

Ejemplo:

```
!buscar universe
```

El bot buscará libros relacionados con el universo y mostrará un párrafo del texto.

---

### Otros ejemplos

```
!buscar physics
!buscar philosophy
!buscar astronomy
!buscar love
```

---

# ⚙️ Cómo funciona el bot

El proceso interno es el siguiente:

1. El usuario escribe un comando en Discord

```
!buscar astronomy
```

2. El bot envía una solicitud a la **Gutendex API**

```
https://gutendex.com/books/?search=astronomy
```

3. La API devuelve una lista de libros.

4. El bot selecciona uno al azar.

5. Descarga el archivo de texto del libro.

6. Divide el texto en párrafos.

7. Selecciona un fragmento aleatorio.

8. Envía el fragmento al canal de Discord.

---

# 📂 Estructura del proyecto

```
library-quote-bot
│
├── bot.py
├── .env
├── README.md
```

---



# 📜 Licencia

Este proyecto utiliza textos de dominio público provenientes de **Project Gutenberg**.

El código está disponible para uso educativo y experimental.

---

# 👩‍💻 Autora

Maria Moreno
Estudiante de Física interesada en programación, ciencia y divulgación científica.

---
