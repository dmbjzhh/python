# -*- coding: utf-8 -*-

import datetime

class PersonTypeError(TypeError):
    pass

class PersonValueError(ValueError):
    pass

# 公共人员类
class Person():
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