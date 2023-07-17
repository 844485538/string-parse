import wx


class TopUi(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY)
        self.str_type_box = None
        self.topBox = None
        self.rightBox = None
        self.leftBox = None
        self.leftPanel = None
        self.rightPanel = None

        self.frameConfig()
        self.init_panel()
        self.init_box()
        self.build_box()
        self.init_left()

    def frameConfig(self):
        """frame config"""

        self.SetSize((1020, 640))
        self.Center()
        self.SetTitle('String-Parse')
        self.SetBackgroundColour("WHITE")

    def init_panel(self):
        self.leftPanel = wx.Panel(self)
        self.rightPanel = wx.Panel(self)

    def init_box(self):
        self.leftBox = wx.BoxSizer(wx.VERTICAL)
        self.rightBox = wx.BoxSizer(wx.VERTICAL)
        self.topBox = wx.BoxSizer(wx.HORIZONTAL)

    def build_box(self):
        self.topBox.Add(self.leftBox, proportion=1, border=2, flag=wx.ALL | wx.EXPAND)
        self.topBox.Add(self.rightBox, proportion=1, border=2, flag=wx.ALL | wx.EXPAND)

    def init_left(self):
        nm = wx.StaticBox(self.leftPanel, -1, '字符串配置')
        nmSizer = wx.StaticBoxSizer(nm, wx.VERTICAL)
        # 构建静态文本框
        modelname = wx.StaticText(self.leftPanel, -1, "字符串类型")
        # 在StaticBoxSizer添加文本框
        nmSizer.Add(modelname, 1, wx.EXPAND | wx.ALL, 1)
        # 创建RadioButton
        lblList = ['json', 'xml']
        self.str_type_box = wx.RadioBox(self.leftPanel, label='字符串类型', choices=lblList, majorDimension=4,
                                        style=wx.RA_SPECIFY_ROWS)
        # 在垂直盒子添加RadioButton
        self.leftBox.Add(self.str_type_box, 0, wx.EXPAND | wx.ALL, 10)
        # 把垂直盒子与LeftPanel关联起来
        self.leftPanel.SetSizer(self.leftBox)
