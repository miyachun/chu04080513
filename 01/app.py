from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():

    data = {
        'name': 'John Doe',
        'age': 20,
        'city': 'New York'
    }


    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run()
