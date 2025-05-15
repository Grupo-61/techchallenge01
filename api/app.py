from src.flask_api import create_app
from flasgger import Swagger

app = create_app()
swagger = Swagger(app, template_file='../../apidocs/swagger_config.yml')

if __name__ == "__main__":
    app.run()