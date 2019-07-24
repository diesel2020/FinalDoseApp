from flask import Flask, render_template, request
from wtforms import Form, FloatField, validators
from compute import calculatedose, calculate_date, print_days, full_dose, normal_round
from wtforms.fields.html5 import DateField
from flask_bootstrap import Bootstrap


app = Flask(__name__)

Bootstrap(app)


class InputForm(Form):
    # Start Dose Form field is assigned to r variable
    start_dose = FloatField(validators=[validators.InputRequired()])

    # Final Dose form field
    final_dose = FloatField(validators=[validators.InputRequired()])

    # Create DateField for calendar1
    calendar1 = DateField('DatePicker1', format='%Y-%m-%d')

    # Create DateField for calendar2
    calendar2 = DateField('DatePicket2', format='%Y-%m-%d')


@app.route('/index.html', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        # VARIABLES SECTION

        # This assigns variable 'r' to form field with 'r' data, in this case start_dose
        start_dose = form.start_dose.data
        # This assigns variable 'z' to form field with 'z' dat, in this case final_dose
        final_dose = form.final_dose.data
        # Assign calendar1 to value input into form.calendar1.data
        calendar1 = form.calendar1.data
        # Assign calendar2 to value input into form.calendar2.data
        calendar2 = form.calendar2.data

        # FUNCTIONS SECTION
        # This passes values from calendar1 and calendar2 form to calculate date and returns total days of taper
        output2 = calculate_date(calendar1, calendar2)

        # This generates a list with the number of days of the taper
        date_list = print_days(output2)

        # This returns a list q by calculating the dose
        q = calculatedose(start_dose, final_dose)

        # This returns a value to be used in calculating taper frequency
        result = output2 / (len(q))

        # This rounds up or down the returned value of result
        result2 = normal_round(result)

        # This returns a list of all the individual doses
        dose = full_dose(q, result2, output2)

        # This return function, passes the elements listed to the view_output.html file.  It does not change
        # the path in the browser, that stays on index.html
        return render_template("view_output.html", form=form, q=q , output2=output2, date_list=date_list , dose=dose,
                               result2=result2 ,zip=zip, calendar1=calendar1, calendar2=calendar2 ,
                               start_dose=start_dose,final_dose=final_dose)

    else:
        return render_template("index.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)

