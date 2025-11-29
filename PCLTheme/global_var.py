"""
全局变量

_containers: 嵌套容器数: 未嵌套时为0, 每嵌套一个数值+1
_templates: 模板列表, 列表的每一个元素均为一个字典, key为模板, value为参数字典
_template_stack: 嵌套模板列表堆栈, 用于暂时存储嵌套容器中的模板列表, 列表的第n个子列表代表当前第n+1个嵌套
_container_rows: _containers中每个容器的行数
_container_columns: _containers中每个容器的列数

_default_XXX_margin: 该控件默认margin参数

_default_text_size: 默认字体大小
"""
from chameleon import PageTemplate

_containers = 0
_templates = []
_template_stack = []
_container_rows = []
_container_columns = []


_default_grid_margin = [0, 0, 0, 0]
_default_panel_margin = [25, 40, 23, 15]
_default_card_margin = [0, 0, 0, 15]
_default_hint_margin = [0, 8, 0, 2]
_default_text_margin = [0, 0, 0, 4]
_default_button_margin = [0, 4, 0, 10]

_default_button_padding = [0, 0, 0, 0]


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


# margin
def get_default_grid_margin():
    """
    返回 _default_margin
    """
    return _default_grid_margin


def set_default_grid_margin(margin: list):
    """
    设置 _default_margin
    :param margin: 默认margin
    """
    global _default_grid_margin
    if len(margin) not in [4, 3, 2, 1]:
        raise ValueError("margin参数错误, list长度需为1~4")
    _default_grid_margin = margin


def get_default_panel_margin():
    """
    返回 _default_panel_margin
    """
    return _default_panel_margin


def set_default_panel_margin(panel_margin: list):
    """
    设置 _default_panel_margin
    :param panel_margin: 默认panel_margin
    """
    global _default_panel_margin
    if len(panel_margin) not in [4, 3, 2, 1]:
        raise ValueError("panel_margin参数错误, list长度需为1~4")
    _default_panel_margin = panel_margin


def get_default_card_margin():
    """
    返回 _default_card_margin
    """
    return _default_card_margin


def set_default_card_margin(card_margin: list):
    """
    设置 _default_card_margin
    :param card_margin: 默认card_margin
    """
    global _default_card_margin
    if len(card_margin) not in [4, 3, 2, 1]:
        raise ValueError("card_margin参数错误, list长度需为1~4")
    _default_card_margin = card_margin


def get_default_hint_margin():
    """
    返回 _default_hint_margin
    """
    return _default_hint_margin


def set_default_hint_margin(hint_margin: list):
    """
    设置 _default_hint_margin
    :param hint_margin: 默认hint_margin
    """
    global _default_hint_margin
    if len(hint_margin) not in [4, 3, 2, 1]:
        raise ValueError("hint_margin参数错误, list长度需为1~4")
    _default_hint_margin = hint_margin


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


def get_default_button_margin():
    """
    返回 _default_button_margin
    """
    return _default_button_margin


def set_default_button_margin(button_margin: list):
    """
    设置 _default_button_margin
    :param button_margin: 默认button_margin
    """
    global _default_button_margin
    if len(button_margin) not in [4, 3, 2, 1]:
        raise ValueError("button_margin参数错误, list长度需为1~4")
    _default_button_margin = button_margin


# padding
def get_default_button_padding():
    """
    返回 _default_button_padding
    """
    return _default_button_padding


def set_default_button_padding(button_padding: list):
    """
    设置 _default_button_padding
    :param button_padding: 默认button_padding
    """
    global _default_button_padding
    if len(button_padding) not in [4, 3, 2, 1]:
        raise ValueError("button_padding参数错误, list长度需为1~4")
    _default_button_padding = button_padding


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


def margin_padding_check_convert(margin_padding: list[int]):
    if not isinstance(margin_padding, list) or len(margin_padding) not in [4, 3, 2, 1]:
        raise ValueError("margin参数错误, list长度需为1~4")

    # 转换margin参数
    if len(margin_padding) == 1:
        changed_margin = f"{margin_padding[0]},{margin_padding[0]},{margin_padding[0]},{margin_padding[0]}"
    elif len(margin_padding) == 2:
        changed_margin = f"{margin_padding[0]},{margin_padding[1]},{margin_padding[0]},{margin_padding[1]}"
    elif len(margin_padding) == 3:
        changed_margin = f"{margin_padding[0]},{margin_padding[1]},{margin_padding[0]},{margin_padding[2]}"
    else:
        changed_margin = f"{margin_padding[0]},{margin_padding[1]},{margin_padding[2]},{margin_padding[3]}"

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