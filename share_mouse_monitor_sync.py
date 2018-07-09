# coding = utf-8

from win32 import win32gui
import monitor_ctrl


def is_share_mouse_dim_window_visible():
    return win32gui.IsWindowVisible(win32gui.FindWindow("TDimForm", None))


if __name__ == '__main__':
    last_visible = False
    monitor_ctrl.enum_monitors()
    while True:
        curr_visible = is_share_mouse_dim_window_visible()
        if last_visible != curr_visible:
            if len(monitor_ctrl.ALL_PHY_MONITORS) > 0:
                monitor_ctrl.set_monitor_attr(monitor_ctrl.ALL_PHY_MONITORS[0], 'input_src',
                                              'DisplayPort 1' if curr_visible else 'Digital Video (TMDS) 3 HDMI 1')
            if len(monitor_ctrl.ALL_PHY_MONITORS) > 1:
                monitor_ctrl.set_monitor_attr(monitor_ctrl.ALL_PHY_MONITORS[1], 'input_src',
                                              'Digital Video (TMDS) 3 HDMI 1' if curr_visible else 'DisplayPort 1')
            last_visible = curr_visible

