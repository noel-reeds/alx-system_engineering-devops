# configures SSH config file
file { '/etc/ssh/ssh_config':
    ensure  => file,
    content => " ",
}

augeas { 'ssh_identity':
    context => '/files/etc/ssh/ssh_config',
    changes => [
        "set IdentityFile[1] ~/.ssh/school",
        "set PasswordAuthentication no",
    ],
}

