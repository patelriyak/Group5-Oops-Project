from flask import Flask
# from controller.index_controller import index_page
from controller.user_controller import user_page
from controller.res_controller import res_page
from controller.about_controller import about_page
from controller.contact_controller import contact_page

app = Flask(__name__)

app.register_blueprint(user_page, url_prefix="/")
app.register_blueprint(res_page, url_prefix="/res")
app.register_blueprint(about_page, url_prefix="/about")
app.register_blueprint(contact_page, url_prefix="/contact")
# app.register_blueprint(event_page, url_prefix="/event")

if __name__ == "__main__":
    app.run(debug=True)