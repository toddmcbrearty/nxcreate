nxcreate
========

Creates an Nginx server_block from commandline.

I created this project to learn python. 

*Note:*
If you've downloaded my [myvagrant](https://github.com/toddmcbrearty/myvagrant) project this is included and will install automatically via vagrant. 

Installation
============

Copy the nxcreate directory to the root of you Linux distrbution.
To make it easy to run from anywhere run the following command
cp /nxcreate/nxcreate.py /usr/bin/nxcreate
or you can run the program by typing /nxcreate/nxcreate.py


Usage
=====

Type nxcreate (if you copied nxcreate.py to /usr/bin) or type /nxcreate/nxcreate.py
You will be asked a series of questions

1. Enter the site URL (what ever the site url is)
2. Enter your sites root directoy (this is the directory within www folder the site is located in)
3. If you sites has a public directory enter it (sometimes you'll use a folder called public_html or public which contains the public files. that is what you add here)
4. Will you be forcing WWW? (this will force the site to use www.)
5. Will you need pretty urls? (this makes pretty urls work. This is tested with CodeIgniter and Laravel)

Once you complete the questions it will create the server_block file in sites-available and create a symlink to sites-enabled. It will also reload nginx

Disclaimer
==========
As I said this was just a way for me to learn python. It works just fine on my local box. Which is Ubuntu 12.04. I have not run it on anything else so USE THIS AT YOUR OWN RISK. Although if you read through the code it can't really mess anything up.






