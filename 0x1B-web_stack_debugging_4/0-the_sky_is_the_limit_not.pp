# adjusts maximum requests handled Nginx webserver
exec {'update_ULIMIT':
  command => 'sed -i "s/15/2048/" /etc/default/nginx',
  path    => ['usr/bin/', '/bin'],
}
exec {'restart_nginx':
  command => '/usr/sbin/service nginx restart',
  path    => ['/usr/sbin/', '/sbin', '/usr/bin'],
}
