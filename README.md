# Servicio Gestión

```sh

python -m venv projvenv # create project venv
cd projvenv && source bin/activate
git clone --single-branch --branch dev git@github.com:Faronien/ServicioGestion.git
pip install -r requirements.txt
pyton manage.py makemigrations && python manage.py migrate 
python manage.py createsuperuser # create admin user
python manage.py runserver # run server

```
