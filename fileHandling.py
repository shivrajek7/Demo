from openpyxl import Workbook

book = Workbook()
sheet = book.active



rows = (
    ('SR.', 'UserName', 'Passward','Expected-Msg'),
    ( 1,'admin','admin123','Success'),
    (2,'admin123','admin','Invalid User name or Passaward'),
    (3,'NA','admin123','Username field cant be empty'),
    (4,'admin','NA','Passward field cant be empty'),
    (5,'abcpqr','xyz','Invalid')
)

for row in rows:
    sheet.append(row)


book.save("Emailsample.xlsx")
