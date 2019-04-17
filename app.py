from flask import Flask, render_template_string
from flask_s3 import FlaskS3
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
s3 = FlaskS3(app)

@app.route('/')
def index():
    template_str="""{{ url_for('static', filename="goat.jpg") }} """

    return render_template_string(template_str)

@app.route('/class')
def index2():
    template_str="""{{ url_for('static', filename="hopethisworks.jpg") }} """

    return render_template_string(template_str)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5110)
