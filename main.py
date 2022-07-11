from flask import Flask, render_template, request, jsonify,flash
import random

# Access point da aplicação
app = Flask(__name__)
app.secret_key = "super secret key"

# Criação de rotas
@app.route("/")
def home():
    return render_template('home.html',username='Yuri')

@app.route("/math-game", methods = ['GET','POST'])
def math_game():
    if request.method == "POST":
        # verificar a resposta
        if "answer" in request.form and "correct_answer" in request.form:
            if request.form['answer'] ==  request.form['correct_answer']:
                flash("Correto!!!")
            else:
                flash("EROU!")
    
    num1 = random.randint(0,100)
    num2 = random.randint(0,100)

    correct_answer = num1 + num2

    return render_template('math.html',num1=num1, num2=num2,correct_answer=correct_answer)

@app.route("/json-test")
def json_test():
    return jsonify({'teste':'0.1', 'author':'yuri'})

    