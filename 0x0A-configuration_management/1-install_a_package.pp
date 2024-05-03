# Define a package ressource to ensure Flask v2.1.0 is installed

package { 'flask':
  ensure => '2.1.0',
  provider => 'pip3',
}
