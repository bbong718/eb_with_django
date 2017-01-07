import os, sys
from subprocess import call

PROJECT_MIN_LEN = 4
PROJECT_INDENTATION = '.' * 3
PROJECT_DJANGO_VER = '1.9.2'

my_home = os.getenv('HOME')
my_cwd = os.getcwd()

def project_name():
    my_project = raw_input(PROJECT_INDENTATION + "[+] What is the project name?: ")
    if len(my_project) < PROJECT_MIN_LEN:
        print "Illegal project name: '" + my_project + "'!"
        exit()
    
    if os.path.exists(my_home + '/' + my_project):
        print "Path: %s/%s already exists, aborting!" % (my_home, my_project)
        exit()

    print PROJECT_INDENTATION * 2 + "[!] Project name: %s" % my_project
    return my_project

def start_virtualenv(my_activate):
    try:
        call(['source', my_activate])
    except:
        print "#" * 60
        print "[!] Failed to call->source on %s" % my_activate
        print "Run 'source %s' by hand!" % my_activate
        print "Run 'pip install django==%s'" % PROJECT_DJANGO_VER
        print "#" * 60
        raw_input()


print "[!] Creating new Python Virtual Environment for Django..."
os.chdir(my_home)

my_project = project_name()
my_project_path = my_home + '/' + my_project

print PROJECT_INDENTATION + '[!] Creating environment: %s...' % my_project
call(['virtualenv', my_project_path])

my_project_activate = my_project_path + '/bin/activate'
start_virtualenv(my_project_activate)

print PROJECT_INDENTATION + "[!] Successfully created new Django virtualenv"
