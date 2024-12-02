from flask import Flask, render_template, request, redirect, url_for, flash

from messages import get_messages, add_message

app = Flask(__name__)
app.secret_key = 'winwinwin'

@app.route('/phone')
def from_phone():
    return render_template('messages.html', device = 'телефона', messages=get_messages('from_phone.txt'))

@app.route('/comp')
def from_comp():
    return render_template('messages.html', device = 'компьютера', messages=get_messages('from_comp.txt'))

@app.route('/p')
def from_phone_short():
    return from_phone()

@app.route('/c')
def from_comp_short():
    return from_comp()

@app.route('/send_message_from_phone', methods=['POST'])
def send_message_from_phone():
    new_message = request.form['new_message']
    if new_message:
        add_message('from_comp.txt', new_message)
    return redirect(url_for('from_phone'))

@app.route('/send_message_from_comp', methods=['POST'])
def send_message_from_comp():
    new_message = request.form['new_message']
    if new_message:
        add_message('from_phone.txt', new_message)
    return redirect(url_for('from_comp'))

if __name__ == '__main__':
    app.run()