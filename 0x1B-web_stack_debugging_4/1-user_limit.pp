# adjusts user limitations.
exec {'update_hard_limit':
  command => 'sed -i "s/5/1024/" etc/security/limits.conf',
  path    => ['usr/bin', '/bin'],
}

exec {'update_soft_limit':
  command => 'sed -i "s/4/1024/" etc/security/limits.conf',
  path    => ['usr/bin', '/bin'],
}
