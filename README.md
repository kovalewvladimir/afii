# Accounting for inventory items. (Учет товарно-материальных ценностей)
Accounting for inventory items. (Учет товарно-материальных ценностей)

## Deploy

```
git clone -b deploy https://github.com/kovalewvladimir/afii.git /docker/afii
cd /docker/afii
docker build -t kovalewvladimir/afii .
docker run -d --name afii --restart always -v /docker/afii/:/afii -p 8000:8000 kovalewvladimir/afii
```

## Использованы библиотеки

### Front-end часть:
* [Bootstrap](http://bootstrap-3.ru) (v3.3.2)
* [jQuery](https://jquery.com) (v1.11.0)
* [jQuere.qrcode](https://github.com/jeromeetienne/jquery-qrcode) (v1.0)
* [jQuery.print](https://github.com/DoersGuild/jQuery.print) (v1.4.0)

### Back-end часть:
* [Django](https://www.djangoproject.com/)

## Контактная информация
e-mail: <kovalew.vladimir@gmail.com>