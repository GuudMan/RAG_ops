import os


for roots, dirs, files in os.walk("./test_data"):
    for file in files:
        if file.endswith(".txt"):
            file_i = os.path.join(roots, file)
            with open(file_i, 'r') as fr:
                lines = fr.readlines()

            # 剔除空行
            lines = [line for line in lines if line.strip() != '']

            # 将处理后的内容写入原文件
            with open(file_i, 'w') as fb:
                fb.writelines(lines)

            print("完成文件：", file_i)



