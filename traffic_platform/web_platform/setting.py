# 配置数据库连接

#调试模式是否开启
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
#session必须要设置key
SECRET_KEY='random string'
#mysql数据库连接信息,这里改为自己的账号
SQLALCHEMY_DATABASE_URI = 'sqlite:///students.sqlite3'

UPLOAD_FOLDER ='upload/'        # 定义上传文件夹的路径
MAX_CONTENT_LENGTH = 10 * 1024 * 1024     # 指定要上传的文件的最大大小（以字节为单位）