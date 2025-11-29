from chameleon import PageTemplate
from PCLTheme import global_var


def my_hint(text: str,
            margin: list[int] = global_var.get_default_grid_margin(),
            theme: str = "Blue",
            row: int = -1,
            column: int = -1,
            width: int = None,
            height: int = None,
            horizontal_alignment: str = "Stretch",
            vertical_alignment: str = "Stretch"
            ):
    """
    创建一个提示框(MyHint)
    :param text: 提示文字, 使用 &#xA; 进行换行
    :param margin:
        边距列表，支持以下格式：
        左、上、右、下边距；
        左右、上、下边距；
        左右、上下边距；
        左右上下边距。
        默认为 `global_var.get_default_margin()`
    :param theme: 颜色主题, 默认为 Blue, choice of {"Blue", "Red", "Yellow"}
    :param row: 所处行数, 作用于Grid中
    :param column: 所处列数, 作用于Grid中
    :param width: 控件宽度, 选填(默认的就很好了)
    :param height: 控件高度, 选填(默认的就很好了)
    :param horizontal_alignment: 横向对齐方式；居左：Left、居中：Center、居右：Right、拉伸（默认）：Stretch
    :param vertical_alignment: 纵向对齐方式；居上：Top、居中：Center、居下：Bottom、拉伸（默认）：Stretch
    """


    tpl_text = """<local:MyHint Margin="${margin}" Theme="${theme}" Text="${text}" />
"""

    # 检查参数正确性
    margin = global_var.margin_padding_check_convert(margin)
    if not isinstance(theme, str) or theme not in ["Blue", "Red", "Yellow"]:
        raise ValueError("theme参数错误, 需要为以下字符串之一: Blue, Red, Yellow")

    # 检查并插入Grid.Column和Grid.Row参数
    global_var.row_column_check(row, column)

    if row != -1:
        tpl_text = tpl_text.replace(" ", f" Grid.Row=\"{row}\" ", 1)
    if column != -1:
        tpl_text = tpl_text.replace(" ", f" Grid.Column=\"{column}\" ", 1)


    # 插入width和height参数
    if width is not None:
        tpl_text = tpl_text.replace(" />", f" Width=\"{width}\" />", 1)
    if height is not None:
        tpl_text = tpl_text.replace(" />", f" Height=\"{height}\" />", 1)

    # 插入对齐参数
    if horizontal_alignment != "Stretch":
        tpl_text = tpl_text.replace(" />", f" HorizontalAlignment=\"{horizontal_alignment}\" />", 1)
    if vertical_alignment != "Stretch":
        tpl_text = tpl_text.replace(" />", f" VerticalAlignment=\"{vertical_alignment}\" />", 1)

    # 包装
    template = PageTemplate(tpl_text)

    data = {
        "text": text,
        "margin": margin,
        "theme": theme,
        "row": row,
        "column": column,
        "width": width,
        "height": height,
        "horizontal_alignment": horizontal_alignment,
        "vertical_alignment": vertical_alignment
    }

    if global_var.get_containers() == 0:
        global_var.add_template(template, data)
    else:
        hint_xaml = "    " * global_var.get_containers() + template(**data)
        global_var.stack_template_stack(hint_xaml)
