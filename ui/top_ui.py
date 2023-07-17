import wx
import pyperclip

from util import json_parse_util


class TopUi(wx.Frame):

    def __init__(self):
        # style 禁用窗口最大化
        wx.Frame.__init__(self, None, wx.ID_ANY, style=wx.DEFAULT_FRAME_STYLE^wx.MAXIMIZE_BOX)
        self.copy_str_after_button = None
        self.compress_str_before_button = None
        self.parse_str_before_button = None
        self.clean_str_after_button = None
        self.str_after_text = None
        self.clean_str_before_button = None
        self.str_before_text = None
        self.str_type_box = None
        self.topBox = None
        self.rightBox = None
        self.leftBox = None
        self.leftPanel = None
        self.rightPanel = None

        self.frameConfig()
        self.init_panel()
        self.init_box()
        self.init_left()
        self.init_right()

        self.topBox.Add(self.leftPanel, proportion=1, border=2, flag=wx.ALL | wx.EXPAND)
        self.topBox.Add(self.rightPanel, proportion=4, border=2, flag=wx.ALL | wx.EXPAND)
        self.SetSizer(self.topBox)
        self.Show()

        self.bind_fun()

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

    def init_left(self):

        str_type_box = wx.BoxSizer(wx.HORIZONTAL)
        util_List = [
            'Json工具',
            'XML工具',
            'JavaScript工具',
            'HTML工具',
            'CSS工具',
            'SQL工具']
        self.str_type_box = wx.RadioBox(self.leftPanel, label="工具选项", choices=util_List, majorDimension=6,
                                        style=wx.RA_SPECIFY_ROWS)
        str_type_box.Add(self.str_type_box, 1, wx.EXPAND | wx.ALL, 1)

        self.leftBox.Add(str_type_box, 0, wx.EXPAND | wx.ALL, 5)

        self.leftPanel.SetSizer(self.leftBox)

    def init_right(self):
        str_before = wx.StaticBox(self.rightPanel, -1, '源字符串')
        str_before_sizer = wx.StaticBoxSizer(str_before, wx.VERTICAL)

        str_before_box = wx.BoxSizer(wx.VERTICAL)
        self.str_before_text = wx.TextCtrl(self.rightPanel, -1, size=(750, 200), style=wx.TE_MULTILINE)
        self.clean_str_before_button = wx.Button(self.rightPanel, -1, "清空")
        self.parse_str_before_button = wx.Button(self.rightPanel, -1, "格式化")
        self.compress_str_before_button = wx.Button(self.rightPanel, -1, "压缩")
        str_before_button_box = wx.BoxSizer(wx.HORIZONTAL)
        str_before_button_box.Add(self.clean_str_before_button, flag=wx.ALL | wx.EXPAND, border=5)
        str_before_button_box.Add(self.parse_str_before_button, flag=wx.ALL | wx.EXPAND, border=5)
        str_before_button_box.Add(self.compress_str_before_button, flag=wx.ALL | wx.EXPAND, border=5)
        str_before_box.Add(self.str_before_text, flag=wx.ALL | wx.EXPAND, border=5)
        str_before_box.Add(str_before_button_box, flag=wx.ALL | wx.EXPAND, border=5)

        str_before_sizer.Add(str_before_box, proportion=0, flag=wx.ALIGN_LEFT | wx.ALIGN_TOP, border=5)
        self.rightBox.Add(str_before_sizer, 0, wx.EXPAND | wx.ALL, 5)
        
        str_after = wx.StaticBox(self.rightPanel, -1, '输出字符串')
        str_after_sizer = wx.StaticBoxSizer(str_after, wx.VERTICAL)

        str_after_box = wx.BoxSizer(wx.VERTICAL)
        self.str_after_text = wx.TextCtrl(self.rightPanel, -1, size=(750, 200), style=wx.TE_MULTILINE)
        self.clean_str_after_button = wx.Button(self.rightPanel, -1, "清空")
        self.copy_str_after_button = wx.Button(self.rightPanel, -1, "复制结果")
        str_after_button_box = wx.BoxSizer(wx.HORIZONTAL)
        str_after_button_box.Add(self.clean_str_after_button, flag=wx.ALL | wx.EXPAND, border=5)
        str_after_button_box.Add(self.copy_str_after_button, flag=wx.ALL | wx.EXPAND, border=5)
        str_after_box.Add(self.str_after_text, flag=wx.ALL | wx.EXPAND, border=5)
        str_after_box.Add(str_after_button_box, flag=wx.ALL | wx.EXPAND, border=5)

        str_after_sizer.Add(str_after_box, proportion=0, flag=wx.ALIGN_LEFT | wx.ALIGN_TOP, border=5)
        self.rightBox.Add(str_after_sizer, 0, wx.EXPAND | wx.ALL, 5)

        self.rightPanel.SetSizer(self.rightBox)

    def bind_fun(self):

        self.clean_str_before_button.Bind(wx.EVT_LEFT_DOWN, self.clean_str_before)
        self.clean_str_after_button.Bind(wx.EVT_LEFT_DOWN, self.clean_str_after)
        self.parse_str_before_button.Bind(wx.EVT_LEFT_DOWN, self.parse_str)
        self.compress_str_before_button.Bind(wx.EVT_LEFT_DOWN, self.compress)
        self.copy_str_after_button.Bind(wx.EVT_LEFT_DOWN, self.copy)

    def clean_str_before(self, evt):
        self.str_before_text.SetValue("")

    def clean_str_after(self, evt):
        self.str_after_text.SetValue("")

    def parse_str(self, evt):
        before_str = self.str_before_text.GetValue()

        utilType = self.str_type_box.GetStringSelection()

        # 'Json工具',
        # 'XML工具',
        # 'JavaScript工具',
        # 'HTML工具',
        # 'CSS工具',
        # 'SQL工具'
        if 'Json工具' == utilType:
            self.str_after_text.SetValue(json_parse_util.json_parse(before_str))

    def compress(self, evt):
        before_str = self.str_before_text.GetValue()

        utilType = self.str_type_box.GetStringSelection()

        if 'Json工具' == utilType:
            self.str_after_text.SetValue(json_parse_util.json_compress(before_str))

    def copy(self, evt):
        pyperclip.copy(self.str_after_text.GetValue())
