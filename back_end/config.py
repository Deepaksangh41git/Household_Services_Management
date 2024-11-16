class Config():
    DEBUG=False
    SQL_ALCHEMY_TRACK_MODIFICATIONS=False

class LocalDevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI="sqlite:///database.sqlite3"
    DEBUG=True
    SECURITY_PASSWORD_HASH='bcrypt'
    
    #it will be added in the password and then the string will be hashed
    SECURITY_PASSWORD_SALT='isthisstringasecrt'
    SECRET_KEY="Thiskeyshoudbeeveryseret"
    WTF_CSRF_ENABLED=False