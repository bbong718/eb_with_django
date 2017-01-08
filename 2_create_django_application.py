import os, sys
from subprocess import call

PROJECT_MIN_LEN = 4
PROJECT_INDENTATION = '.' * 3
PROJECT_EB_JANGO = ['django-admin', 'startproject', 'ebdjango']
PROJECT_START = ['python', 'manage.py', 'runserver']
PROJECT_REQUIREMENTS = 'pip freeze > requirements.txt'
PROJECT_EB_EXTENSION = '.ebextensions'
PROJECT_EB_DJANGO_CONF = 'django.config'
PROJECT_EB_DJANGO_CONF_DATA = """
option_settings:
      aws:elasticbeanstalk:container:python:
          WSGIPath: %s/%s/wsgi.py
"""


if not hasattr(sys, 'real_prefix'):
    print "[!] Please run me in virtualenv on your project!"
    exit()

def create_new_project():
    print "[!] Starting new Elastic Beanstalk Django project..."
    try:
        call(PROJECT_EB_JANGO)
    except BaseException as e:
        print PROJECT_INDENTATION + "[!] Failed to create new ebdjango project! %s" % str(e)
        exit()

def run_manage():
    print PROJECT_INDENTATION + "[+] Starting python server for your django project"
    try:
        call(PROJECT_START)
    except:
        print PROJECT_INDENTATION + "[!] Failed to start project, see error for details!"
        exit()

def project_requirements():
    print PROJECT_INDENTATION + "[+] Creating project requirements for Elastic Beanstalk..."
    try:
        os.system(PROJECT_REQUIREMENTS)
    except:
        print PROJECT_INDENTATION + "[!] Failed to create project requirements"
        exit()

def create_ebextensions():
    print PROJECT_INDENTATION + '[+] Creating ' + PROJECT_EB_EXTENSION
    try:
        os.mkdir(PROJECT_EB_EXTENSION)
    except BaseException as e:
        print PROJECT_INDENTATION + '[!] Failed to create EB Extensions directory'

    eb_ext_fh = open(PROJECT_EB_EXTENSION + '/' + PROJECT_EB_DJANGO_CONF, "w")
    eb_ext_fh.truncate()
    eb_ext_fh.write(PROJECT_EB_DJANGO_CONF_DATA % (PROJECT_EB_JANGO[2], PROJECT_EB_JANGO[2]))
    eb_ext_fh.close()

def get_python_version():
    print PROJECT_INDENTATION + '[?] Figuring out Python version...',
    for py in os.listdir('lib')
        if 'python' in py:
            break
    py
    return py

def init_eb_project(my_py):
    my_eb_proj_create = raw_input(PROJECT_INDENTATION + '[?] Do you want to AWS EB project? [y/n]: ')
    if my_eb_proj_create == 'n':
        print 'Goodbye!'
        exit()

    while True:
        my_eb_proj_name = raw_input(PROJECT_INDENTATION + '[?] What would you like to call your application?: ')
        if len(my_eb_proj_name) < PROJECT_MIN_LEN:
            print PROJECT_INDENTATION + '[!] Project should be at least %d characters long!' % PROJECT_MIN_LEN
        else:
            break

    call(['eb', 'init', '-p', my_py, my_eb_proj_name])

os.chdir(os.getcwd())
create_new_project()
project_requirements()
create_ebextensions()

os.chdir(PROJECT_EB_JANGO[2])
run_manage()

# Move up one path so we can get the python version
os.chdir('..')
my_py = get_python_version()

init_eb_project(my_py)
