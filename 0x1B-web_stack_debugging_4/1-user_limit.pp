# adjusts user login limits requests
exec {'update_hard_limit':
  command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 2048/" etc/security/limits.conf',
  path    => ['usr/bin', '/bin'],
}

exec {'update_soft_limit':
  command => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 1024/" etc/security/limits.conf',
  path    => ['usr/bin', '/bin'],
}
