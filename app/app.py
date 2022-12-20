from typing import List

from flask import Flask, redirect, render_template, request, session, url_for, Response, send_file
import os
import io

from models import Course
from models.Section import Section

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/")
def home():
    """route to the homepage"""
    return render_template("index.html")


def get_class(dept_name: str, course_id: int) -> Course:
    """
    Description of what the function does

    Args:
        dept_name: The name of the department
        course_id: The id of the course

    Returns:
        A Course object corresponding to the given department name and id
    """
    # all dept info including courses and
    all_dept_info = request.get("https://web-app.usc.edu/web/soc/api/classes/" + dept_name.lower() + "/20231"
                                                                                                     "?refresh"
                                                                                                     "=Mary4adAL1ttle"
                                                                                                     "Lamp"
                                                                                                     "&=&=0765631822")
    # list of courses
    all_dept_courses = all_dept_info["OfferedCourses"]["course"]
    # Course that corresponds to given dept name and course id
    found_course = None
    for course in all_dept_courses:
        course_data = course["CourseData"]
        if int(course_data["number"]) == course_id:
            # if we have found the course, separate the sections and create a Course instance for this course
            lecture_sections = []
            lab_sections = []
            quiz_sections = []
            discussion_sections = []
            for section in course_data["SectionData"]:
                new_section = Section(section["id"], section["dclass_code"], section["type"],
                                      section["spaces_available"], section["day"], section["start_time"],
                                      section["end_time"], section["location"])
                if section["type"] == "Lec":
                    lecture_sections.append(new_section)
                elif section["type"] == "Lab":
                    lab_sections.append(new_section)
                elif section["type"] == "Qz":
                    quiz_sections.append(new_section)
                elif section["type"] == "Dis":
                    discussion_sections.append(new_section)
            # make course with given sections
            found_course = Course(int(course_data["number"]), course_data["title"], course_data["description"],
                                  course_data["units"], course_data["prereq_text"], lecture_sections,
                                  lab_sections, quiz_sections, discussion_sections)

    # return the course with given dept name and course id
    return found_course

def get_all_classes(students_courses: List) -> List:
    """
    Description of what the function does

    Args:
        students_courses: List of course names/ids inputted by the user (eg. ["CSCI 103", "CSCI 170", "WRIT 150"])

    Returns:
        A List of Course objects corresponding to the names of courses inputted by the user
    """
    all_courses = []
    for course in students_courses:
        course_as_list = course.split()
        dept_name = course_as_list[0]
        course_id = int(course_as_list[1])
        all_courses.append(get_class(dept_name, course_id))
    return all_courses


@app.route('/<path:path>')
def catch_all(path):
    """catch errors and redirect to home page"""
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
