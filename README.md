# Flashcard
Flashcard Django based proect with API and GUI.

![image1](https://cloud.githubusercontent.com/assets/6136638/25011145/70d0c3e2-207d-11e7-84e8-2b1769a0f151.png)

![image2](https://cloud.githubusercontent.com/assets/6136638/25011148/729ef6a8-207d-11e7-944a-bf83f4f61994.png)

## API usage
Here are the API usage examples using httpie client.

### Get auth token
```bash
http POST example.com:8000/flashcard/api/v1/api-token-auth/ username='user' password='password'
```
```json
{
    "token": "11111111222223333333333334445"
}
```
```bash
export AUTH="Authorization:Token 11111111222223333333333334445"
```
### Get list of decks
```bash
http GET example.com:8000/flashcard/api/v1/decks/  "$AUTH"
```
```json
[
    {
        "description": "",
        "id": 21,
        "name": "Misc"
    },
    {
        "description": "",
        "id": 17,
        "name": "MyEnglish"
    }
]
```
### Create new deck
```bash
http POST example.com:8000/flashcard/api/v1/decks/ "$AUTH" name='MyDeck'
```
```json
{
    "description": "",
    "id": 22,
    "name": "MyDeck"
}
```
### List of cards in a deck
```bash
http example.com:8000/flashcard/api/v1/decks/7/cards/ "$AUTH"
```
```json
[
   {
        "answer": "That's their kitchen.\r\nThe kitchen is huge.\r\nNowadays, it's hard to find kitchens like this.",
        "consec_correct_answers": 1,
        "easiness": 3.28,
        "id": 31,
        "question": "Это кухня.\r\nОчень большая.\r\nНелегко найти дом с такой кухней."
    },
    {
        "answer": "- Do you know why he's not coming? - I don't care.\r\nIt's because he hasn't spoken to me since I came out.\r\nHe didn't know before that?",
        "consec_correct_answers": 1,
        "easiness": 3.44,
        "id": 37,
        "question": "Вы знаете, почему он не приедет?\r\nМне все равно. Потому, что он не разговаривает со мной. С тех пор, как я открылся ему.\r\nОн не знал до этого?"
    }
]
```
### Create new card
```bash
http POST example.com:8000/flashcard/api/v1/decks/1/cards/ "$AUTH" "question"="How are you?" "answer"="Fine!"
```
```json
{
    "answer": "Fine!",
    "consec_correct_answers": 0,
    "easiness": 2.5,
    "id": 39,
    "question": "How are you?"
}
```
### Get list of cards planned to study for N next days (days=0 for today)
```bash
http example.com:8000/flashcard/api/v1/decks/7/cards/?days=N "$AUTH"
```
```json
[
    {
        "answer": "Who do you think gave Kai the idea to put Elena in that sleeping beauty coma?",
        "consec_correct_answers": 1,
        "easiness": 2.72,
        "id": 24,
        "question": "Как ты думаешь, кто подал Каю идею уложить Елену в эту спящую кому?"
    },
    {
        "answer": "Looks like a Bentley.",
        "consec_correct_answers": 1,
        "easiness": 3.6,
        "id": 25,
        "question": "Выглядит, как Бентли."
    }
]

```
## Installation
### Dependencies
* python 3
* dangorestframework
* bootstrap

### Installation
```bash
# clone repo
git clone https://github.com/zserg/flashcard.git

# create virtualenv, activate it
cd flashcard
virtualenv -p python3 venv
. venv/bin/activate

# install dependencies 
pip install -r requirements/local.txt
```
### Database setup (PostgreSQL as example)
```bash
sudo -u postgres psql
# run commands in psql
create database <base>;
create user <username> with password <password>;
grant all on database <base> to user <username>;
```
### Django setup
```bash
# create secret key
python -c 'import random; import string; print("".join([random.SystemRandom().choice(string.digits + string.ascii_letters + string.punctuation) for i in range(100)]))'

# create .env file with the following content:
 DEBUG=on
 ALLOWED_HOSTS='your_host_name'
 SECRET_KEY='your_secret_key'
 DATABASE_URL=psql://<ursername>:<password>@127.0.0.1:port/<base>

#migrate database
DJANGO_READ_DOT_ENV_FILE=True ./manage.py migrate

# create superuser
DJANGO_READ_DOT_ENV_FILE=True ./manage.py createsuperuser
```
### Run Django dev server
```bash
DJANGO_READ_DOT_ENV_FILE=True ./manage.py runserver
```
