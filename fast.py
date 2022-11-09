from fastapi import FastApi

app=FastApi(title='Fast api')
@app.get('/')
def index():
    return 'First page'

if __name__=='__main__':
    app.run()