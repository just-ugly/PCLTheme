from pathlib import Path

from chameleon import PageTemplate
from PCLTheme import global_var



def my_hint(text: str,
            margin: list[int] = [0, 0, 0, 15],
            theme: str = "Blue",
            row: int = -1,
            column: int = -1
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
        默认为[0, 0, 0, 15]
    :param theme: 颜色主题, 默认为 Blue, choice of {"Blue", "Red", "Yellow"}
    :param row: 所处行数, 作用于Grid中
    :param column: 所处列数, 作用于Grid中
    :return:
    """

    path = Path(__file__).cwd().joinpath("PCLTheme\\Controls\\my_hint.pt")
    tpl_text = Path(path).read_text(encoding='utf-8')

    # 检查参数正确性
    if not isinstance(margin, list) or len(margin) not in [4, 3, 2, 1]:
        raise ValueError("margin参数错误, list长度需为1~4")
    if not isinstance(theme, str) or theme not in ["Blue", "Red", "Yellow"]:
        raise ValueError("theme参数错误, 需要为以下字符串之一: Blue, Red, Yellow")

    # 转换margin参数
    changed_margin = []
    if len(margin) == 1:
        changed_margin = f"{margin[0]},{margin[0]},{margin[0]},{margin[0]}"
    elif len(margin) == 2:
        changed_margin = f"{margin[0]},{margin[1]},{margin[0]},{margin[1]}"
    elif len(margin) == 3:
        changed_margin = f"{margin[0]},{margin[1]},{margin[0]},{margin[2]}"
    else:
        changed_margin = f"{margin[0]},{margin[1]},{margin[2]},{margin[3]}"

    # 检查并插入Grid.Column和Grid.Row参数
    if global_var.get_containers() == 0:
        if row != -1 or column != -1:
            raise ValueError("row/column参数错误, 需要在Grid中")
    else:
        # 先检查row参数
        container_row = global_var.get_container_row()
        if row == -1 and container_row != 1:
            raise ValueError("row参数错误, 需要在有row设置的容器中设置row参数")
        if row != -1 and container_row == 1:
            raise ValueError("row参数错误, 所属容器无row参数")
        if row != -1 and row >= container_row:
            raise ValueError("row参数错误, row值超出范围")
        # 检查column参数
        container_column = global_var.get_container_column()
        if column == -1 and container_column != 1:
            raise ValueError("column参数错误, 需要在有column设置的容器中设置column参数")
        if column != -1 and container_column == 1:
            raise ValueError("column参数错误, 所属容器无column参数")
        if column != -1 and column >= container_column:
            raise ValueError("column参数错误, column值超出范围")


    if row != -1:
        template = PageTemplate(tpl_text.replace(" ", f" Grid.Row=\"{row}\" ", 1))
    if column != -1:
        template = PageTemplate(tpl_text.replace(" ", f" Grid.Column=\"{column}\" ", 1))
    else:
        template = PageTemplate(tpl_text)

    data = {
        "text": text,
        "margin": changed_margin,
        "theme": theme,
        "row": row,
        "column": column
    }

    if global_var.get_containers() == 0:
        global_var.add_template(template, data)
    else:
        hint_xaml = "    " * global_var.get_containers() + template(**data)
        global_var.stack_template_stack(hint_xaml)

