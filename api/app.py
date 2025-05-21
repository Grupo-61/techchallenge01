from api.src.flask_api import create_app
from flasgger import Swagger
import yaml
import os

app = create_app()

with open("apidocs/swagger_config.yml", "r") as file:
    swagger_config = yaml.safe_load(file)

swagger_config["host"] = os.getenv("API_HOST", "localhost:5000") 

swagger = Swagger(app, template=swagger_config)

if __name__ == "__main__":
    app.run()