FROM netroby/docker-apache-perl:latest

ADD ./SOLDOUT/soldout /var/www/html
WORKDIR /var/www/html

CMD "/usr/sbin/apache2ctl" "-D" "FOREGROUND"
