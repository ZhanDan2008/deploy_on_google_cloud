run this commands:
git clone <repository_link>
python3 -m venv venv
source venv/bin/activate
pip install -r requirments.txt
while read file; do
    export "$file";
    done < .env
For running server:
python3 manage.py runserver --settings=app.settings.dev
