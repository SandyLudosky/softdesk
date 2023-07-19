[![forthebadge](https://forthebadge.com/images/badges/cc-0.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/uses-css.svg)](https://forthebadge.com)


## Technologies
- Python 3
- Django 4
- Django Rest Framework


## Authors

Sandy Ludosky

# SoftDesk
Projet de développement d'API RESTful avec Django REST framework


## Installation & lancement

### cloner le répertoire
```
git clone https://github.com/SandyLudosky/softdesk

```
### créer un nouvel environnement virtuel:
```
python -m venv env
```
### activez l'environnement virtuel:
- Windows:
```
env\scripts\activate.bat
```
- Linux:
```
source env/bin/activate
```
### installer les librairies et paquets:
```
pip install -r requirements.txt
```
### exécuter les migrations:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
### lancer le serveur:
```
python manage.py runserver
```

Le serveur de développement est accessible sur http://127.0.0.1:8000/
Pour quitter, faire `CONTROL-C`.