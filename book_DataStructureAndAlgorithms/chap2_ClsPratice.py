# -*- coding: utf-8 -*-

import datetime

class PersonTypeError(TypeError):
    pass

class PersonValueError(ValueError):
    pass

# 公共人员类
class Person(object):    # python2中如果要使用继承的话，基类要写出从object继承
    _num = 0

    def __init__(self, name, sex, birthday, ident):
        if not (isinstance(name, str) and sex in ('男', '女')):
            raise PersonValueError(name, sex)
        try:
            birth = datetime.date(*birthday)
        except:
            raise PersonValueError('Wrong date:', birthday)
        self._name = name
        self._sex = sex
        self._birthday = birth
        self._id = ident
        Person._num += 1
    
    def id(self): return self._id
    
    def name(self): return self._name
    
    def sex(self): return self._sex
    
    def birthday(self): return self._birthday
    
    def age(self): return (datetime.date.today().year - self._birthday.year)
    
    def set_name(self, name):
        if not isinstance(name, str):
            raise PersonValueError("set_name", name)
        self._name = name
    
    def __lt__(self, another):
        if not isinstance(another, Person):
            raise PersonTypeError(another)
        return self._id < another._id
    
    @classmethod
    def num(cls):
        return Person._num
    
    def __str__(self):
        return ' '.join((self._id, self._name, self._sex, str(self._birthday)))
    
    def details(self):
        return ', '.join(("编号: " + self._id, "姓名: " + self._name,
                          "性别: " + self._sex, "出生日期: " + str(self._birthday)))

# 测试Person类

p1 = Person('xiaoyi', '女', (1996,4,1), '1997593883')
p2 = Person('xiaoyi2', '女', (1996,3,2), '4997593883')
p3 = Person('xiaoyi3', '女', (1996,5,3), '3997593883')
p4 = Person('xiaoyi4', '女', (1996,1,4), '4897593883')

plist = [p1, p2, p3, p4]
for p in plist:
    print(p)

print('After sorting: ')
plist.sort()
for p in plist:
    print(p.details())

print('{0} people had been created.'.format(Person.num()))

# 学生类

class Student(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return "1{:04}{:05}".format(year, cls._id_num)

    def __init__(self, name, sex, birthday, department):
        Person.__init__(self, name, sex, birthday, Student._id_gen()) # emmmm为什么要在Person类中init _id_gen
        self._department = department
        self._enroll_date = datetime.date.today()
        self._courses = {}
    
    def set_course(self, course_name):
        self._courses[course_name] = None
    
    def set_score(self, course_name, score):
        if course_name not in self._courses:
            raise PersonValueError('None course selected: ', course_name)
        self._courses[course_name] = score
    
    def scores(self): return [(cname, self._courses[cname]) for cname in self._courses]
    
    def details(self):
        return ', '.join((Person.details(self), '入学日期: ' + str(self._enroll_date), 
        '院系: ' + self._department, '课程记录: ' + str(self.scores())))

# 测试学生类
su1 = Student('heping1', '女', (1993,1,1), 'computer')
su2 = Student('heping2', '女', (1993,1,1), 'English')

print(su1)
print(su2)

su1.set_course('English')
su1.set_score('English','80')
print(su1.details())
# 教师类

class Staff(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls, birthday):
        cls._id_num += 1
        birth_year = datetime.date(*birthday).year
        return '0{:04}{:05}'.format(birth_year, cls._id_num)
    
    def __init__(self, name, sex, birthday, entry_date = None):
        super(Staff, self).__init__(name, sex, birthday, Staff._id_gen(birthday))
        #Person.__init__(self, name, sex, birthday, Staff._id_gen(birthday))
        if entry_date:
            try:
                self._entry_date = datetime.date(*entry_date)
            except:
                raise PersonValueError('Wrong data: ', entry_date)
        else:
            self._entry_date = datetime.date.today()
        self._salary = 1000
        self._department = 'Undefined'
        self._position = 'Undefined'

    def set_salary(self, amount):
        if not type(amount) is int:
            raise TypeError
        self._salary = amount
    
    def set_position(self, position):
        self._position = position
    
    def set_department(self, department):
        self._department = department
    
    def details(self):
        return ', '.join((super(Staff, self).details(), '入职日期: ' + str(self._entry_date), 
        '院系: ' + self._department, '职位: ' + self._position, '工资: ' + str(self._salary)))

# 该类的使用

s1 = Staff('ksm1', '女', (1996, 1, 1))
s2 = Staff('ksm2', '女', (1996, 1, 1))

print(s1)
print(s2)

s1.set_department('math')
s1.set_position('teacher')
s1.set_salary(2000)

print(s1.details())
print(s2.details())
