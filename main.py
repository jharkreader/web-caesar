from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <h1>Web Caesar</h1>
        <p>A Caesar cipher encrypts a message by rotating each character 13 places. This application will allow you to set the rotation factor and encrypt a message.</p>

        <form action="/" method="POST">
            <label for="rot">Rotate by: 
                <input type="text" name="rot" id="rot" value="0"/> 
            </label>
            <textarea name="text">{0}</textarea>
            <input type="submit" value="Encrypt my message!">
        </form>

    </body>
</html>

"""


@app.route("/")
def index():
    return form.format("")


@app.route("/", methods=["POST"])
def encrypt():
    rot_factor = request.form['rot']
    message = request.form['text']
    secret = rotate_string(message, rot_factor)

    return form.format(secret)


app.run()