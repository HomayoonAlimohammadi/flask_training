from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Student:
    id: str
    first_name: str
    last_name: str
    courses: list[Course] = field(default_factory=list)


@dataclass
class Instructor:
    id: str
    first_name: str
    last_name: str
    courses: list[Course] = field(default_factory=list)


@dataclass
class Course:
    id: str
    name: str
    instructor_id: str = ""
    students: list[str] = field(default_factory=list)
