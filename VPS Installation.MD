**Newbie Guide to Linux/Ubuntu, Apache, Python, [Mongo] Stack**

Install Ubuntu 16.04 image on vps
Login as root
[Create user with admin priviledges]

Update Ubuntu
```
apt-get update && apt-get upgrade
```

Credits
https://blog.udacity.com/2015/03/step-by-step-guide-install-lamp-linux-apache-mysql-python-ubuntu.html

Install Apache
```
sudo apt-get install apache2
```

Test for Apache Default Page in Browser or
```
curl localhost
```

Install Python/Apache Tools
```
apt-get install python-setuptools libapache2-mod-wsgi
```

Restart Server
```
service apache2 restart
```

Add Spotipy Spotify Python Library
https://github.com/plamere/spotipy

```
apt install python-pip
pip install spotipy
```
**Do not update pip to version 10**

Spotipy Dependency
```
pip install spotipy
```

```
Block
```

