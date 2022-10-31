#!/usr/bin/env bash
#preparing the web servers for deployment

mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Web server is working..." > /data/web_static/releases/test/index.html

#create the link
LINK=/data/web_static/current
if [ -L $LINK ]
then
	rm -f $LINK
fi

ln -s /data/web_static/releases/test/ $LINK

#chown ubuntu -R /data && chgrp ubuntu -R /data
echo > -e 'events {
}

http {
        server {
                listen 80;
                root /var/www/alx/html;
                index index.html;

                location \ {

                }
        }

}

' >  /etc/nginx/nginx.conf

systemctl restart nginx

exit 0
