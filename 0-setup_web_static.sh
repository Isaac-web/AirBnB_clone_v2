#!/usr/bin/env bash
#preparing the web servers for deployment

mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echoh "Web server is working..." > /data/web_static/releases/test/index.html

#create the link
LINK=/data/web_static/current
if [ -L $LINK ]
then
	rm -f $LINK
fi

ln -s /data/web_static/releases/test/ $LINK

chown ubuntu -R /data && chgrp ubuntu -R /data
sed -i ,root /var/www/school, root /data/web_static/current/, /etc/nginx/nginx/conf

systemclt restart nginx

exit 0
