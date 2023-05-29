from flask import render_template
import config
from handlers.contentHandlers import getAllData

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

@app.route("/")
def home():
  content = getAllData()

  return render_template("home.html", content=content)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000, debug=True)
