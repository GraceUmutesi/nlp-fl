from flask import Flask,request
from datetime import datetime

app= Flask('the app')
@app.route('/')
def index():
    return '''
    <h1>Food is good</h1>
    <p>My name is Grace and am a foodie</p>
    '''
@app.route('/content')
def contact_page():
    return 'contact me on my email'

@app.route('/date')
def date_page():
    date=str(datetime.now())
    return f'Today is {date}'


@app.route('/birthyear', methods=['POST','GET'])
def calc_birthyear():
    if request.method == 'POST':
        return f"you declared your age as {request.form.get('birthyear')}"
    elif request.method== 'GET':
        return '''
        <form action="/birthyear" method='POST'>
            <input type="number" name="birthyear" placeholder="Birth year e.g 2020">
            <button type="submit">Submit</submit>
        </form>
        '''

if __name__ == "__main__":
    app.run()