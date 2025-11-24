from pathlib import Path

from chameleon import PageTemplate
from PCLTheme import global_var



def my_hint(text: str,
            margin: list[int] = [0, 0, 0, 15],
            theme: str = "Blue"):
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
    :return:
    """

    path = Path(__file__).cwd().joinpath("PCLTheme\\Controls\\my_hint.pt")
    tpl_text = Path(path).read_text(encoding='utf-8')
    template = PageTemplate(tpl_text)

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

    data = {
        "text": text,
        "margin": changed_margin,
        "theme": theme
    }

    if global_var._containers == 0:
        global_var._templates.append({template: data})
    else:
        hint_xaml = "    " * global_var._containers + template(**data)
        global_var._template_stack[-1] += (hint_xaml)

