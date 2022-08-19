import re
while True:
    try:
        str_ = input()
        print(len(re.sub('[^a-z]',"", str_)),len(re.sub('[^A-Z]',"", str_)),len(re.sub('[^0-9]',"", str_)), len(str_.split(' ')) - 1)
    except EOFError:
        break
