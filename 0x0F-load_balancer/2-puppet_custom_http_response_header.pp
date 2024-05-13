# Install Nginx and configuring my server with puppet
package { 'install nginx':
  ensure => installed,
}

file_line { 'config nginx':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Server-By $HOSTNAME;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

