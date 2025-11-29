from chameleon import PageTemplate
from PCLTheme import global_var


class stack_panel:
    """
    StackPanel控件
    """

    def __init__(self,
                 orientation: str = "Vertical",
                 horizontal_alignment: str = "Stretch",
                 vertical_alignment: str = "Stretch",
                 margin: list[int] = global_var.get_default_panel_margin(),
                 row: int = -1,
                 column: int = -1
                 ):
        """
        创建一个StackPanel
        :param orientation: 排列方向；垂直：Vertical、水平：Horizontal
        :param horizontal_alignment: 横向对齐方式；居左：Left、居中：Center、居右：Right、拉伸（默认）：Stretch
        :param vertical_alignment: 纵向对齐方式；居上：Top、居中：Center、居下：Bottom、拉伸（默认）：Stretch
        :param margin:
            边距列表，支持以下格式：
            左、上、右、下边距；
            左右、上、下边距；
            左右、上下边距；
            左右上下边距。
            默认为[0, 0, 0, 15]
        :param row: 所处行数, 作用于Grid中
        :param column: 所处列数, 作用于Grid中
        """

        self.orientation = orientation
        self.horizontal_alignment = horizontal_alignment
        self.vertical_alignment = vertical_alignment
        self.margin = margin
        self.row = row
        self.column = column

        # 检查并转换参数正确性
        self.margin = global_var.margin_padding_check_convert(self.margin)

        # 检查排列方式参数
        if self.orientation not in ["Vertical", "Horizontal"]:
            raise ValueError("""orientation参数错误, orientation参数只能为Vertical或Horizontal""")

    def __enter__(self):
        containers = global_var.get_containers()

        panel_xaml = "    " * containers + f"""<StackPanel Margin=\"{self.margin}\" Orientation=\"{self.orientation}\">
"""
        # 检查并插入row和column参数
        global_var.row_column_check(self.row, self.column)

        if self.row != -1:
            panel_xaml = panel_xaml.replace("<StackPanel ", f"<StackPanel Grid.Row=\"{self.row}\" ", 1)
        if self.column != -1:
            panel_xaml = panel_xaml.replace("<StackPanel ", f"<StackPanel Grid.Column=\"{self.column}\" ", 1)

        # 插入对齐参数
        if self.horizontal_alignment != "Stretch":
            panel_xaml = panel_xaml.replace(" >", f" HorizontalAlignment=\"{self.horizontal_alignment}\" >", 1)
        if self.vertical_alignment != "Stretch":
            panel_xaml = panel_xaml.replace(" >", f" VerticalAlignment=\"{self.vertical_alignment}\" >", 1)


        global_var.add_container()
        global_var.add_container_row(1)
        global_var.add_container_column(1)
        global_var.add_template_stack(panel_xaml)

    def __exit__(self, exc_type, exc_val, exc_tb):
        panel_xaml = global_var.pop_template_stack()
        containers = global_var.get_containers()
        panel_xaml += "    " * (containers-1) + f"""</StackPanel>
"""

        global_var.reduce_container()
        containers -= 1
        if containers != 0:
            global_var.stack_template_stack(panel_xaml)
        else:
            template = PageTemplate(panel_xaml)
            global_var.add_template(template, {})

        global_var.reduce_container_row()
        global_var.reduce_container_column()