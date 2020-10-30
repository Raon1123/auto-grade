class Student:
    def __init__(self, id_, name_):
        self.id = id_
        self.name = name_
        self.score_list = []
        self.folderpath = ''

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_folderPath(self, path):
        self.folderpath = path

    def get_folderPath(self):
        return self.folderpath

    def append_scoreList(self, l):
        self.score_list.append(l)

    def printId(self):
        print(self.id)

    def printScore(self):
        print(str(self.id) + ": " + str(self.score))

    def get_score(self):
        score = 0
        for l in self.score_list:
            for s in l:
                score += s
        return score

    def individualReport(self):
        report_path = self.get_folderPath() + '/individual_report.txt'
        report = open(report_path, 'w')
        report.write('=== Report Id ' + self.id + ' ===\n')
        score = 0
        for l in self.score_list:
            for s in l:
                score += s

        report.write('=== Total: ' + str(score) + ' ===\n')
        for i, l in enumerate(self.score_list):
            report.write('=== Problem ' + str(i+1) + ' ===\n')
            for j, n in enumerate(l):
                report.write('Task ' + str(j+1) + ' Score: ' + str(n) + '\n')