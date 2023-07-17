import wx

from ui.top_ui import TopUi

if __name__ == '__main__':
    app = wx.App()
    frame = TopUi()
    frame.Show()
    app.MainLoop()
