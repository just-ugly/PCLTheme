"""
全局变量

_containers: 嵌套容器数: 未嵌套时为0, 每嵌套一个数值+1
_templates: 模板列表, 列表的每一个元素均为一个字典, key为模板, value为参数字典
_template_stack: 嵌套模板列表堆栈, 用于暂时存储嵌套容器中的模板列表, 列表的第n个子列表代表当前第n+1个嵌套
_container_rows: _containers中每个容器的行数
_container_columns: _containers中每个容器的列数
_default_margin: 默认控件margin参数
"""
from chameleon import PageTemplate

_containers = 0
_templates = []
_template_stack = []
_container_rows = []
_container_columns = []

_cards = 0

_default_margin = [0, 0, 0, 15]
_default_text_margin = [0, 0, 0, 5]
_default_text_size = 16


# 供外部使用的一系列方法
def add_container():
    """
    _containers += 1
    """
    global _containers
    _containers += 1


def reduce_container():
    """
    _containers -= 1
    """
    global _containers
    _containers -= 1


def get_containers():
    """
    返回 _containers
    """
    return _containers


def add_template(template: PageTemplate, data: dict):
    """
    在 templates 里新增一个字典
    :param template: xaml模板
    :param data: 参数字典
    """
    global _templates
    _templates.append({template: data})


def add_template_stack(container_xaml: str):
    """
    在 template_stack 里新增一个字符串
    :param container_xaml: 嵌套容器的xaml模板
    """
    global _template_stack
    _template_stack.append(container_xaml)


def stack_template_stack(container_xaml: str):
    """
    将 template_stack 中的内容添加到 templates 中的最后一个元素
    :param container_xaml: 嵌套容器的xaml模板
    """
    global _template_stack
    _template_stack[-1] += container_xaml


def pop_template_stack():
    """
    将 template_stack 中的最后一个元素弹出
    """
    global _template_stack
    return _template_stack.pop()


def add_container_row(row: int):
    """
    在 container_rows 中新增一个元素
    :param row: 容器的行数
    """
    global _container_rows
    _container_rows.append(row)


def add_container_column(column: int):
    """
    在 container_columns 中新增一个元素
    :param column: 容器的列数
    """
    global _container_columns
    _container_columns.append(column)


def reduce_container_row():
    """
    删除 container_rows 中的最后一个元素
    """
    global _container_rows
    _container_rows.pop()


def reduce_container_column():
    """
    删除 container_columns 中的最后一个元素
    """
    global _container_columns
    _container_columns.pop()


def get_container_row():
    """
    返回 container_rows 中的最后一个元素
    """
    global _container_rows
    return _container_rows[-1]


def get_container_column():
    """
    返回 container_columns 中的最后一个元素
    """
    global _container_columns
    return _container_columns[-1]


def add_cards():
    """
    _cards += 1
    """
    global _cards
    _cards += 1


def get_cards():
    """
    返回 _cards
    """
    return _cards


def reduce_cards():
    """
    _cards -= 1
    """
    global _cards
    _cards -= 1


def get_default_margin():
    """
    返回 _default_margin
    """
    return _default_margin


def set_default_margin(margin: list):
    """
    设置 _default_margin
    :param margin: 默认margin
    """
    global _default_margin
    if len(margin) not in [4, 3, 2, 1]:
        raise ValueError("margin参数错误, list长度需为1~4")
    _default_margin = margin


def get_default_text_margin():
    """
    返回 _default_text_margin
    """
    return _default_text_margin


def set_default_text_margin(text_margin: list):
    """
    设置 _default_text_margin
    :param text_margin: 默认text_margin
    """
    global _default_text_margin
    if len(text_margin) not in [4, 3, 2, 1]:
        raise ValueError("text_margin参数错误, list长度需为1~4")
    _default_text_margin = text_margin


def get_default_text_size():
    """
    返回 _default_text_size
    """
    return _default_text_size


def set_default_text_size(text_size: int):
    """
    设置 _default_text_size
    :param text_size: 默认text_size
    """
    global _default_text_size
    _default_text_size = text_size


def margin_check_convert(margin: list[int]):
    if not isinstance(margin, list) or len(margin) not in [4, 3, 2, 1]:
        raise ValueError("margin参数错误, list长度需为1~4")

    # 转换margin参数
    if len(margin) == 1:
        changed_margin = f"{margin[0]},{margin[0]},{margin[0]},{margin[0]}"
    elif len(margin) == 2:
        changed_margin = f"{margin[0]},{margin[1]},{margin[0]},{margin[1]}"
    elif len(margin) == 3:
        changed_margin = f"{margin[0]},{margin[1]},{margin[0]},{margin[2]}"
    else:
        changed_margin = f"{margin[0]},{margin[1]},{margin[2]},{margin[3]}"

    return changed_margin


def row_column_check(row: int, column: int):
    if get_containers() == 0:
        if row != -1 or column != -1:
            raise ValueError("row/column参数错误, 需要在Grid中")
    else:
        # 先检查row参数
        container_row = get_container_row()
        if row == -1 and container_row != 1:
            raise ValueError("row参数错误, 需要在有row设置的容器中设置row参数")
        if row != -1 and container_row == 1:
            raise ValueError("row参数错误, 所属容器无row参数")
        if row != -1 and row >= container_row:
            raise ValueError("row参数错误, row值超出范围")
        # 检查column参数
        container_column = get_container_column()
        if column == -1 and container_column != 1:
            raise ValueError("column参数错误, 需要在有column设置的容器中设置column参数")
        if column != -1 and container_column == 1:
            raise ValueError("column参数错误, 所属容器无column参数")
        if column != -1 and column >= container_column:
            raise ValueError("column参数错误, column值超出范围")