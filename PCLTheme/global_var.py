"""
全局变量

_containers: 嵌套容器数: 未嵌套时为0, 每嵌套一个数值+1
_templates: 模板列表, 列表的每一个元素均为一个字典, key为模板, value为参数字典
_template_stack: 嵌套模板列表堆栈, 用于暂时存储嵌套容器中的模板列表, 列表的第n个子列表代表当前第n+1个嵌套
"""
_containers = 0
_templates = []
_template_stack = []