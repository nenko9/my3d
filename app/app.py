from flask import Flask, render_template, request, request_started
from search_engine import GetFromThingiverse

app=Flask(__name__)

@app.route('/', methods=["GET","POST"])
def IndexPage():
    if request.method=="POST":
        data=GetFromThingiverse(request.form['fdata'])
        return render_template('content.html', data=data)
    else:
        return render_template('search.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")