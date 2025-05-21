from api.src.flask_api import create_app
from flasgger import Swagger
import yaml
import os

swagger_path = os.path.join(os.path.dirname(__file__), "apidocs", "swagger_config.yml")
with open(swagger_path, "r") as file:
    swagger_config = yaml.safe_load(file)

swagger_config["host"] = os.getenv("API_HOST", "localhost:5000") 

app = create_app()

swagger = Swagger(app, template=swagger_config)

if __name__ == "__main__":
    app.run()