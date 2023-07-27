---
title: Installation fails; cannot create install.log
description: This article provides a fix for a failed installation due to the Setup Wizard not creating the `install.log` during the installation.
exl-id: ff614018-8e49-4170-a806-8ebdc91ae8a9
feature: Install, Logs, Upgrade
role: Developer
---
# Installation fails; cannot create install.log

This article provides a fix for a failed installation due to the Setup Wizard not creating the `install.log` during the installation.

## Issue

Running Adobe Commerce processes at the same time might result in problems creating the installation log. (For example, two different installations in separate tab pages.)

## Cause

Installation-fails-cannot-create-install.log
Review your setting for `open_basedir` in `php.ini`. The Setup Wizard uses the [sys\_get\_temp\_dir ( void )](https://php.net/manual/en/function.sys-get-temp-dir.php) PHP call to get the value of the temporary directory. If [open\_basedir](http://php.net/manual/en/ini.core.php#ini.open-basedir) is set to refuse connections to a directory specified by `sys_get_temp_dir`, the installation fails.]
Review your setting for `open_basedir` in `php.ini`. The Setup Wizard uses the [sys\_get\_temp\_dir ( void )](https://php.net/manual/en/function.sys-get-temp-dir.php) PHP call to get the value of the temporary directory. If [open\_basedir](https://php.net/manual/en/ini.core.php#ini.open-basedir) is set to refuse connections to a directory specified by `sys_get_temp_dir`, the installation fails.


## Solution

To resolve the issue, change the value of `open_basedir` and restart the webserver.

If you're not sure how to change this value, use the following steps:

1. If you haven't already done so, create [phpinfo.php](https://devdocs.magento.com/guides/v2.3/install-gde/prereq/optional.html#install-optional-phpinfo).
1. Enter the following URL in your browser's address or location field: `https://<your web server IP or hostname>/<path to docroot>/phpinfo.php`
1. Look for the location of `php.ini`.     `php.ini` is typically specified as **Loaded Configuration File** in the displayed results.
1. As a user with root privileges, open `php.ini` in a text editor.
1. Locate the value of `open_basedir` and change it.
1. Save your changes to `php.ini`.
1. Restart the webserver.
