import webview


class Api:
    def select_dir(self):  # 选择目录
        result = window.create_file_dialog(webview.FOLDER_DIALOG)
        print(result)
        return result[0] if result else ''

    def select_file(self):  # 选择文件
        file_types = ('Image Files (*.bmp;*.jpg;*.gif;*.png)', 'All files (*.*)')
        result = window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=True, file_types=file_types)
        print(result)
        return result[0] if result else ''

    def check_login(self, user, pwd):  # 用户登录接口
        print(user, pwd)
        if user != 'test' or pwd != 'test':
            return {'code': '4103', 'msg': '用户名或密码错误'}
        import time
        time.sleep(1)

        groups = {"首页": [], "业务菜单": ["3D模型", "画图展示", "业务3"], "系统设置": ["用户管理", "系统日志"]}
        roles = {"首页": ["读"], "3D模型": ["读", "写"], "业务2": ["读", "写"], "业务3": ["读", "写"],
                 "用户管理": ["读", "写"], "系统日志": ["读", "写"]}

        return {'code': '0', 'data': {'groups': groups, 'roles': roles}, 'msg': 'ok'}


if __name__ == '__main__':
    chinese = {
        'global.quitConfirmation': u'确定关闭?',
    }

    api = Api()
    window = webview.create_window(
        title='pywebview+vue实现系统登录',
        url='static',
        width=900,
        height=620,
        resizable=True,  # 固定窗口大小
        text_select=False,  # 禁止选择文字内容
        confirm_close=True,  # 关闭时提示
        js_api=api,  # api中定义供html调用的函数
        min_size=(900, 620)  # 设置窗口最小尺寸
    )

    # 启动窗口
    webview.start(localization=chinese, http_server=True, debug=True)
