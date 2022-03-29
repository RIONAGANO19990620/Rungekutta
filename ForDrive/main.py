from ForDrive.Util import Util
from Model.Term.D1Dx import D1Dx


def main():
    term_list = [D1Dx(- Util.a)]
    teacher_data = Util.get_teacher_data(term_list)
    Util.plot_teacher_data(teacher_data)