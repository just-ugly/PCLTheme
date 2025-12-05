# PCLTheme

一个用 Python 构建 PCL 主页 XAML 的轻量库，目标是让用户无需编写 XAML，就能通过 Python 语法快速构建并输出 PCL 自定义主页（Custom.xaml）


### :star:主要特点

- 用 Python API 构建 XAML，降低学习 XAML 的门槛
- 支持容器（Grid、StackPanel、MyCard 等）与PCL控件（TextBlock、MyButton、MyImage、MyHint 等）
- 支持嵌套容器与栈式渲染，按添加顺序拼接输出
- 可直接保存为 PCL 本地自定义主页路径（例如保存为 Custom.xaml）

## :rocket: 快速开始

### :memo: 前提要求

- Python 3.6 或更高版本

### :computer: 安装方式

从 PyPI 安装（最新版本：0.2.3）

``` bash
pip install PCLTheme
```

### :coffee: 示例代码

下面示例展示了一个最小的使用流程：创建容器与控件，然后调用 `build()` 获取生成的 XAML。

```python
import PCLTheme as pt

if __name__ == "__main__":
    path = "D:\-shot 2.9.2\PCL" # 替换为 PCL 主页路径
    file_name = "Custom.xaml" # 本地自定义主页文件名

    with pt.my_card(title="PCLTheme",
                    can_swap=False):
        with pt.stack_panel():
            pt.text_block(
                margin=[0, 0, 0, 30],
                text="PCLTheme",
                font_size=36,
                font_weight="Bold",
                foreground="T2",
                background="T6",
                horizontal_alignment="Center", )

            pt.text_block(
                margin=[0, 0, 0, 30],
                text="一个用 Python 构建 PCL（个人启动页/主页）XAML 模板的轻量库&#xA;目标是让用户无需编写 XAML，就能通过 Python 语法快速构建并输出 PCL 自定义主页（Custom.xaml）",
                text_wrapping="Wrap",
                font_size=16,
                horizontal_alignment="Left",
            )

            pt.text_block(
                margin=[0, 0, 0, 10],
                text="该库亦可用于自动化批量生成 PCL 主页，实现一些高级功能",
                text_wrapping="Wrap",
                font_size=16,
                horizontal_alignment="Left",
            )

            pt.my_button(
                text="前往GitHub主页",
                color_type="Highlight",
                event_type="打开网页",
                event_data1="https://github.com/just-ugly/PCLTheme",
                height=35,
            )

    print(pt.build(path, file_name))

```

## :book: 常用控件速览

目前已包含除 “进阶：高级自定义事件” 板块外所有存在于《自定义主页与帮助 XAML格式》帮助文档中的控件

具体有（按字母顺序排列，已省略 local 前缀）：

- Grid
- MyButton
- MyCard
- MyHint
- MyIconButton
- MyIconTextButton
- MyImage
- MyListItem
- MyTextButton
- StackPanel
- TextBlock
- WarpPanel

## :pen: 自定义默认样式与全局设置

项目在 `PCLTheme.global_var` 中维护了若干全局默认值（如默认 margin/padding/文本大小等），并导出了 getter/setter，示例：

```python
import PCLTheme as pt

pt.set_default_text_size(14)
pt.set_default_panel_margin([20, 30, 20, 12])
```

## :question: 错误检查与常见异常

- 大多数控件会对 `margin`/`padding` 长度（只接受长度 1~4）做检查。
- 当控件需要在 Grid 中指定 `row`/`column` 时，如果当前并不在有 row/column 的容器内部，会抛出 ValueError。
- 请按照控件函数签名提供正确类型与取值范围，会在运行时抛出有意义的异常提示。
- 在 MyCard 中使用 MyCard 会被警告（ :alien: 邪修）

## :next_track_button: TODOLIST

- [ ] 实现无法寻找到文件时，自动创建文件
- [ ] 实现“进阶：高级自定义事件”中的控件
- [ ] 实现所有方法的`Opacity`属性
- [ ] 实现所有方法的`Visibility`属性
- [ ] 为所有有`padding`属性的控件实现`padding`属性
- [ ] 为属性的插入顺序排序
