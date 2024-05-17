# adjusts user login limits
exec {'change_os_configuration_for_holberton_user1':
  command => 'sudo sed -i "s/nofile 5/nofile 2048/" etc/security/limits.conf',
  path    => ['usr/bin', '/bin'],
}
exec {'change_os_configuration_for_holberton_user':
  command => 'sudo sed -i "s/nofile 4/nofile 1024/" etc/security/limits.conf',
  path    => ['usr/bin', '/bin'],
}
