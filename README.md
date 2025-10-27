# Pipeline ETL y Análisis Académico con PowerBI

![Dashboard Académico](https://i.imgur.com/38okuRU.jpeg) 
![Dashboard Académico](https://i.imgur.com/hbgg9qo.png) 
![Dashboard Académico](https://i.imgur.com/8sQprEw.png) 

## Descripción del Proyecto
Este proyecto es una demostración de un pipeline **ETL (Extract, Transform, Load)** completo. El objetivo es conectar con una base de datos MySQL local (`db_colegio`), extraer los datos brutos, aplicar un proceso de limpieza y transformación robusto con **Python (Pandas)**, y cargar los datos limpios en ficheros CSV listos para ser consumidos por una herramienta de Business Intelligence como **Power BI**.

El proyecto demuestra habilidades clave en:
* Conexión segura a bases de datos con `SQLAlchemy` y `python-dotenv`.
* Limpieza y estandarización de datos (manejo de nulos, duplicados y normalización de categorías).
* Manejo de tipos de datos, especialmente la conversión de fechas.
* Preparación de un modelo de datos optimizado para el análisis visual.
---
## Objetivos del Análisis
El dashboard final en Power BI permite explorar los datos limpios para responder preguntas clave sobre el rendimiento académico, tales como:

* ¿Cuál es la distribución de notas (`nota`) por asignatura y rama de conocimiento?
* ¿Cómo se comparan las notas medias entre trimestres?
* ¿Existe alguna correlación entre la fecha del examen y la nota obtenida?
* Identificación de alumnos y su rendimiento a través de las diferentes asignaturas.

---
## Tecnologías Utilizadas
* **Base de Datos:** MySQL
* **ETL (Python):** Pandas, SQLAlchemy, python-dotenv
* **Visualización:** Power BI
* **Control de Versiones:** Git y GitHub
---
## Estructura del Proyecto
```
instituto/
├── data_clean/         # Datos limpios generados por el script de Python
├── scripts/
│   ├── db_extraccion.py 
│   └── limpieza_instituto.py   # Script principal de ETL y análisis
├── sql/
│   ├── schema.sql              # Script DDL para crear la estructura de la BBDD
│   ├── data_insertion.sql      # Script DML para poblar la BBDD
│   └── Schema Diaram           # Modelo visual de la BBDD (MySQL Workbench)
└── README.md

```
---
## ¿Cómo Empezar?

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/dani-dp/analisis_instituto.git
    ```
2.  **Monta la Base de Datos:**
    * Ejecuta el script `sql/schema.sql` en tu gestor de MySQL para crear las tablas.
    * Ejecuta el script `sql/data_insertion.sql` para añadir los datos de ejemplo.

3.  **Prepara el Entorno de Python:**
    * Asegúrate de tener Python instalado.
    * Se recomienda crear un entorno virtual:
        ```bash
        python -m venv .venv
        source .venv/bin/activate
        ```
    * Instala la librería necesaria:
        ```bash
        pip install pandas sqlalchemy mysql-connector-python python-dotenv
        ```
4.  **Configura las Credenciales:**
    * Navega a la carpeta scripts/ 
    * Crea un archivo llamado .env
    * Añade tus credenciales de la base de datos local al archivo .env

5.  **Ejecuta el Script ETL:**
    * Navega a la carpeta `scripts/` y ejecuta el script principal:
        ```bash
        python limpieza_instituto.py
        ```
    * Esto generará los ficheros limpios en la carpeta `data_clean`.

6.  **Abre el Dashboard:**
    * Abre el fichero `.pbix` del proyecto con Power BI Desktop.
    * Si es necesario, actualiza las rutas de origen de los datos para que apunten a tu carpeta local `data_clean`.

---
## Autor

* **Daniel Díaz** - [Perfil de Linkedin](www.linkedin.com/in/danieldiaz-data) | [Portfolio en GitHub](https://github.com/dani-dp)
