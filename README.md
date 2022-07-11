# Instalação do Flask

````
pip install Flask
````

## Definindo variáveis de ambiente e iniciando

Linux/Bash:
````
export FLASK_APP=main.py
export FLASK_ENV=development
flask run
````

Windows Powershell:
````
$env:FLASK_APP=".\main.py"
$env:FLASK_ENV="development"
flask run
````

Agora você tem o seu servidor de desenvolvimento do Flask rodando e poderá acessar em http://127.0.0.1:5000/


# Criando rotas
Um modo de definir uma rota é como segue

````
@app.route('/about')
def about():
    return "About Page"
````

Nesse caso, estamos definindo uma rota /about a partir do diretório base. Ao realizar uma requisição do tipo GET, o usuário irá receber a mensagem "About Page".

# Criando rotas passando variáveis
Nesse caso, durante a criação da rota, colocar a variável entre <> e solicitar como parâmetro da função 
````
@app.route("/user/<username>")
def user_profile(username):
    return f"Welcome {username}"
````

# Retornando páginas HTML

Primeiro é necessário importar a função do flask
````
from flask import render_template
````

Em seguida, basta criar um diretório chamado "templates" onde ficarão todos os templates HTML do seu aplicativo e dentro do método retornar 

````
    return render_template('example.html')
````

# Lidando com diferentes métodos de requisição

Para definir quais métodos de requisição uma rota irá aceitar, defina uma lista de métodos no decorator da rota

````
@app.route("/user/<username>",methods=['GET','POST'])
````

Para verificar qual o tipo de requisição foi realizada importe 

````
from flask import request
````

E verifique por meio do request.method