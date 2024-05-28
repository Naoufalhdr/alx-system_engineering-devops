CREATE USER 'replica_user'@'%' IDENTIFIED BY 'your_replica_password';

GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';

FLUSH PRIVILEGES;
