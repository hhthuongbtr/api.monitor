#/script/sql_update.sh
#!/bin/bash
cat /tmp/log_file.sql > /tmp/inprocess.sql
cat /dev/null > /tmp/log_file.sql
sleep 1
mysql -uMonitorAgent -p11nit0rA93nt monitor -h x.x.x.x < /tmp/inprocess.sql

#crontab
* * * * * /script/sql_update.sh
* * * * * sleep 10; /script/sql_update.sh
* * * * * sleep 20; /script/sql_update.sh
* * * * * sleep 30; /script/sql_update.sh
* * * * * sleep 40; /script/sql_update.sh
* * * * * sleep 50; /script/sql_update.sh
