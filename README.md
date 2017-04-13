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



