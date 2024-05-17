# adjusts OS config for holberton user
exec {'change_os_configuration_for_holberton_user1':
  command => 'sed -i "/holberton hard/s/5/2048/" etc/security/limits.conf',
  path    => ['usr/bin', '/bin'],
  user    => 'root',
  before  => Exec['change_os_configuration_for_holberton_user'],
}
exec {'change_os_configuration_for_holberton_user':
  command => 'sed -i "/holberton soft/s/4/1024/" etc/security/limits.conf',
  path    => ['usr/bin', '/bin'],
  user    => 'root',
}
