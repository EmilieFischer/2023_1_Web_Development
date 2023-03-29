from bottle import get, template


#########################
# skaber stien til contact-siden, så brugeren bare kan søge "about" i browseren i stedet for hele html-navnet
# inkluderer eksempel på hvordan man tilføjer title via variabler i app.py
@get("/contact")
def _():
    return template("contact-us", title="Contact us")