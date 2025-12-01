import re
from pydantic.v1.color import Color

from chameleon import PageTemplate
from PCLTheme import global_var


def text_block(text: str,
               text_wrapping: str = "Wrap",
               font_size: int = None,
               font_weight: str = "Normal",
               foreground: str = "T2",
               background: str = None,
               margin: list[int] = None,
               row: int = -1,
               column: int = -1,
               width: int = None,
               height: int = None,
               horizontal_alignment: str = "Stretch",
               vertical_alignment: str = "Stretch"
               ):
    """
    创建一个纯文本
    :param text: 文本内容
    :param text_wrapping: 换行方式
    :param font_size: 文本大小
    :param font_weight: 文本粗体设置
    :param foreground: 文本前景颜色: 支持颜色代码或输入T1~T8应用主题色
    :param background: 文本背景颜色: 支持颜色代码或输入T1~T8应用主题色, 默认为None
    :param margin:
        边距列表，支持以下格式：
        左、上、右、下边距；
        左右、上、下边距；
        左右、上下边距；
        左右上下边距。
        默认为 `global_var.get_default_text_margin()`
    :param row: 所处行数, 作用于Grid中
    :param column: 所处列数, 作用于Grid中
    :param width: 控件宽度, 选填
    :param height: 控件高度, 选填
    :param horizontal_alignment: 横向对齐方式；居左：Left、居中：Center、居右：Right、拉伸（默认）：Stretch
    :param vertical_alignment: 纵向对齐方式；居上：Top、居中：Center、居下：Bottom、拉伸（默认）：Stretch
    """

    tpl_text = """<TextBlock Margin="${margin}" Text="${text}" TextWrapping="${text_wrapping}" Foreground="${foreground}" FontWeight="${font_weight}" FontSize="${font_size}" />
"""

    # 检查参数正确性
    if margin is None:
        margin = global_var.get_default_text_margin()
    margin = global_var.margin_padding_check_convert(margin)

    if font_size is None:
        font_size = global_var.get_default_text_size()

    # 颜色参数检测
    if re.match(r"^T[1-8]$", foreground):
        foreground = "{DynamicResource ColorBrush" + foreground.replace("T", "") + "}"
    else:
        try:
            foreground = str(Color(foreground))
        except ValueError:
            raise ValueError("foreground参数错误, 需要为以下字符串之一: T1~T8, 颜色代码")
    if background is not None:
        if re.match(r"^T[1-8]$", background):
            background = "{DynamicResource ColorBrush" + background.replace("T", "") + "}"
        else:
            try:
                background = str(Color(background))
            except ValueError:
                raise ValueError("background参数错误, 需要为以下字符串之一: T1~T8, 颜色代码")

        tpl_text = tpl_text.replace("<TextBlock ", "<TextBlock Background=\"${background}\" ", 1)

    # 检查并插入Grid.Column和Grid.Row参数
    global_var.row_column_check(row, column)


    if row != -1:
        tpl_text = tpl_text.replace(" ", " Grid.Row=\"${row}\" ", 1)
    if column != -1:
        tpl_text = tpl_text.replace(" ", " Grid.Column=\"${column}\" ", 1)


    # 插入width和height参数
    if width is not None:
        tpl_text = tpl_text.replace(" />", " Width=\"${width}\" />", 1)
    if height is not None:
        tpl_text = tpl_text.replace(" />", " Height=\"${height}\" />", 1)

    # 插入对齐参数
    if horizontal_alignment != "Stretch":
        tpl_text = tpl_text.replace(" />", " HorizontalAlignment=\"${horizontal_alignment}\" />", 1)
    if vertical_alignment != "Stretch":
        tpl_text = tpl_text.replace(" />", " VerticalAlignment=\"${vertical_alignment}\" />", 1)

    # 包装
    template = PageTemplate(tpl_text)

    data = {
        "text": text,
        "text_wrapping": text_wrapping,
        "font_size": font_size,
        "font_weight": font_weight,
        "foreground": foreground,
        "background": background,
        "margin": margin,
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
