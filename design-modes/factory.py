from abc import ABCMeta, abstractmethod

class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):
    def describe(self):
        print("Personal")

class AlbumSection(Section):
    def describe(self):
        print("Album")

class PatentSection(Section):
    def describe(self):
        print("Patent")

class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()
    
    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)

class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())

class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())

if __name__ == "__main__":
    tp = input("[LinkedIn or FaceBook]")
    profile = eval(tp.lower())()
    print(type(profile))
    print(profile.getSections())
    for sect in profile.getSections():
        sect.describe()