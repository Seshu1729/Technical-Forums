import click
import sys
import os
import MySQLdb

from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Forum_Application.settings")
application = get_wsgi_application()

from Technical_Forums.models import *

@click.group()
def main():
    pass

@main.command('create_database', short_help='to create requried database')
@click.argument('username')
@click.argument('password')
@click.argument('database_name')
def create_database(username,password,database_name):
    '''command that creates a database and the appropriate tables (students and marks) and foreign key relationship between marks and students tables'''
    connection = MySQLdb.connect('localhost', username, password, '')
    cur = connection.cursor()
    sql_command = "CREATE DATABASE %s" % database_name
    try:
        cur.execute(sql_command)
        print "DATABASE CREATED SUCCUSSFULLY"

    except MySQLdb.Error,e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

    os.system("python manage.py makemigrations")
    os.system("python manage.py migrate")

@main.command('drop_database', short_help='to drop database')
@click.argument('username')
@click.argument('password')
@click.argument('database_name')
def drop_database(username,password,database_name):
    '''command that drop the database of students and marks'''
    connection = MySQLdb.connect('localhost', username, password, '')
    cur = connection.cursor()
    sql_command = "DROP DATABASE %s" % database_name
    try:
        cur.execute(sql_command)
        print "DROP DATABASE SUCCUSSFULLY"

    except MySQLdb.Error,e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

@main.command('clear_database', short_help='to clear database')
def clear_database():
    '''command that drop the database of students and marks'''
    Question.objects.all().delete()
    Answer.objects.all().delete()
    Reply.objects.all().delete()
    Tag.objects.all().delete()
    Tag_Question_Link.objects.all().delete()
    print "DATABASE CLEARED SUCCUSSFULLY"

if __name__ == '__main__':
    main()
