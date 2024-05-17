# adjusts user login limits
exec {'change_os_configuration_for_holberton_user1':
  command => 'sudo sed -i "/holberton hard/s/5/2048/" etc/security/limits.conf',
  path    => ['usr/bin', '/bin'],
  require => Exec['change_os_configuration_for_holberton_user'],
}
exec {'change_os_configuration_for_holberton_user':
  command => 'sudo sed -i "/holberton soft/s/4/1024/" etc/security/limits.conf',
  path    => ['usr/bin', '/bin'],
}
