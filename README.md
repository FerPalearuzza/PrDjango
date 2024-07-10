Proyecto Integrador Codo a Codo 
MundoCafe

Autores Frontend: Sol, Fer & Exe
Autores Backend:  Sol, Fer, Exe & Maxi

Descripcion: breve pagina web con informacion relacionada con el cafe. Backend Realizado en Django

NOTAS PARA EL BACKEND: 
Se requiere un entorno virtual de python con las dependencias que figuran en el archivo "requirements.txt". 
pip tiene un comando para instalar leyendo el archivo directamenente.

La base de datos no se commitea, las migraciones estrucutran la tabla, pero no su contendio.
Para cargar el contenido de la tabla, estando en la misma carpeta del archivo json:
python manage.py loaddata db_recetas.json

Las imagenes correspondientes deberían estar ya cargadas en media/recipes



