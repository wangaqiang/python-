import os
from multiprocessing import Pool,Manager

def copy(file_name, old_folder_name, new_folder_name, q):
    """从文件夹中copy文件到新文件夹中"""
    # 打开当前路径下的要拷贝的文件夹下的某个文件
    fr = open(old_folder_name+"/"+file_name, "r")

    # 打开要复制的新的文件夹
    fw = open(new_folder_name+"/"+file_name, "w")

    # 读取旧文件夹中的内容并写到新文件夹中
    fw.write(fr.read())

    # 关闭文件
    fr.close()
    fw.close()

    # 完成一个给队列中扔一个
    q.put(file_name)

def main():
    # 0.获取要拷贝的文件夹名字
    old_folder_name = input("请输入要拷贝的文件夹名:")
    new_folder_name = old_folder_name+"-复件"

    # 1.创建新文件夹
    while True:
        try:
            os.mkdir(new_folder_name)
            break
        except Exception:
            new_folder_name = new_folder_name + "-复件"

    # 2.获取旧文件夹中的文件名
    file_name_list = os.listdir(old_folder_name) # 返回值为文件夹里面内容的列表 

    # 3.创建进程池
    po = Pool(3)

    # 4.建立进程间的通信
    q = Manager().Queue()

    # 5.向进程池中添加任务
    for file_name in file_name_list:
        po.apply_async(copy, (file_name, old_folder_name, new_folder_name, q))
    
    num = 0
    file_num = len(file_name_list)
    while num<file_num:
        q.get()
        num+=1
        print("\r拷贝进度为%.2f%%"%(num/file_num*100),end="")
    print("已完成拷贝")


if __name__ == "__main__":
    main()
