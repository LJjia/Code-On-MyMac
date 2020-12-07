#!/usr/bin/env python
# -*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  data_sheet.py
#       Author @  Jia Liangjun
#  Create date @  2020/08/16 13:09
#        Email @  LJjiahf@163.com
#  Description @  数据统计
# ********************************************************************

import random
import copy


class Course():
    def __init__(self, school_schedule, teacher_list, teacher_class_num_dict, class_num=5):
        '''
        排课对象初始化
        :param school_schedule:日程表,表示哪几天上课.每个班相同
        :param teacher_list:老师名对应列表
        :param teacher_class_num:对应每个老师每周上课数量的列表,此变量为字典
        :param class_num:班级数量
        '''
        self.school_schedule = school_schedule
        self.class_num = class_num
        self.teacher_list = teacher_list
        self.teach_num = len(self.teacher_list)
        self.teacher_class_dict = teacher_class_num_dict
        self.class_schedule = []
        ret=self.check_course_num()
        if ret<0:
            return

        self.prt_school_shcedule()
        self.structure_course_pool()


    def prt_school_shcedule(self):
        print("学校课程表")
        day_of_class = len(self.school_schedule)
        # 默认3个时间段,早中晚
        for period in range(len(self.school_schedule[0])):
            for day in range(day_of_class):
                print("%s"% self.school_schedule[day][period],end='\t')
            print()
    def prt_class_shcedule(self,class_cnt):
        print("班级%s课程表"%(class_cnt+1))
        schedule=self.class_schedule[class_cnt]
        day_of_class = len(schedule)
        # 默认3个时间段,早中晚
        for period in range(len(schedule[0])):
            for day in range(day_of_class):
                print("%s"% schedule[day][period],end='\t')
            print()

    def check_course_num(self):
        '''
        检查学校日志表和老师安排的课时是否相等
        :return:
        '''
        self.school_schedule_num = 0
        # self.school_schedule: 表示学校日程表的list,其中每个元素为每天的日程,1表示早中或者晚上上课
        for day in self.school_schedule:
            for time in day:
                if time == 1:
                    self.school_schedule_num += 1
        self.all_course_num = self.class_num * self.school_schedule_num
        teacher_class_num = 0
        for teacher in self.teacher_list:
            teacher_class_num += self.teacher_class_dict[teacher]
        print('calc teacher class num %s, calc school_schedule_num %s'%(teacher_class_num, self.all_course_num))
        if teacher_class_num != self.all_course_num:
            print('not equal')
            return -1
        return self.all_course_num

    def structure_course_pool(self):
        '''
        构造上课列表池,每次排课从该池中取出一个变量
        :return:
        '''
        self.course_pool = []  # 存储teahcername 每个teachername对应一个老师的一节课程
        for teacher in self.teacher_list:
            this_teacher_coursenum = self.teacher_class_dict[teacher]
            for course_cnt in range(this_teacher_coursenum):
                self.course_pool.append(teacher)
        #print("find teacher course %s"% self.course_pool)
        random.shuffle(self.course_pool)

    def start_arrange_class(self,class_cnt):
        # 实现列表的深拷贝
        arrange_num=0
        tmp_schedule=copy.deepcopy(self.school_schedule)
        for day in range(len(self.school_schedule)):
            for period in range(len(self.school_schedule[day])):
                if self.school_schedule[day][period]==1:
                    # 将第一个元素pop出来
                    course = self.course_pool.pop(0)
                    random.shuffle(self.course_pool)
                    tmp_schedule[day][period]=course
                    arrange_num +=1
        self.class_schedule.append(tmp_schedule)
        print("end range class arrange %s arrange num %s pool remain %s"%(class_cnt+1,arrange_num,len(self.course_pool)))
        self.prt_class_shcedule(class_cnt)

    def arrange_class(self):
        for i in range(self.class_num):
            self.start_arrange_class(i)
        return self.class_schedule



def test_demo():
    school_schedule = [[1, 1, 0], [1, 1, 0], [1, 1, 0], [1, 1, 0], [1, 1, 0], [1, 1, 0], [0, 0, 0]]
    teacher_list = ['jia', 'liu', 'wang', 'zhang', 'li']
    teacher_dict = {'jia': 10, 'liu': 8, 'wang': 5, 'zhang': 11, 'li': 2}
    national_day = Course(school_schedule=school_schedule, teacher_list=teacher_list, teacher_class_num_dict=teacher_dict,
                          class_num=3)
    national_day.arrange_class()

if __name__ == '__main__':
    test_demo()