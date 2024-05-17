# adjusts user login limits
exec {'change_os_configuration_for_holberton_user':
  command => 'sed -i "s/5/2048/" etc/security/limits.conf; sed -i "s/4/1024/" etc/security/limits.conf',
  path    => ['usr/bin', '/bin'],
}
