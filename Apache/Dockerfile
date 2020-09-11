FROM httpd:2.4

RUN apt-get install -y perl-base

ADD ./httpd.conf /usr/local/apache2/conf/httpd.conf
WORKDIR /usr/local/apache2/htdocs
