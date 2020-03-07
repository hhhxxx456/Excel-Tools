#coding=gbk
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
import threading
import time
import Main1


def select_main_table():
    global main_table_file
    main_table_file = filedialog.askopenfilename(filetypes=[('excel file(.*xlsx)', '.xlsx')])  # ���ѡ��õ��ļ�
    main_table_file = main_table_file.replace('/', '\\')
    print(main_table_file)
    main_table_text.insert('insert','�����ǣ�' + main_table_file)
    select_main_table_button['text'] = '����ѡ������'
    print(main_table_file)
    print(len(main_table_file))
    return main_table_file


def select_sub_table():
    global sub_table_file_list
    sub_table_file_list = filedialog.askopenfilenames(filetypes=[('excel file (.*xlsx)', '.xlsx')])
    namelist = []
    str = ''
    for name in sub_table_file_list:
        name = name.replace('/', '\\')
        namelist.append(name)
        str = str + name + '\n'
    sub_table_file_list = namelist
    # ���ԭ��������
    sub_table_text.delete('1.0', 'end')
    sub_table_text.insert('insert', '�ӱ�: \n' + str)
    sub_table_text.update()
    #t['height'] = min(len(sub_table_file_list) + 1, 15)
    select_sub_table_button['text'] = '����ѡ���ӱ�'
    return namelist


def call_main_begin():
    global main_table_file, sub_table_file_list, window,begin_meger_button
    begin_meger_button.place_forget()
    time.sleep(2)
    label2 = tk.Label(window, text='���ںϲ�')
    label2.place(x=300,y=380)
    time.sleep(2)
    label2.place_forget()
    Main1.begin(main_table_file, sub_table_file_list)
    label2.config(text='�ϲ����')
    time.sleep(2)
    begin_meger_button.place(x=300, y=380)


def begin():
    if(len(main_table_file)==0):
        tkinter.messagebox.showwarning(title='Hi', message='����ûѡ')
        return
    if(len(sub_table_file_list)==0):
        tkinter.messagebox.showwarning(title='hi',message='ûѡ�ӱ�')
        return
    thread1 = threading.Thread(target=call_main_begin)
    thread1.start()

#����������
window = tk.Tk()
window.title('Excel tool')
window.geometry('800x500')

#������frame
frame = tk.Frame(window,width=800,height=500)
frame.pack()

#navigation_frame: ��ߵĵ�������
navigation_frame = tk.Frame(frame,width=100,height=500,bg='green')
content_frame = tk.Frame(frame,width=700,height=500)
navigation_frame.place(x=0,y=0)
content_frame.place(x=100,y=0)


#���õ��������ͼƬ
canvas = tk.Canvas(navigation_frame, bg='blue', height=500, width=100)
canvas.place(x=0,y=0)
image_file = tk.PhotoImage(file='img\p1.jpg')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)

#���������lookup��ť�ͺϲ���ť
lookup_button = tk.Button(navigation_frame,height=2,text='lookup\n��������',background='GhostWhite')
lookup_button.place(x=20,y=130)
meger_button = tk.Button(navigation_frame,height=2,text='�ϲ����',background='GhostWhite')
meger_button.place(x=20,y=260)

#ѡ������İ�ť������߶�Ӧ��text
select_main_table_button = tk.Button(content_frame,height=1,text=' ѡ������ ',background='GhostWhite',command=select_main_table)
select_main_table_button.place(x=600,y=47)
text_width = 55
main_table_text = tk.Text(content_frame,height=1,width=text_width,font=('Arial',12))
main_table_text_pos_x = 70
main_table_text.place(x=main_table_text_pos_x,y=50)

#�ӱ��text��
sub_table_text = tk.Text(content_frame,height=14,width=text_width,font=('Arial',12))
sub_table_text.place(x=main_table_text_pos_x,y=100)
#ѡ���ӱ�İ�ť
select_sub_table_button = tk.Button(content_frame,height=1,text=' ѡ���ӱ� ',background='GhostWhite',command=select_sub_table)
select_sub_table_button.place(x=600,y=130)
#ɾ���ӱ�İ�ť
delete_sub_table_button = tk.Button(content_frame,height=1,text=' ɾ���ӱ� ',background='GhostWhite')
delete_sub_table_button.place(x=600,y=180)
#ѡ���ļ��еİ�ť
select_folder_button = tk.Button(content_frame,height=1,text='ѡ���ļ���',background='GhostWhite')
select_folder_button.place(x=600,y=230)
#��ʼ�ϲ��İ�ť
begin_meger_button = tk.Button(content_frame,height=1,text='��ʼ�ϲ�',background='GhostWhite',command=begin)
begin_meger_button.place(x=300,y=380)

main_table_file = ''
sub_table_file_list = ''

tk.mainloop()