# Ensure Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Create necessary directories
file { '/data':
  ensure => directory,
}

file { '/data/web_static':
  ensure => directory,
}

file { '/data/web_static/releases':
  ensure => directory,
}

file { '/data/web_static/shared':
  ensure => directory,
}

file { '/data/web_static/releases/test':
  ensure => directory,
}

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html><head></head><body>Holberton School</body></html>',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
}

# Ensure correct ownership
exec { 'set_ownership':
  command => 'chown -R ubuntu:ubuntu /data',
  path    => '/bin:/usr/bin',
  require => [
    File['/data'],
    File['/data/web_static'],
    File['/data/web_static/releases'],
    File['/data/web_static/shared'],
    File['/data/web_static/releases/test'],
    File['/data/web_static/releases/test/index.html'],
    File['/data/web_static/current'],
  ],
}

# Restart Nginx
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

