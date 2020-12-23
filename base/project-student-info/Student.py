#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:Administrator
    @file:Student.py
    @time:2020/12/21
"""

def main():
    while True:
        menm()
        choice = int(input('请选择：'))
        if choice in range(8):
            if choice == 0:
                answer = input('确定退出系统吗：y/n')
                if answer == 'y' or answer == 'yes':
                    print('谢谢使用本系统！！')
                    break
                else:
                    continue
            elif choice == 1:   #todo
                # 录入学生信息
                insert()
            elif choice == 2: #todo
                # 查找学生信息
                search()
            elif choice == 3:   #todo
                # 删除学生信息
                delete()
            elif choice == 4:   #todo
                # 修改学生信息
                modify()
            elif choice == 5:   #todo
                # 排序
                sort()
            elif choice == 6:   #todo
                # 统计学生总人数
                total()
            elif choice == 7:   #todo
                # 显示所有学生信息
                show()


def menm():
    print('-----------------主菜单----------------')
    print('================功能菜单=================')
    print('\t\t\t\t1.录入学生信息')
    print('\t\t\t\t2.查找学生信息')
    print('\t\t\t\t3.删除学生信息')
    print('\t\t\t\t4.修改学生信息')
    print('\t\t\t\t5.排序')
    print('\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t0.退出系统')
    print('--------------------------------------')

def insert():
    student_list=[]
    while True:
        student_id = input('请输入学生ID或姓名（例如1001）：')
        if not student_id:
            break
        else:
            student_info = input('请输入学生信息：')
            student_list.append(student_info)
            break

def search():
    pass
def delete():
    pass
def modify():
    pass
def sort():
    pass
def total():
    pass
def show():
    pass


if __name__ == '__main__':
    main()