# import os, random, shutil

# now_path = os.path.abspath("")
# print(now_path)

# path_1 = now_path + "\DownloadEncrpyModel"
# print(path_1)
# os.chdir(path_1) #進入要清空的目錄
# ds = list(os.listdir()) #獲得該目錄下所有檔案或資料夾列表
# for d in ds: #遍歷該列表
#     if os.path.isfile(d): #如果列表項是檔案
#         os.remove(d) #直接刪除
#     else: #如果不是檔案，肯定是資料夾
#        shutil.rmtree(d) #也直接刪除
# print("刪除1 Ok")

# # print("===================================")

# path_2 = now_path + "\RealServerModel"
# print(path_2)

# os.chdir(path_2)
# ds = list(os.listdir()) #獲得該目錄下所有檔案或資料夾列表
# for d in ds: #遍歷該列表
#     if os.path.isfile(d): #如果列表項是檔案
#         os.remove(d) #直接刪除
#     else: #如果不是檔案，肯定是資料夾
#        shutil.rmtree(d) #也直接刪除
# print("刪除2 Ok")


import os
#建立目錄'D:\test'
os.makedirs("./aaa/")