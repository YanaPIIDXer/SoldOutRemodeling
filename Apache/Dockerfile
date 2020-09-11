FROM centos:7

RUN yum install -y httpd httpd-devel

ADD ./httpd.conf /etc/httpd/conf/httpd.conf

ADD ./SOLDOUT/soldout /var/www/html
RUN chmod 755 /var/www/html -R && \
    chown apache:apache /var/www/html -R
RUN chmod 777 /var/www/html/data
WORKDIR /var/www/html

CMD "/usr/sbin/httpd" "-D" "FOREGROUND"
