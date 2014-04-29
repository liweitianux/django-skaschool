django_skaschool deployment
===========================

Installation Notes
------------------
django 1.6:
requires python >= 2.6
requires mod_wsgi
requires mysql >= 5.0.3
requires MySQLdb >= 1.2.1p2 (pip mysql-python)

mysql-python:
requires mysql_config (libmysqlclient-dev)
requires Python.h (gcc build)

mod_wsgi:
daemon mode requires apache 2.x


MySQL database
--------------
database backend settings: `PROJECT_ROOT/settings.py'
  * NAME, USER, PASSWORD
create database table manually:
  mysql> CREATE DATABASE <NAME> CHARACTER SET utf8;
then syncdb using django manage.py:
  $ python manage.py syncdb
load data if needed:
  $ python manage.py loaddata <data.json>


MEDIA_ROOT:
set write permission for MEDIA_ROOT directory (upload files)


Apache2
-------
Requires version >= 2.2 (user authentication)
Configuration file: APACHE2_skaschool.conf


