# adjusts user limitations.
exec {'update_hard_limit':
  command => 'sed -i "s/nofile 5/nofile 2048/" etc/security/limits.conf',
  path    => ['usr/bin', '/bin'],
}

exec {'update_soft_limit':
  command => 'sed -i "s/nofile 4/nofile 1024/" etc/security/limits.conf',
  path    => ['usr/bin', '/bin'],
}
