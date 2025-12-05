from chameleon import PageTemplate
from PCLTheme import global_var

event_type_list = [
    "打开网页", "执行命令", "打开文件", "打开帮助", "启动游戏",
    "复制文本", "刷新页面", "刷新主页", "刷新帮助", "今日人品",
    "内存优化", "清理垃圾", "弹出窗口", "弹出提示", "切换页面",
    "导入整合包", "安装整合包", "下载文件", "修改设置", "写入设置",
    "修改变量", "写入变量", "加入房间"
]


def my_list_item(logo: str = None,
                 title: str = None,
                 info: str = None,
                 list_type: str = None,
                 margin: list[int] = None,
                 event_type: str = None,
                 event_data1: str = None,
                 event_data2: str = None,
                 event_data3: str = None,
                 row: int = -1,
                 column: int = -1,
                 width: int = None,
                 height: int = None,
                 horizontal_alignment: str = "Stretch",
                 vertical_alignment: str = "Stretch"
                 ):
    """
    创建一个列表项
    :param logo: 列表项图标
    :param title: 列表项标题
    :param info: 列表项信息
    :param list_type: 列表项类型, 默认为None, 设置为Clickable表示可点击
    :param margin:
        边距列表，支持以下格式：
        左、上、右、下边距；
        左右、上、下边距；
        左右、上下边距；
        左右上下边距。
        默认为 `global_var.get_default_list_item_margin()`
    :param event_type:
        按钮事件类型,支持以下事件:
        打开网页, 执行命令, 打开文件, 打开帮助, 启动游戏,
        复制文本, 刷新页面, 刷新主页, 刷新帮助, 今日人品,
        内存优垃圾, 弹出窗口, 弹出提示, 切换页面,
        导入整合包, 安装整合包, 下载文件, 修改设置, 写入设置,
        修改变量, 写入变量, 加入房间
        具体事件用法和事件数据含义请参考文档说明：
        https://github.com/Meloong-Git/PCL/wiki/%E8%87%AA%E5%AE%9A%E4%B9%89%E4%BA%8B%E4%BB%B6
        (edited by 龙腾猫跃)
    :param event_data1: 事件数据1, 具体含义根据event_type而定, 默认为None
    :param event_data2: 事件数据2, 具体含义根据event_type而定, 默认为None
    :param event_data3: 事件数据3, 具体含义根据event_type而定, 默认为None
    :param row: 所处行数, 作用于Grid中
    :param column: 所处列数, 作用于Grid中
    :param width: 控件宽度, 选填
    :param height: 控件高度, 选填
    :param horizontal_alignment: 横向对齐方式；居左：Left、居中：Center、居右：Right、拉伸（默认）：Stretch
    :param vertical_alignment: 纵向对齐方式；居上：Top、居中：Center、居下：Bottom、拉伸（默认）：Stretch
    """

    tpl_text = """<local:MyListItem Margin="${margin}" />
"""

    if logo is not None:
        tpl_text = tpl_text.replace(" />", " Logo=\"${logo}\" />", 1)

    if title is not None:
        tpl_text = tpl_text.replace(" />", " Title=\"${title}\" />", 1)

    if info is not None:
        tpl_text = tpl_text.replace(" />", " Info=\"${info}\" />", 1)

    # 检查参数正确性
    if margin is None:
        margin = global_var.get_default_list_item_margin()
    margin = global_var.margin_padding_check_convert(margin)

    # 检查并插入Grid.Column和Grid.Row参数
    global_var.row_column_check(row, column)

    if row != -1:
        tpl_text = tpl_text.replace(" ", " Grid.Row=\"${row}\" ", 1)
    if column != -1:
        tpl_text = tpl_text.replace(" ", " Grid.Column=\"${column}\" ", 1)

    event_data = None
    if list_type is not None:
        if list_type is "Clickable":
            tpl_text = tpl_text.replace(" />", " Type=\"Clickable\" />", 1)

            # 插入事件参数
            if event_type is not None:
                tpl_text = tpl_text.replace(" />", " EventType=\"${event_type}\" />", 1)

            # 拼凑事件数据并插入
            if event_data1 is not None:
                event_data = event_data1
                if event_data2 is not None:
                    event_data = event_data + "|" + event_data2
                    if event_data3 is not None:
                        event_data = event_data + "|" + event_data3

                tpl_text = tpl_text.replace(" />", " EventData=\"${event_data}\" />", 1)

        else:
            raise ValueError("Type参数错误, 需要为Clickable")

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
        "logo": logo,
        "title": title,
        "info": info,
        "type": list_type,
        "margin": margin,
        "event_type": event_type,
        "event_data": event_data,
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


