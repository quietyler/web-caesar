from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True
from caesar import rotate_string
form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
    <form method="post">
      <label> Rotate by:</label>
      <input type="text" name="rot" value="0" /> <br></br>
      <textarea name="text"> </textarea>
      <input type="submit" />
    </form>

    </body>
</html>"""
@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt(text, rot):
    encrypted_text = ''
    for char in text:
        encrypted_text += rotate_character(char, rot)
    return encrypted_text

app.run()
