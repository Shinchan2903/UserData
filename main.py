from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)


class UserForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    project = StringField(label="Project", validators=[DataRequired()])
    skills = StringField(label="Skills", validators=[DataRequired()])
    role = StringField(label="Role Assigned", validators=[DataRequired()])
    joining_date = DateField(label="Joining Date", validators=[DataRequired()])
    end_date = DateField(label="End Date", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["POST", "GET"])
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        with open('userdata.csv', 'a', encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.name.data}|{form.project.data}|{form.skills.data}|{form.role.data}|{form.joining_date.data}|{form.end_date.data}")
        return redirect(url_for('user_data'))
    return render_template('add.html', form=form)


@app.route("/user_data")
def user_data():
    with open('userdata.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter='|')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('users.html', users=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)


