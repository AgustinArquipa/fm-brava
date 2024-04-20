# DJANGO FM BRAVA Project

Este es un proyecto base de Django diseñado específicamente para estructurar y organizar el proyecto de balance. Proporciona una estructura escalable y está preparado para ser utilizado con una base de datos PostgreSQL.

## 🚀 Pasos de instalación
### 1. Crear un entorno virtual

Utilizamos `venv` para manejar entornos virtuales. Para crear un nuevo entorno virtual llamado `venv-balance`, ejecuta:

python3.11 -m venv venv-balance


Activar el entorno virtual:


- **Linux o Mac**:

source venv-balance/bin/activate

- **Windows**:

cd optica-total

cd Scripts

```./activate```

### 2. Instalación de dependencias

Una vez dentro del entorno virtual, navega hasta la raíz del proyecto y ejecuta:

pip install -r requirements.txt

### 3. Configuración de credenciales

Dentro de la raíz del proyecto, crea un archivo llamado `secret.json` con la siguiente estructura:

```json
{
    "FILENAME": "secret.json",
    "SECRET_KEY": "clave_secreta_pedir_administrador_del_sistema",
    "DB_NAME": "DB_NAME",
    "DB_USER": "postgres",
    "DB_PASSWORD": "password",
    "DB_HOST": "localhost",
    "DB_PORT": 5432,

    "EMAIL_HOST": "smtp.gmail.com",
    "EMAIL_HOST_USER": "CORREO_EMPLEADO",
    "EMAIL_HOST_PASSWORD": " <<PASSWORD>> ",
    "SERVER_EMAIL": "CORREO_EMPLEADO",
    "DEFAULT_FROM_EMAIL": "NAME_RANDOM"
}
```
Nota: Asegúrate de cambiar los valores de SECRET_KEY, DB_NAME, DB_USER y DB_PASSWORD a los apropiados para tu configuración.

### 4. Configuración de la base de datos

Dado que utilizamos PostgreSQL como base de datos, asegúrate de tenerlo instalado y en ejecución.

### 5. Crear y aplicar migraciones

Para crear las migraciones y aplicarlas, ejecuta:

python manage.py makemigrations
python manage.py migrate

### 6. Variable de entorno
al ejecutar la aplicación o al configurar tu entorno virtual. Puedes hacerlo directamente en la terminal antes de ejecutar tu aplicación.

**En sistemas basados en Unix/Linux/Mac**

###########################################################

sudo su root

source venv-balance/bin/activate

export DEVELOPMENT_ENVIRONMENT="True"

python manage.py runserver

###########################################################

```export DEVELOPMENT_ENVIRONMENT=True```

**En Windows (CMD)**

```set DEVELOPMENT_ENVIRONMENT=True```