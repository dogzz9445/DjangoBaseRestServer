set DJANGO_PROJECT_URI=C:\\Projects\\BaseRestfulServer\\
set DJANGO_VENV_URI=venv\\Scripts\\
set "VENV_PYTHON=%DJANGO_PROJECT_URI%%DJANGO_VENV_URI%

cd %DJANGO_PROJECT_URI% &
%VENV_PYTHON%python.exe manage.py makemigrations &
%VENV_PYTHON%python.exe manage.py migrate &
%VENV_PYTHON%python.exe manage.py runserver
