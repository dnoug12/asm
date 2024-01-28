class hinhCN:
    def __init__(self,chieudai,chieurong):
        self.chieudai = chieudai
        self.chieurong = chieurong

    def get_dientich(self):
        return self.chieudai * self.chieurong

    def get_chuvi(self):
        return ((self.chieudai + self.chieurong) * 2)

    def display(self):
        print(f'chiều dài hình chữ nhật: {self.chieudai}')
        print(f'chiều rông hình chữ nhât {self.chieurong}')
        print(f'dien tich: {self.get_dientich()}')
        print(f'chu vi: {self.get_chuvi()}')


class hinhVuong(hinhCN):
    def __init__(self, canh):
        super().__init__(canh, canh)
        self.canh  = canh

    def get_dientich(self):
        return self.canh * self.canh

    def get_chuvi(self):
        return self.canh * 4

    def display(self):
        print(f'cạnh hình vuông: {self.canh}')
        print(f'dien tich: {self.get_dientich()}')
        print(f'chu vi: {self.get_chuvi()}')



# Bài 2
class SinhVienPoly:
    def __init__(self,name,majors):
        self.name = name
        self.majors = majors
        self.diem = 0

    def get_diem(self):
        return self.diem

    def get_hocluc(self):
        hocluc = ''
        if self.get_diem() >=9:
            hocluc = 'Xuất sắc'
        elif 8 <= self.get_diem() < 9:
            hocluc = 'Giỏi'
        elif 7 <= self.get_diem() < 9:
            hocluc = 'Khá'
        elif 5 <= self.get_diem() < 7:
            hocluc = 'Trung Bình'
        elif 5 < self.get_diem():
            hocluc = 'Yếu'
        return hocluc

    def input(self):
        self.name = input('Enter your name: ')
        self.majors = input('Enter your majors: ')


    def display(self):
        print(f'Tên sinh viên: {self.name}, chuyên ngành: {self.majors}')
        print(f'Tổng điểm trung bình: {self.get_diem()}')
        print(f'Học lực: {self.get_hocluc()}')


# Bài 3
class SinhVienIT(SinhVienPoly):
    def __init__(self,name,majors,java,html,css):
        super().__init__(name,majors)
        self.java = java
        self.html = html
        self.css = css

    def input(self):
        self.java = float(input('Java: '))
        self.html = float(input('Html: '))
        self.css = float(input('Css: '))


    def get_diem(self):
        return round((2 * self.java + self.html + self.css) / 4,2)

class SinhVienBiz(SinhVienPoly):
    def __init__(self,name,majors,sales,marketing):
        super().__init__(name,majors)
        self.sales = sales
        self.marketing = marketing

    def input(self):
        self.sales = float(input('Sales: '))
        self.marketing = float(input(''))


    def get_diem(self):
        return round((2 * self.marketing + self.sales) / 3,2)

# sv1 = SinhVienIT('','','','','')
# sv1.nhap()
# sv1.input()
# sv1.display()
#
# sv2 = SinhVienBiz('','','','')
# sv2.nhap()
# sv2.input()
# sv2.display()