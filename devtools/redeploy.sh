# 重新配置本地数据库
# 项目根目录运行`sh devtools/redeploy.sh`
rm db.sqlite3
# 使用前先删除之前创建的迁移文件
python manage.py makemigrations
python manage.py migrate
python manage.py createcachetable
python manage.py createinitialrevisions