from app import create_app
from dynaconf import settings

application = create_app()

# Uncomment this while testing the app locally
if settings.ENV_FOR_DYNACONF == "development":
    application.run(host="0.0.0.0", port=5000, debug=True)