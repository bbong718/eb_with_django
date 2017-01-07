import os
from subprocess import call

PROJECT_MIN_LEN = 4
PROJECT_INDENTATION = '.' * 3

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
        print "Failed to call->source on %s" % my_activate


print "[!] Creating new Python Virtual Environment for Django..."
os.chdir(my_home)

my_project = project_name()
my_project_path = my_home + '/' + my_project

print PROJECT_INDENTATION + '[!] Creating environment: %s...' % my_project
call(['virtualenv', my_project_path])

my_project_activate = my_project_path + '/bin/activate'
print "Project Activate is: %s" % my_project_activate

start_virtualenv(my_project_activate)
call(['pip', 'freeze'])

print PROJECT_INDENTATION + "[!] Successfully created new Django virtualenv"
