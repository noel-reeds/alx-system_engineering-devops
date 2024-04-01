# kills a process

exec { 'pkill':
    command => '/usr/bin/pkill killmenow',
    onlyif  => '/usr/bin/pgrep killmenow',
    path    => '/usr/bin:/bin',
}
