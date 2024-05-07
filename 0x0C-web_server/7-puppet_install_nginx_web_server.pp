# Install Nginx and configuring my server with puppet

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Create the index html file
file { '/var/www/html/index.html':
  ensure  => present,
  content => "Hello World!",
}

# Define Nginx configuration file
file_line { 'ensure_line_exist':
  ensure => present,
  line   => 'listen 80 default_server;',
  path   => '/etc/nginx/sites-available/default',
}

file_line { '301_redirection_insert':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  content => '\n\tlocation /redirect_me {\n\t\treturn 301 youtube.com;\n\t}',
  after   => 'server_name _;
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
