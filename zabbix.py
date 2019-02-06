version: '2'
services:
  zabbix-db:
    image: zabbix/zabbix-db-mariadb
    volumes:
      - zabbix-db-storage:/var/lib/mysql
      - backups:/backups
      - /etc/localtime:/etc/localtime:ro
    environment:
      - MARIADB_USER=zabbix
      - MARIADB_PASS=my_password
  zabbix-server:
    image: zabbix/zabbix-3.0:latest
    depends_on:
      - zabbix-db
    ports:
      - "80:80"
      - "10051:10051"
    volumes:
      - /etc/localtime:/etc/localtime:ro
    links:
      - zabbix-db:zabbix.db
    environment:
      - ZS_DBHost=zabbix.db
      - ZS_DBUser=zabbix
      - ZS_DBPassword=my_password
volumes:
  zabbix-db-storage:
    driver: local
  backups:
    driver: local