# configures SSH config file
file { 'ssh_config':
    ensure  => file,
    path    => '/etc/ssh/ssh_config',
    content => "
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
    ",
}
