# ----- 拉取环境 -----
# 自制Django-MySQL版镜像
FROM quanttide-docker.pkg.coding.net/qtopen-django/django-with-mysql/django-with-mysql:latest


# ----- 复制文件到镜像 -----

# 创建`app`文件夹并将其设置为工作目录
RUN mkdir /app
WORKDIR /app

# 将当前目录复制到容器的`app`目录
ADD . /app/


# ----- 安装Python依赖 -----

# 可以在requirements.txt里设置Django等已打包依赖的版本覆盖镜像默认版本。
RUN pip install -r requirements.txt


# ----- 运行Django服务 -----

# 暴露端口
EXPOSE 8000

# 运行manage.py命令
CMD python3 manage.py migrate \
    && python3 manage.py createcachetable \
    && exec gunicorn qtpay.wsgi:application --bind 0.0.0.0:8000