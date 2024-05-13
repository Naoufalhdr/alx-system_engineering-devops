# Install Nginx and configuring my server with puppet

exec { 'update repo':
  command  => 'apt-get upadate',
  user     => 'root',
  provider => 'shell',
}

package { 'install nginx':
  ensure   => present,
  provider => 'apt',
}

file_line { 'config nginx':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Server-By $hostname;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  enable  => true, 
  require => Package['nginx'],
}

