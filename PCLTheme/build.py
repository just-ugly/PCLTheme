from chameleon import PageTemplate
from PCLTheme import global_var



def add_template(template: PageTemplate, data: dict):
    """
    在 templates 里新增一个字典
    :param template: xaml模板
    :param data: 参数字典
    """


def build() -> str:
    """
    按添加顺序依次渲染并拼接
    """
    out_xaml = ""
    for template_dict in global_var._templates:
        template = list(template_dict.keys())[0]
        data = template_dict[template]
        out_xaml += str(template(**data))

    return out_xaml