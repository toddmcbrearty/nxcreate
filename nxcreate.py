#!/usr/bin/env python

import sys,os

nxfunctions = open('/nxcreate/nxcreate_functions.py').read()
exec nxfunctions

euid = os.geteuid()
if euid != 0:
    print "Script not started as root. Running sudo.."
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    # the next line replaces the currently-running process with the sudo
    os.execlpe('sudo', *args)

print 'Script is now running as root'

#first lets load the server_block template
with open ("/nxcreate/templates/server_block.template") as sb_temp:
	server_block_template=sb_temp.read()

#first lets load the www template
with open ("/nxcreate/templates/www.template") as www_temp:
	www_template=www_temp.read()


site_url = raw_input('Enter the site URL: ')
site_directory = raw_input('Enter your sites root directoy: ')
public_directory = raw_input('If you sites has a public directory enter it: ')
force_www = query_yes_no('Will you be forcing WWW?', 'no')
pretty_urls = query_yes_no('Will you need pretty urls?', 'no')

block_file = server_block_template

if force_www:
	block_file = block_file.replace('[WWW]', www_template.replace('[URL]', site_url))
	www = 'www.'
else:
	block_file = block_file.replace('[WWW]', '')
	www = ''

if pretty_urls:
	block_file = block_file.replace('[PRETTY_URL]', 'if (!-e \$request_filename) { rewrite \$ \/index.php?\$1 last; }')
else:
	block_file = block_file.replace('[PRETTY_URL]', '')

if public_directory:
	site_directory = site_directory + '/' + public_directory


block_file = block_file.replace('[URL]', site_url)
block_file = block_file.replace('[DIRECTORY]', site_directory)
block_file = block_file.replace('[www]', www)

#remove the files if they exist already
if os.path.exists('/etc/nginx/sites-available/' + site_url):
	os.remove('/etc/nginx/sites-available/' + site_url)

if os.path.exists('/etc/nginx/sites-available/' + site_url):
	os.remove('/etc/nginx/sites-enabled/' + site_url)

#ok now we have contents created save it to the block_file
sb = open('/etc/nginx/sites-available/' + site_url, 'w')
sb.write(block_file)
sb.close()

if not os.path.islink('/etc/nginx/sites-enabled' + site_url): 
	os.symlink('/etc/nginx/sites-available/' + site_url, '/etc/nginx/sites-enabled/' + site_url)

os.system('service nginx reload')
