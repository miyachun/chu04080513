from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data=[{ 'name': '10801','value': 138881  },
        { 'name': '10802','value': 137512  },
        { 'name': '10803','value': 101301  },
        { 'name': '10804','value': 186020  },
        { 'name': '10805','value': 160695  },
        { 'name': '10806','value': 169084  },
        { 'name': '10807','value': 144669  },
        { 'name': '10808','value': 135557  },
        { 'name': '10809','value': 127176  },
        { 'name': '10810','value': 180991  },
        { 'name': '10811','value': 180144  },
        { 'name': '10812','value': 147301  }]
    return render_template("index01.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)