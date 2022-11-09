from fastapi import FastAPI, Request
from datetime import datetime

storage=FastAPI(title='Fast api')
@storage.get('/')
def index():
    return 'My name is Grace'
@storage.get('/today')
def today():
    return str(datetime.now())
@storage.get('/myname')
def names(first_name:bool =False,last_name:bool=False):
    full_name=""
    if first_name:
        full_name+='Grace'
    if last_name:
        full_name+=' Umutesi'
    if full_name:
        full_names = "Hello my name Grace Umutesi"
    return full_name


# if __name__=='__main__':
#     app.run()