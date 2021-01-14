score = 90
grade = 'A'

print("普通字符串:")
print("你的成绩为:", score, " 等级为:", grade, "\n查询完毕")
print("\n原始字符串:")
print("你的成绩为:", score, " 等级为:", grade, r"\n查询完毕")

# 格式化字符串
print("\n使用格式化操作符[麻烦，不推荐使用]:")
print("你的成绩为:{} 等级为:{}\n查询完毕".format(score, grade))

print("\n使用 format() 函数[不够直观]:")
print("你的成绩为:%d 等级为:%s\n查询完毕" %(score, grade))

print("\n使用格式字符串[推荐]:")
print(f"你的成绩为:{score} 等级为:{grade}\n查询完毕")