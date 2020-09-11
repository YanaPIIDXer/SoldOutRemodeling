FROM httpd:2.4

RUN apt-get install -y perl-base
RUN ln -s /usr/bin/perl /usr/local/bin/perl

ADD ./httpd.conf /usr/local/apache2/conf/httpd.conf
WORKDIR /usr/local/apache2/htdocs
