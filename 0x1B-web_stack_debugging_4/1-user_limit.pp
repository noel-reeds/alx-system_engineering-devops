# adjusts OS configs for holberton user
exec {'change-os-configs-for-holberton-user':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 2048/" /etc/security/limits.conf',
}
exec {'change-os-configs-for-holberton-user2':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 2048/" /etc/security/limits.conf',
}
