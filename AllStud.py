from StudentInfo import StudentInfo
from ArtStud import ArtStud
from SciStud import Scistud

def main():
    shiv = StudentInfo(1, 'shiv', 30, 99, 'Peth')
    sachin = ArtStud(2,'Sachin',29,70,'ART','Walwa')
    pruthvi = Scistud(3,'Pruthviraj',28,89,'Science','Peth')
    shiv.showdetails()
    sachin.showdetails()
    pruthvi.showdetails()

if __name__ == '__main__':
    main()







