from flask import Flask, render_template, request

from typograph import typograph

app = Flask(__name__)
app.config.from_object('config')


@app.route('/', methods=['POST', 'GET'])
def form():
    input_text = request.form['text'] if request.method == 'POST' else ''
    formatted_text = typograph(input_text)
    return render_template('form.html',
                           input_text=input_text,
                           formatted_text=formatted_text)


if __name__ == "__main__":
    app.run()
