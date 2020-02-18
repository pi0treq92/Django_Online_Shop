# Django_Online_Shop
### The main puprpose was create web application using Django 2.2.8 framework
### Technologies used in project:

<p><a href="url"><img src="https://docs.celeryproject.org/en/latest/_static/celery_512.png" align="left" height="80"></a>
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="url"><img src="https://cloud.githubusercontent.com/assets/72164/2638484/3f743636-beaf-11e3-8f26-0d3b41f12edf.png" align="left" height="64"></a></p>
<p><a href="url"><img src="https://weasyprint.readthedocs.io/en/stable/_static/logo.png" align="left" height="64"></a> &emsp;&emsp;<a href="url"><img src="https://www.rabbitmq.com/img/RabbitMQ-logo.svg" align="left"></a></p>
<br>
<p><a href="url"><img src="https://redis.io/images/redis-white.png" align="left"></a></p>
<br>
<br>
GTK+ for Windows Runtime Environment Installer: 64-bit is required for WeasyPrint</p>
If you get an error like OSError: dlopen() failed to load a library: cairo / cairo-2 it’s probably because cairo (or another GTK+ library mentioned in the error message) is not properly available in the folders listed in your PATH environment variable.</p>
<br>
<br>
<br>
How to install rosetta and gettext-tools for translation on Windows?
<br>
<br>
In windows you just need to download :
<br>
&emsp;gettext-tools-xx.zip
<br>
&emsp;gettext-runtime-xx.zip

from here:<a href="http://ftp.gnome.org/pub/gnome/binaries/win32/dependencies/"> enter link description here</a>

Then you need to unzip them and copy all in bin folder of both files into:
<br>C:\Program Files\gettext-utils\bin 
<br>then you need to go to control panel-> system -> advanced -> environment variables and add this path:<br>C:\Program Files\gettext-utils\bin to path variables. 
<br>
<br>
Note: xx is the version you want to download if you download version 18 you will get an error that some dll file is missing, I suggest to download version 17
    this folder :gettext-utils\bin does not exist and you need to create it
    restart your pc before you use gettext
<br>
<br>
After settings Languages in settings.py in the shell type:<br>
&emsp;django-admin makemessages --all <br>
You should get the following output:<br>
&emsp;processing locale en<br>
&emsp;processing locale pl<br>
<br>
If you get something like that:<br>
&emsp;CommandError: Can't find msguniq. Make sure you have GNU gettext tools 0.15 or newer installed.
<br>
Check once more if you correctly did steps above.<br>
<br>
To complie your translation in .po files type in the shell:<br>
&emsp;django-admin compilemessages


