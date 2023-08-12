from jwt import encode,decode

### Funcion para crear token ###
def create_token(data:dict):
    token: str=encode(payload=data,key="my_secret", algorithm="HS256")
    return token

# Funcion para validar Token ###
def validate_token(token: str)-> dict:
    data: dict = decode(token,key="my_secret", algorithms=['HS256'])
    return data

