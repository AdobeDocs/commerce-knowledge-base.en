---
title: Composer plugins issues when upgrading to Adobe Commerce 2.4.4
description: This article provides a solution to avoid the issue with composer plugins when upgrading from Adobe Commerce 2.4.3 and earlier to Adobe Commerce 2.4.4 or higher (when future versions are released).
exl-id: 7502ca9e-c307-4e8a-aa1d-4886e7be25da
feature: Upgrade
role: Developer
---
# Composer plugins issues when upgrading to Adobe Commerce 2.4.4

This article provides a solution to avoid issues with composer plugins when upgrading from Adobe Commerce 2.4.3 and earlier to Adobe Commerce 2.4.4 or higher (when future versions are released).

## Affected products and versions

* Adobe Commerce on premises, any version when updating to 2.4.4 or higher (when released)
* Adobe Commerce on cloud infrastructure, any version when updating to 2.4.4 or higher (when released)
* Magento Open Source, any version when updating to 2.4.4 or higher (when released)

## Issue

When updating to Adobe Commerce 2.4.4 or higher after July 2022, you might get a warning from composer about plugins.

<u>Steps to reproduce</u>:

Prerequisites: Adobe Commerce 2.4.3 or earlier is installed.

1. Start the upgrade as described in [Perform an upgrade](https://experienceleague.adobe.com/docs/commerce-operations/upgrade-guide/implementation/perform-upgrade.html).
1. Run the `composer update` command to upgrade the Adobe Commerce application.

<u>Expected results</u>:

Upgrade is successful.

<u>Actual results</u>:

Installation fails with an error similar to the following:

```bash
Writing lock file
Installing dependencies from lock file (including require-dev)
Package operations: 591 installs, 0 updates, 0 removals
  - Installing laminas/laminas-dependency-plugin (2.2.0): Extracting archive
laminas/laminas-dependency-plugin contains a Composer plugin which is currently not in your allow-plugins config. See https://getcomposer.org/allow-plugins
Do you trust "laminas/laminas-dependency-plugin" to execute code and wish to enable it now? (writes "allow-plugins" to composer.json) [y,n,d,?] y
Plugin initialization failed (require(app/etc/NonComposerComponentRegistration.php): failed to open stream: No such file or directory), uninstalling plugin
  - Removing laminas/laminas-dependency-plugin (2.2.0)
    Install of laminas/laminas-dependency-plugin failed


  [ErrorException]
  require(app/etc/NonComposerComponentRegistration.php): failed to open stream: No such file or directory
```

## Cause

After July 2022 Composer changes the default value of the [`allow-plugins` option](https://getcomposer.org/doc/06-config.md#allow-plugins) to `{}` and plugins will not load anymore unless allowed.

## Solution

Add the following to your `composer.json` file, depending on how you installed Adobe Commerce:

* If the project has been created [using the `composer create-project` command](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/composer#get-the-metapackage):

    ```json
    "config": {
        "allow-plugins": {
            "dealerdirect/phpcodesniffer-composer-installer": true,
            "laminas/laminas-dependency-plugin": true,
            "magento/*": true
        }
    }
    ```

* If the project has been created by another way and does not have `"dealerdirect/phpcodesniffer-installer"` in `"require-dev"` section:

    ```json
    "config": {
        "allow-plugins": {
            "laminas/laminas-dependency-plugin": true,
            "magento/*": true
        }
    }
    ```

After updating the `composer.json` file, run the `composer update` command and restart the upgrade process.
