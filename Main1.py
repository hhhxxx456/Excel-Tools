# coding=gbk
import sys
import xlwings as xw
from Pre_Init import *
from All_Merge import *

# main_table_file=input()
# key=input()
# sub_table_file_list=[]
# for line in sys.stdin:
#     sub_table_file_list.extend(line.split())
# main_table_file=r'G:\�������ƴ���\�����ļ�\ģ��(ĸ��).xlsx'
# # key=2
# # sub_table_file_list=[
# # r'G:\�������ƴ���\�����ļ�\�ӱ�1_B.xlsx',
# # r'G:\�������ƴ���\�����ļ�\�ӱ�2_���CD.xlsx',
# # r'G:\�������ƴ���\�����ļ�\�ӱ�3_��һCD.xlsx',
# # r'G:\�������ƴ���\�����ļ�\�ӱ�4_��һ2��A.xlsx',
# # r'G:\�������ƴ���\�����ļ�\�ӱ�5_��һ3��A .xlsx',
# # r'G:\�������ƴ���\�����ļ�\�ӱ�6_���2��A .xlsx',
# # r'G:\�������ƴ���\�����ļ�\�ӱ�7_���3��A.xlsx']
# # need_add=(4,)


# need_add=tuple(input())
def begin(main_table_file,sub_table_file_list):
    # main_table_file=r'G:\�������ƴ���\�����ļ�2\m1.xlsx'
    key=2
    need_add=()
    print(main_table_file)
    print(sub_table_file_list)
    for name in sub_table_file_list:
        print(name)
    # sub_table_file_list=[
    # r'G:\�������ƴ���\�����ļ�2\z1.xlsx',
    # r'G:\�������ƴ���\�����ļ�2\z2.xlsx',
    # r'G:\�������ƴ���\�����ļ�2\z3.xlsx',
    # r'G:\�������ƴ���\�����ļ�2\z4.xlsx',
    # r'G:\�������ƴ���\�����ļ�2\z5.xlsx'
    # ]

    app=xw.App(visible=False)
    main_wb=app.books.open(main_table_file)

    mem_map={}
    try:
        print('Ԥ����')
        col_num,row_start=Pre_Init(wb=main_wb)
        print('��ʼ�ϲ�')
        all_merge(wb=main_wb,row_start=row_start,col_num=col_num,file_name_list=sub_table_file_list,mem_map=mem_map,key=key,need_add_col=need_add)
        print('�ϲ����')

    finally:
        print('finally')
        main_wb.save()
        main_wb.close()
        app.quit()
        app.kill()