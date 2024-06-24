# 1-user_limit.pp
# The script will modify '/etc/security/limits.conf' to increase the number of open files for the holberton user.

exec { 'change-os-configuration-for-holberton-user':
  command => 'echo "holberton soft nofile 4096\nholberton hard nofile 8192" >> /etc/security/limits.conf',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  unless  => 'grep -q "holberton" /etc/security/limits.conf',
}
