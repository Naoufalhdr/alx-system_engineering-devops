# 0-the_sky_is_the_limit_not.pp
# Increases the worker_connections setting in the Nginx configuration file from 1024 to 4096.

exec {'fix--for-nginx':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],
}

exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
