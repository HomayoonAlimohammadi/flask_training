from __future__ import annotations
from flask import Flask, Response, request, render_template
from courseware.utils import valid_form, load_data, add_model


app = Flask(__name__)


DATA_PATH = "./data/"
students = load_data(DATA_PATH, "students")
instructors = load_data(DATA_PATH, "instructors")
courses = load_data(DATA_PATH, "courses")

MODELS = {
    "students": students,
    "instructors": instructors,
    "courses": courses,
}


@app.route("/")
def index_view():
    return render_template("index.html")


@app.route("/<model>/")
def list_view(model: str):
    res = []
    if model not in MODELS:
        return render_template("404.html")
    elements = MODELS[model]
    for element in elements.values():
        record = []
        for key, value in element.__dict__.items():
            if key != "id":
                record.append((key, value))
        res.append(record)
    print(res)
    return render_template("list_view.html", elements=res)


@app.route("/<model>/add", methods=["GET", "POST"])
def add_student_view(model):
    if model not in MODELS:
        return render_template("404.html")

    if request.method == "GET":
        if model in ["students", "instructors"]:
            return render_template("add_member.html")
        return render_template("add_course.html")

    elements = MODELS[model]
    form = request.form
    if not valid_form(form):
        if model in ["students", "instructors"]:
            return render_template("add_member.html", message="Invalid credentials!")
        return render_template("add_course.html", message="Invalid credentials!")

    elements = add_model(model, elements, form, DATA_PATH)
    return render_template(
        "list_models.html",
        message=f"Added {model} successfully!",
        elements=elements,
    )
