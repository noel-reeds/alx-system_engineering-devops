# adjusts OS configs for holberton user
exec {'change_os_configuration_for_holberton_user':
  provider => shell,
  command  => 'sudo sed -i "/holberton hard/s/5/50000000/" etc/security/limits.conf',
  before   => Exec['change_os_configuration_for_holberton_user2'],
}
exec {'change_os_configuration_for_holberton_user2':
  provider => shell,
  command  => 'sudo sed -i "/holberton soft/s/4/4500000/" etc/security/limits.conf',
}
