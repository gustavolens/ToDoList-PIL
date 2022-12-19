# ToDoList-PIL

## Back 

### Requerimientos:
- Python >=3.10: https://www.python.org/
- Pip: https://pypi.org/project/pip/
- mysqlclient (especialmente usuarios de Linux): https://pypi.org/project/mysqlclient/
- Xampp o cualquier otro administrador de bases de datos relacionales: https://www.apachefriends.org/download.html
### Instalación local:
- Clonar repositorio:
``` sh
git clone https://github.com/gustavolens/ToDoList-PIL.git 
```
- Dentro de la carpeta, crear entorno virtual:
``` sh
python -m venv env 
```
- Activar el entorno (Linux):
``` sh
source env/bin/activate 
``` 
- Ingresar a la carpeta backend e instalar dependencias:
``` sh
pip install -r requirements.txt 
``` 
### Ejecutar proyecto:
- Antes, importar base de datos 'todolist.sql' y, en el archivo settings.py, configurar acorde a usuario, contraseña y nombre de BD:
- Luego, ejecutar Django:
``` sh
python manage.py runserver
``` 

## Front

### Requerimientos:
- Nodejs (se recomienda nvm): https://nodejs.dev/en/
### Proyecto creado con React + Vite:
``` sh
npm create vite@latest
```
### Bibliotecas:
- Axios para trabajar apis: https://axios-http.com/
### Instalación local:
- Ir a la carpeta front y ejecutar:
``` sh
npm install 
```
### Ejecutar proyecto:
``` sh
npm run dev 
```
