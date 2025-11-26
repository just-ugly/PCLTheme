from typing import ContextManager
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
                 margin: list[int] = global_var.get_default_margin(),
                 self_row: int = -1,
                 self_column: int = -1
                 ):
        self.column = column
        self.row = row
        self.margin = margin
        self.column_width = column_width
        self.row_height = row_height
        self.self_row = self_row
        self.self_column = self_column

        # 检查参数正确性
        if not isinstance(margin, list) or len(margin) not in [4, 3, 2, 1]:
            raise ValueError("margin参数错误, list长度需为1~4")
        if column < 1:
            raise ValueError("column参数错误, 需要大于0")
        if row < 1:
            raise ValueError("row参数错误, 需要大于0")
        if column_width is not None and len(column_width) != column:
            raise ValueError("column_width参数错误, 需要与column参数一致")
        if row_height is not None and len(row_height) != row:
            raise ValueError("row_height参数错误, 需要与row参数一致")


        # 转换margin参数
        self.changed_margin = []
        if len(margin) == 1:
            self.changed_margin = f"{margin[0]},{margin[0]},{margin[0]},{margin[0]}"
        elif len(margin) == 2:
            self.changed_margin = f"{margin[0]},{margin[1]},{margin[0]},{margin[1]}"
        elif len(margin) == 3:
            self.changed_margin = f"{margin[0]},{margin[1]},{margin[0]},{margin[2]}"
        else:
            self.changed_margin = f"{margin[0]},{margin[1]},{margin[2]},{margin[3]}"

        # 转换column_width参数
        if column_width is None:
            self.column_width = ["1*"] * self.column

        # 转换row_height参数
        if row_height is None:
            self.row_height = ["1*"] * self.row


    def __enter__(self):
        containers = global_var.get_containers()

        grid_xaml = """
""" + "    " * (containers-1) + f"""<Grid Margin=\"{self.changed_margin}\">
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
        if global_var.get_containers() == 0:
            if self.self_row != -1 or self.self_column != -1:
                raise ValueError("row/column参数错误, 需要在Grid中")
        else:
            # 先检查row参数
            container_row = global_var.get_container_row()
            if self.self_row == -1 and container_row != 1:
                raise ValueError("row参数错误, 需要在有row设置的容器中设置row参数")
            if self.self_row != -1 and container_row == 1:
                raise ValueError("row参数错误, 所属容器无row参数")
            if self.self_row != -1 and self.self_row >= container_row:
                raise ValueError("row参数错误, row值超出范围")
            # 检查column参数
            container_column = global_var.get_container_column()
            if self.self_column == -1 and container_column != 1:
                raise ValueError("column参数错误, 需要在有column设置的容器中设置column参数")
            if self.self_column != -1 and container_column == 1:
                raise ValueError("column参数错误, 所属容器无column参数")
            if self.self_column != -1 and self.self_column >= container_column:
                raise ValueError("column参数错误, column值超出范围")

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
