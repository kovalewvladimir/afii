#Django 

##Установка (windows)

```
git clone https://github.com/kovalewvladimir/afii.git
virtualenv --no-site-packages afii
cd afii
Scripts\activate
pip install -r requirements.txt
python Scripts\django-admin.py startproject afii
cd afii
python manage.py startapp inventory
```