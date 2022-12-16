class Section(object):
    def __init__(self, id, clearance_code, type,
                 spaces_available, day, start_time,
                 end_time, location):
        """
        Constructs a new Section object
        Parameters: 8
        id: id of the section (int)
        clearance code: either R or D (string)
        type: Lec, Lab, Dis, or Qz (string)
        spaces_avaiable: number of spots left (int)
        day: day the section meets (M, T, W, TH or F) (string)
        start_time: time section starts in military time (ex: "12:30") (string)
        start_time: time section ends in military time (ex: "13:50") (string)
        location: the room the section meets at (string)
        """
        self._id = id
        self._clearance_code = clearance_code
        self._type = type
        self._spaces_available = spaces_available
        self._day = day
        self._start_time = start_time
        self._end_time = end_time
        self._location = location


    @property
    def id(self):
        return self._id

    @property
    def clearance_code(self):
        return self._clearance_code

    @property
    def type(self):
        return self._type

    @property
    def spaces_available(self):
        return self._spaces_available

    @property
    def day(self):
        return self._day

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time

    @property
    def location(self):
        return self._location








