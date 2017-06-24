from flask import render_template, request
from . import project
import re

@project.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if validate(request.files['file'].filename):
            list_table = create_list(request.files['file'], request.form['sep'])
            return render_template('table.html', title='Table from file', content=list_table)
        else:
            return render_template('table.html', title='Error format file', error='Error format file')
    return render_template('index.html', title='Convert csv to html')


def validate(file):
    if re.search(r'\.csv$', file, re.I):
        return True

def create_list(raw, sep):
    return [x.split(sep) for x in raw.read().decode('utf-8').split('\n')][:-1]

