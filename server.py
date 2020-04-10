from flask import Flask,render_template,request,redirect
import pickle
import util
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        text = str(request.form['review'])
        return redirect('/review/{}'.format(text))
    else:
        return render_template("index.html")
@app.route('/review/<string:review>')
def get_review(review):
    sentiment = str(util.get_sentiment(review))
    return render_template("sent.html",sentiment = sentiment)

if __name__ == "__main__":
    app.run(debug=True)



