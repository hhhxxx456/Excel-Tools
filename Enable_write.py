#�ļ��ڱ�����Ӧ�ô�ʱ����ֻ���ģ��޷���д��
#��������Ϊ�ж��ļ��Ƿ�ֻ������ʾʹ���߹ر��ļ�
def is_only_read(file_name):
    try:
        with open(file_name, "r+") as fr:
            return False
    except IOError as e:
        if "[Errno 13] Permission denied" in str(e):
            return True
        else:
            print(str(e))
            return False