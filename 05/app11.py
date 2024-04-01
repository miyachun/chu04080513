from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('static/people108.csv')

@app.route('/')
def index(): 
    Nlist=df.iloc[:,2].tolist()
    Alist=df.iloc[:,3] .tolist()
    Blist=df.iloc[:,4] .tolist()
    Clist=df.iloc[:,5] .tolist()
    Dlist=df.iloc[:,6] .tolist()
    Elist=df.iloc[:,7] .tolist()
    Flist=df.iloc[:,8] .tolist()
    Glist=df.iloc[:,9] .tolist()
    Hlist=df.iloc[:,10] .tolist()

    return render_template("index11.html", xdata=Nlist,ydata01=Alist,ydata02=Blist,ydata03=Clist,ydata04=Dlist,ydata05=Elist,ydata06=Flist,ydata07=Glist,ydata08=Hlist)
  

if __name__ == "__main__":
    app.run(debug=True)