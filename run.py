from os import getenv
from src import create_app
from src.config import DevelopmentConfig, ProductionConfig, TestingConfig

environment = getenv('CONFIG') or 'development'
if environment == 'production':
    config_class = ProductionConfig
elif environment == 'testing':
    config_class = TestingConfig
else:
    config_class = DevelopmentConfig

app = create_app(config_class)

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])