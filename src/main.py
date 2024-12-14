import logging
from flask import Flask
from flask import render_template

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log")
    ]
)

@app.route("/")
def index():
    app.logger.info("HI THERE!")
    return render_template('index.html', person="JAKE")

if __name__ == "__main__":
    app.run()
