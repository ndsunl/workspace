# 下面写法最后导入的 foo 将覆盖之前导入的 foo

from day06_06_module1 import foo
from day06_06_module2 import foo

# 输出 goodby, world!
foo()