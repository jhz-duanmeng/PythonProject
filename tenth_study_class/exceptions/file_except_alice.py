import os


def count_words(file_name):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        errors = "Sorry, the file " + file_name + " does not exist."
        print(errors)
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        words_num = len(words)
        print("The file " + file_name + " has about " + str(words_num) +
              " words.")


filename = "F:/WorkSpace/PythonProject/tenth_study_class/alice"
files = ["F:/WorkSpace/PythonProject/tenth_study_class/alice", "hello", "nihao"]
# count_words(filename)
for file in files:
    count_words(file)

# print("\n")
# pwd = os.getcwd()
# print(str(pwd))
