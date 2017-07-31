import waitress
from Application import application

waitress.serve(application, listen="*:8080")