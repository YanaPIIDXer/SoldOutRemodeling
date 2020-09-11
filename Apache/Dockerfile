FROM netroby/docker-apache-perl:latest

ADD ./SOLDOUT/soldout /var/www/html
RUN chmod 755 /var/www/html -R
WORKDIR /var/www/html

CMD "/usr/sbin/apache2ctl" "-D" "FOREGROUND"
