# Puppet Manifest for SSH Client Configuration

file_line { "Turn off passwd auth":
  path   => "~/.ssh/config",
  line   => 'PasswordAuthentication no',
  match  => '^\s*PasswordAuthentication',
  ensure =>  present,
}

file_line { "Declare identity file":
  path   => "~/.ssh/config
  line   => 'IdentityFile ~/.ssg/school',
  match  => '^\s*IdentityFile',
  ensure => present,
}
