class Config:
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Dev127336'
    MYSQL_DB = 'subject_system'
    MYSQL_HOST = 'mysql'  # 使用 Docker Compose 服務名
    MYSQL_PORT = 3306
    SEND_FILE_MAX_AGE_DEFAULT = 0  # 禁用靜態文件緩存
    TEMPLATES_AUTO_RELOAD = True  # 自動重新加載模板