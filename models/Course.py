class Course(object):
    def __init__(self, id_param, title_param, description_param,
                 units_param, prereq_param, lecture_sections_param,
                 lab_sections_param, quiz_sections_param, discussion_sections_param):
        """Constructs a new Course object
        Parameters: 9
        id: id of the course such as 103 (int)
        title: title of the course such Introduction to Programming (string)
        description: description of the course (string)
        units: number of units for the course such as 2 or 4 units (int)
        prereq: the prerequisite classes for this course (list of ints (class ids))
        sections: section objects such as lectures, labs, quizzes, etc (list of objects)"""
        self._id = id_param
        self._title = title_param
        self._description = description_param
        self._units = units_param
        self._prereq = prereq_param
        self._lecture_sections = lecture_sections_param
        self._lab_sections = lab_sections_param
        self._quiz_sections = quiz_sections_param
        self._discussion_sections = discussion_sections_param


    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def units(self):
        return self._units

    @property
    def get_prereq(self):
        return self._prereq

    @property
    def lecture_sections(self):
        return self._lecture_sections

    @property
    def _lab_sections(self):
        return self._lab_sections

    @property
    def _quiz_sections(self):
        return self._quiz_sections

    @property
    def discussion_sections(self):
        return self._discussion_sections

    @lecture_sections.setter
    def lecture_sections(self, new_lecture_section):
        self._lecture_sections.append(new_lecture_section)

    @_lab_sections.setter
    def _lab_sections(self, new_lab_sections):
        self._lab_sections.append(new_lab_sections)

    @_quiz_sections.setter
    def _quiz_sections(self, new_quiz_sections):
        self._quiz_sections.append(new_quiz_sections)

    @discussion_sections
    def discussion_sections(self, new_discussion_sections):
        self._discussion_sections.append(new_discussion_sections)




