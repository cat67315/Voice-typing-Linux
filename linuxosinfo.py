#!/usr/bin/env python3

import os
import subprocess
import configparser

def is_dark_mode():
    # GNOME
    try:
        theme = subprocess.check_output(
            ["gsettings", "get", "org.gnome.desktop.interface", "gtk-theme"],
            text=True
        ).strip().strip("'")
        if "dark" in theme.lower():
            return True
    except Exception:
        pass

    # KDE Plasma
    kde_config_path = os.path.expanduser("~/.config/kdeglobals")
    if os.path.exists(kde_config_path):
        config = configparser.ConfigParser()
        config.read(kde_config_path)
        try:
            color_scheme = config.get("General", "ColorScheme")
            if "dark" in color_scheme.lower():
                return True
        except Exception:
            pass

    # XFCE
    try:
        xfce_theme = subprocess.check_output(
            ["xfconf-query", "-c", "xsettings", "-p", "/Net/ThemeName"],
            text=True
        ).strip()
        if "dark" in xfce_theme.lower():
            return True
    except Exception:
        pass

    # Cinnamon
    try:
        cinnamon_theme = subprocess.check_output(
            ["gsettings", "get", "org.cinnamon.desktop.interface", "gtk-theme"],
            text=True
        ).strip().strip("'")
        if "dark" in cinnamon_theme.lower():
            return True
    except Exception:
        pass

    # MATE
    try:
        mate_theme = subprocess.check_output(
            ["gsettings", "get", "org.mate.interface", "gtk-theme"],
            text=True
        ).strip().strip("'")
        if "dark" in mate_theme.lower():
            return True
    except Exception:
        pass

    return False

def os_accent_color():
    return 1,4,7 # Temporary placeholder