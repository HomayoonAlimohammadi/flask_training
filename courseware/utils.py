from __future__ import annotations
from typing import Any
from courseware.classes import Course, Student, Instructor
import uuid
import json


def valid_form(form) -> bool:
    if form["first_name"] and form["last_name"]:
        return True
    return False


def load_data(base_path: str, name: str) -> dict[str, Any]:
    data = {}
    MODELS = {"students": Student, "instructors": Instructor, "courses": Course}
    with open(f"{base_path}{name}.json") as f:
        records = json.load(f)
        model = MODELS[name]
        for record in records:
            record_obj = model(**record)
            data[record["id"]] = record_obj
    return data

def serialize_data(data: dict[str, Any]) -> dict[str, dict[str, str]]:
    serialized_data = data.copy()
    for key, value in serialized_data.items():
        serialized_data[key] = value.__dict__
    return serialized_data

def update_data(data: dict[str, Any], base_path: str, name: str) -> dict[str, Any]:
    serialized_data = serialize_data(data)
    path = f"{base_path}{name}.json"
    with open(path, "w") as f:
        json.dump(serialized_data, f)
    return data


def add_model(model: str, elements: dict[str, Any], form, base_path: str) -> None:
    MODELS = {"students": Student, "instructors": Instructor, "courses": Course}
    id = uuid.uuid4()
    model_class = MODELS[model]
    record = model_class(id=id, **form)
    elements[id] = record
    update_data(elements, base_path, model)
    return elements


def set_course_instructor(course: Course, instructor: Instructor) -> None:
    course.instructor_id = instructor.id
