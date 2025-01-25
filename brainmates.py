class BrainMate:
    def __init__(self, name, subjects, study_time, location):
        self.name = name
        self.subjects = subjects
        self.study_time = study_time
        self.location = location

    def __repr__(self):
        return f"{self.name} ({', '.join(self.subjects)}, {self.study_time}, {self.location})"


class BrainMatesFinder:
    def __init__(self):
        self.mates = []

    def add_mate(self, mate):
        self.mates.append(mate)

    def find_mates(self, subject, study_time, location=None):
        matches = []
        for mate in self.mates:
            if subject in mate.subjects and mate.study_time == study_time:
                if location:
                    if mate.location == location:
                        matches.append(mate)
                else:
                    matches.append(mate)
        return matches