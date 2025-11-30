from chameleon import PageTemplate
from PCLTheme import global_var



def add_template(template: PageTemplate, data: dict):
    """
    在 templates 里新增一个字典
    :param template: xaml模板
    :param data: 参数字典
    """


def build(file_path: str = None):
    """
    按添加顺序依次渲染并拼接

    给定保存路径可保存至该路径下

    若为PCL自定义主页的路径,则应该以"\PCL\Custom.xaml"结尾
    """
    out_xaml = ""
    for template_dict in global_var._templates:
        template = list(template_dict.keys())[0]
        data = template_dict[template]
        out_xaml += str(template(**data))

    if file_path is not None:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(out_xaml)

    global_var.clear()

    return out_xaml