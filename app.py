from chalice import Chalice

app = Chalice(app_name="hello-world-chalice")


@app.route("/")
def index():
    return {"hello": "world"}
