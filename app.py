
from flask import Flask, render_template, request, redirect, flash
from flask import session,url_for, escape
from predictor import predictor
from info import info
from flask import jsonify
app = Flask(__name__)

class App():

    @app.route('/')
    def main():
        return render_template('index.html')

    @app.route('/index')
    def home():
        return render_template('index.html')

    @app.route('/predict', methods = ['GET', 'POST'])
    def predict():
        return render_template("predict.html")

    @app.route('/videos', methods = ['GET', 'POST'])
    def videos():
        return render_template("videos.html")

    @app.route('/score', methods = ['GET', 'POST'])
    def score():
        return render_template("score.html")

    @app.route('/join', methods = ['GET', 'POST'])
    def join():
        return render_template("join.html")

    @app.route('/player_stats', methods = ['GET', 'POST'])
    def player():
        return render_template("visual1.html")

    @app.route('/player_info', methods=['GET', 'POST'])
    def player_info():
        name = request.form["player_name"]
        ob = info()
        res = ob.player_info(name)
        return jsonify(res)

    @app.route('/team_info', methods=['GET', 'POST'])
    def team_info():
        name = request.form["team_name"]
        ob = info()
        res = ob.team_info(name)
        print(res)
        return jsonify(res)

    @app.route('/destination', methods = ['GET', 'POST'])
    def destination():
        return render_template("destination.html")

    @app.route('/team_stats', methods = ['GET', 'POST'])
    def team():
        return render_template("visual2.html")

    @app.route('/predict_team',methods=['GET','POST'])
    def predict_team():
        print("i was called")
        predict_this = {"team":request.form["team"],
                        "hg":request.form["hg"],
                        "attendance":request.form["attendance"],
                        "hthg":request.form["hthg"],
                        "htag":request.form["htag"]
                        }
        print(predict_this)
        ob = predictor().predict(predict_this)
        return ob
