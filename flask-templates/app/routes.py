from app import app

@app.route('/')
def index():
    user = {
        'name':'Chandra'
    }
    return '''
    <html>
    <head>
    <title>Colorful Hello, World!</title>
    </head>
    <body>
    <h1 style="color:#093657"> Hello, World! '''+user['name']+'''</h1>
    </body>
    </html>
    '''
