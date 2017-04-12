0. clone repo
git clone https://github.com/zserg/flashcard.git

1. create virtualenv, activate it
cd flashcard
virtualenv -p python3 venv

1.1 Setup database:
create user
create table
add permission to user

2.2 pip install -r requirements/local.txt
2. edit .env file:
 DEBUG=on
 ALLOWED_HOSTS='your_host_name'
 SECRET_KEY='your_secret_key'
 DATABASE_URL=psql://urser:password@127.0.0.1:port/database


3. migrate database
DJANGO_READ_DOT_ENV_FILE=True ./manage.py migrate

4. create superuser
 DJANGO_READ_DOT_ENV_FILE=True ./manage.py createsuperuser

4. run dev server
 DJANGO_READ_DOT_ENV_FILE=True ./manage.py runserver


$ http POST example.com:8000/flashcard/api/v1/api-token-auth/ username='user'  password='password'

$ http GET example.com:8000/flashcard/api/v1/decks/ Authorization:'Token 11111111111111111111111111111111111'
$ export AUTH="Authorization:Token 11111111111111111111111111111111111"
$ http GET example.com:8000/flashcard/api/v1/decks/ "$AUTH"

$ http POST example.com:8000/flashcard/api/v1/decks/ "$AUTH" name='MyDeck'


$ http example.com:8000/flashcard/api/v1/decks/7/cards/ "$AUTH"
$ http POST example.com:8000/flashcard/api/v1/decks/1/cards/ "$AUTH" "question"="How are you?" "answer"="Fine!"

$ http example.com:8000/flashcard/api/v1/decks/7/cards/?days=1 "$AUTH"

$ http DELETE example.com:8000/flashcard/api/v1/decks/20/ "$AUTH"

