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
                 margin: list[int] = [0, 0, 0, 15]
                 ):
        self.column = column
        self.row = row
        self.margin = margin
        self.column_width = column_width
        self.row_height = row_height

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
        global_var._containers += 1
        grid_xaml = """
""" + "    " * (global_var._containers-1) + f"""<Grid Margin=\"{self.changed_margin}\">
"""
        if self.column > 1:
            grid_xaml += "    " * global_var._containers + f"""<Grid.ColumnDefinitions>
"""
            for i in range(self.column):
                grid_xaml += "    " * (global_var._containers+1) + f"""<ColumnDefinition Width=\"{self.column_width[i]}\"/>
"""

            grid_xaml += "    " * global_var._containers + f"""</Grid.ColumnDefinitions>
"""
        if self.row > 1:
            grid_xaml += "    " * global_var._containers + f"""<Grid.RowDefinitions>
"""
            for i in range(self.row):
                grid_xaml += "    " * (global_var._containers+1) + f"""<RowDefinition Height=\"{self.row_height[i]}\"/>
"""

            grid_xaml += "    " * global_var._containers + f"""</Grid.RowDefinitions>
"""

        global_var._template_stack.append(grid_xaml)


    def __exit__(self, exc_type, exc_val, exc_tb):
        grid_xaml = global_var._template_stack.pop()
        grid_xaml += "    " * (global_var._containers-1) + f"""</Grid>

"""
        global_var._containers -= 1
        if global_var._containers != 0:
            global_var._template_stack[-1] += grid_xaml
        else:
            template = PageTemplate(grid_xaml)
            global_var._templates.append({template: {}})
