from jwt import encode

### Funcion para crear token ###
def create_token(data:dict):
    token: str=encode(payload=data,key="my_secret", algorithm="HS256")
    return token