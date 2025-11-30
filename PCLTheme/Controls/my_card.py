import warnings

from chameleon import PageTemplate
from PCLTheme import global_var


class my_card:
    """
    card控件
    """

    def __init__(self,
                 title: str,
                 can_swap: bool = True,
                 default_swaped: bool = False,
                 margin: list[int] = global_var.get_default_card_margin(),
                 row: int = -1,
                 column: int = -1,
                 width: int = None,
                 height: int = None,
                 horizontal_alignment: str = "Stretch",
                 vertical_alignment: str = "Stretch"
                 ):
        """
        创建一个卡片
        :param title: 卡片标题
        :param can_swap: 是否可以折叠, 默认为可以
        :param default_swaped: 初始是否折叠, 默认为不折叠
        :param margin:
            边距列表，支持以下格式：
            左、上、右、下边距；
            左右、上、下边距；
            左右、上下边距；
            左右上下边距。
            默认为global_var.get_default_card_margin()
        :param row: 所处行数, 作用于Grid中
        :param column: 所处列数, 作用于Grid中
        :param width: 控件宽度, 选填(默认的就很好了)
        :param height: 控件高度, 选填(默认的就很好了)
        :param horizontal_alignment: 横向对齐方式；居左：Left、居中：Center、居右：Right、拉伸（默认）：Stretch
        :param vertical_alignment: 纵向对齐方式；居上：Top、居中：Center、居下：Bottom、拉伸（默认）：Stretch
        """

        self.title = title
        self.can_swap = can_swap
        self.default_swaped = default_swaped
        self.margin = margin
        self.row = row
        self.column = column
        self.width = width
        self.height = height
        self.horizontal_alignment = horizontal_alignment
        self.vertical_alignment = vertical_alignment

        # 检查并转换margin
        self.margin = global_var.margin_padding_check_convert(self.margin)

        # 检测折叠参数合理性
        if (not self.can_swap) and self.default_swaped:
            raise ValueError("""can_swap参数错误, 当default_swaped为True时, can_swap必须为True.
            一个卡片不能在不可折叠的同时默认折叠""")


    def __enter__(self):
        containers = global_var.get_containers()
        if global_var.card_in_card():
            warnings.warn("注意到您在MyCard控件内又使用了MyCard控件, 请尽量避免这种情况orz", UserWarning)
        global_var.add_container_stack("MyCard")

        card_xaml = "    " * containers + f"""<local:MyCard Margin=\"{self.margin}\" Title=\"{self.title}\" CanSwap=\"{self.can_swap}\" IsSwaped=\"{self.default_swaped}\" >
"""

        # 检查并插入row和column参数
        global_var.row_column_check(self.row, self.column)

        if self.row != -1:
            card_xaml = card_xaml.replace("<local:MyCard ", f"<local:MyCard Grid.Row=\"{self.row}\" ", 1)
        if self.column != -1:
            card_xaml = card_xaml.replace("<local:MyCard ", f"<local:MyCard Grid.Column=\"{self.column}\" ", 1)


        # 插入width和height参数
        if self.width is not None:
            card_xaml = card_xaml.replace(" >", f" Width=\"{self.width}\" >", 1)
        if self.height is not None:
            card_xaml = card_xaml.replace(" >", f" Height=\"{self.height}\" >", 1)

        # 插入对齐参数
        if self.horizontal_alignment != "Stretch":
            card_xaml = card_xaml.replace(" >", f" HorizontalAlignment=\"{self.horizontal_alignment}\" >", 1)
        if self.vertical_alignment != "Stretch":
            card_xaml = card_xaml.replace(" >", f" VerticalAlignment=\"{self.vertical_alignment}\" >", 1)

        global_var.add_container()
        global_var.add_container_row(1)
        global_var.add_container_column(1)
        global_var.add_template_stack(card_xaml)

    def __exit__(self, exc_type, exc_val, exc_tb):
        card_xaml = global_var.pop_template_stack()
        containers = global_var.get_containers()
        card_xaml += "    " * (containers-1) + f"""</local:MyCard>
"""
        global_var.reduce_container()
        containers -= 1
        if containers != 0:
            global_var.stack_template_stack(card_xaml)
        else:
            template = PageTemplate(card_xaml)
            global_var.add_template(template, {})

        global_var.reduce_container_row()
        global_var.reduce_container_column()
        global_var.reduce_container_stack()
