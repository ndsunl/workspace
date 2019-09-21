#import abc

# 抽象类
class StudentBase(object):
    #__metaclass__ = abc.ABCMeta

    #@abc.abstractclassmethod
    def study(self):
        pass

    def play(self):
        print("play")


# 实现类
#class GoodStudent(StudentBase):
#    def study(self):
#        print("study hard!")

    
if __name__ == '__main__':
    #student = GoodStudent()
    student = StudentBase()
    student.study()
    student.play()