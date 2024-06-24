# 0-the_sky_is_the_limit_not.pp
# Increases the worker_connections setting in the Nginx configuration file from 1024 to 4096.

exec { 'fix--for-nginx':
  command => 'sed -i "s/worker_connections 1024/worker_connections 4096/" /etc/nginx/nginx.conf && service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin'
}
