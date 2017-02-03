from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.secret_key = "ABC"


@app.route('/')
def index():
    """Return HTML for homepage."""

    return render_template("index.html")


@app.route('/application-form')
def show_application_form():
    """Return HTML for application form using POST method."""

    jobtitles = ['Software Engineer', 'QA Engineer', 'Product Manager']

    return render_template("application-form.html", jobtitles=jobtitles)


@app.route('/application-success', methods=["POST"])
def show_app_success():
    """Return customized application-success page with user's information from application form."""
    
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    jobtitle = request.form.get("jobtitle")
    salaryreq = request.form.get("salaryreq")

    return render_template("application-response.html", firstname=firstname,
                                                        lastname=lastname,
                                                        jobtitle=jobtitle,
                                                        salaryreq=salaryreq)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
