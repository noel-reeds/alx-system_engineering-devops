# adjusts OS configs for holberton user
exec {'change-os-configs-for-holberton-user':
  command  => 'sudo sed -i "/s/nofile 5/nofile 2048/" /etc/security/limits.conf',
  path     => ['/usr/bin/', '/bin/'],
}
exec {'change-os-configs-for-holberton-user2':
  command  => 'sudo sed -i "/s/nofile 4/nofile 2048/" /etc/security/limits.conf',
  path     => ['/usr/bin/', '/bin/'],
}
