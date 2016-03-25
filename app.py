import flask

app = flask.Flask(__name__)

@app.route('/')
def root():
    flask.render_template('root.html')
    


if __name__ == '__main__':
    app.run(debug=True)
