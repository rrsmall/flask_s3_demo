from flask import Flask, render_template_string
from flask_s3 import FlaskS3

app = Flask(__name__)
app.config['FLASKS3_BUCKET_NAME'] = 'cus1166-flask-s3-example'
app.config['AWS_SECRET_KEY_ID'] = 'AWS_SECRET_KEY_ID'
app.config['AWS_SECRET_ACCESS_KEY'] = 'AWS_SECRET_ACCESS_KEY'
s3 = FlaskS3(app)

@app.route('/')
def index():
    template_str="""{{ url_for('static', filename="goat.jpg") }}"""
    return render_template_string(template_str)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5110)
