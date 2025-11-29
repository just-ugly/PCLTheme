from PCLTheme import global_var

from chameleon import PageTemplate


Pair = dict[PageTemplate, dict]


class grid:
    """
    Grid控件
    """
    def __init__(self,
                 column: int = 1,
                 column_width: list = None,
                 row: int = 1,
                 row_height: list = None,
                 margin: list[int] = global_var.get_default_grid_margin(),
                 self_row: int = -1,
                 self_column: int = -1
                 ):
        """
        创建一个Grid控件
        :param column: 列数
        :param column_width: 列宽列表
        :param row: 行数
        :param row_height: 行高列表
        :param margin:
            边距列表，支持以下格式：
            左、上、右、下边距；
            左右、上、下边距；
            左右、上下边距；
            左右上下边距。
            默认为 `global_var.get_default_margin()`
        :param self_row: 所处行数, 作用于Grid中
        :param self_column: 所处列数, 作用于Grid中
        """

        self.column = column
        self.row = row
        self.margin = margin
        self.column_width = column_width
        self.row_height = row_height
        self.self_row = self_row
        self.self_column = self_column

        # 检查并转换参数正确性
        self.margin = global_var.margin_padding_check_convert(self.margin)

        if column < 1:
            raise ValueError("column参数错误, 需要大于0")
        if row < 1:
            raise ValueError("row参数错误, 需要大于0")
        if column_width is not None and len(column_width) != column:
            raise ValueError("column_width参数错误, 需要与column参数一致")
        if row_height is not None and len(row_height) != row:
            raise ValueError("row_height参数错误, 需要与row参数一致")


        # 转换column_width参数
        if column_width is None:
            self.column_width = ["1*"] * self.column

        # 转换row_height参数
        if row_height is None:
            self.row_height = ["1*"] * self.row


    def __enter__(self):
        containers = global_var.get_containers()

        grid_xaml = "    " * containers + f"""<Grid Margin=\"{self.margin}\">
"""
        if self.column > 1:
            grid_xaml += "    " * containers + f"""<Grid.ColumnDefinitions>
"""
            for i in range(self.column):
                grid_xaml += "    " * (containers+1) + f"""<ColumnDefinition Width=\"{self.column_width[i]}\"/>
"""

            grid_xaml += "    " * containers + f"""</Grid.ColumnDefinitions>
"""
        if self.row > 1:
            grid_xaml += "    " * containers + f"""<Grid.RowDefinitions>
"""
            for i in range(self.row):
                grid_xaml += "    " * (containers+1) + f"""<RowDefinition Height=\"{self.row_height[i]}\"/>
"""

            grid_xaml += "    " * containers + f"""</Grid.RowDefinitions>
"""

        # 检查并插入Grid.Column和Grid.Row参数
        global_var.row_column_check(self.self_row, self.self_column)

        if self.self_row != -1:
            grid_xaml = grid_xaml.replace("<Grid ", f"<Grid Grid.Row=\"{self.self_row}\" ", 1)
        if self.self_column != -1:
            grid_xaml = grid_xaml.replace("<Grid ", f"<Grid Grid.Column=\"{self.self_column}\" ", 1)
        else:
            grid_xaml = grid_xaml


        global_var.add_container()
        global_var.add_container_row(self.row)
        global_var.add_container_column(self.column)
        global_var.add_template_stack(grid_xaml)


    def __exit__(self, exc_type, exc_val, exc_tb):
        grid_xaml = global_var.pop_template_stack()
        containers = global_var.get_containers()
        grid_xaml += "    " * (containers-1) + f"""</Grid>
"""
        global_var.reduce_container()
        containers -= 1
        if containers != 0:
            global_var.stack_template_stack(grid_xaml)
        else:
            template = PageTemplate(grid_xaml)
            global_var.add_template(template, {})

        global_var.reduce_container_row()
        global_var.reduce_container_column()
