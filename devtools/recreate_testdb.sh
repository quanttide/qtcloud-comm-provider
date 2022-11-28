# 数据库命令，暂存命令
psql postgres

DROP DATABASE test_qtcloud_payments;
CREATE DATABASE test_qtcloud_payments;
GRANT ALL PRIVILEGES ON DATABASE test_qtcloud_payments to qtcloud_payments;
