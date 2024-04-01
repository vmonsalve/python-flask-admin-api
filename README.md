# Api users

## Estructura

* controller
* models
* herlpers

## Archivo .env

```
DBA_NAME=xxx
DBA_USER=xxx
DBA_PASSWORD=xxx
DBA_HOST=127.0.0.1
DBA_PORT=3306
```
## Archivo requirements.txt

Si se agregan nuevas libreas se debe actualizar este archivo con el siguiente comando

```
python -m pip freeze > requirements.txt

```

Para instalar las dependencias debe ser con el comando

```
pip install -r requirements.txt
```

## Instalar mysql con docker

```
docker run \
 --name mysqldb \
 -e MYSQL_ROOT_PASSWORD=tu_password \
 -v $(pwd)/data_folder:/var/lib/mysql \
 -p 3306:3306 \
 -d \
 arm64v8/mysql
```