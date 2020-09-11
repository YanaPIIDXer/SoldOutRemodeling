FROM netroby/docker-apache-perl:latest

ADD ./SOLDOUT/soldout /var/www/html
RUN chmod 755 /var/www/html -R && \
    chown www-data:www-data /var/www/html -R
RUN chmod 777 /var/www/html/data
WORKDIR /var/www/html

CMD "/usr/sbin/apache2ctl" "-D" "FOREGROUND"
