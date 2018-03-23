FROM nginx:alpine

RUN mkdir -p /var/www/test
RUN apk update
RUN apk add apache2-utils
RUN htpasswd -bc /etc/nginx/.htpasswd ray wong
RUN echo "a" > /var/www/test/a.txt
RUN echo "b" > /var/www/test/b.txt
RUN echo "c" > /var/www/test/c.txt
RUN echo "d" > /var/www/test/d.txt
RUN touch -d '201803230010' -t '201803230010' /var/www/test/d.txt
RUN touch -d '201803230008' -t '201803230008' /var/www/test/b.txt
RUN touch -d '201803230015' -t '201803230015' /var/www/test/c.txt
RUN touch -d '201803230010' -t '201803230010' /var/www/test/a.txt

COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /var/www/index.html

CMD ["nginx", "-g", "daemon off;"]

expose 8080