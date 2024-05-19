# Fixes a internal 500 server err
exec {'sorts-wordpress-500-server-err':
  provider => shell,
  command  => 'sudo sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
}
