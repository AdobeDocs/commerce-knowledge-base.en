---
title: Locked (grayed out) fields in Commerce Admin
description: This article provides a solution for when you cannot modify fields in the Commerce Admin.
exl-id: 5fe0967a-4241-440b-bb0d-429fa5644bbc
feature: Admin Workspace
role: Developer
---
# Locked (grayed out) fields in Commerce Admin

This article provides a solution for when you cannot modify locked (grayed out) fields in the Commerce Admin.

## Affected products and versions

* Adobe Commerce on-premises 2.3.x, 2.4.x
* Adobe Commerce on cloud infrastructure 2.3.x, 2.4.x

## Issue

Once you have saved a change to your configuration to `app/etc/env.php` or `app/etc/config.php`, you cannot modify the setting in the Admin.

<u>Steps to reproduce</u>:

 Note: This is an example - the issue can affect all configurations that have been saved.

1. The merchant saves their delivery methods credentials using the following command in the terminal: `./vendor/bin/ece-tools config:dump`. This saves the credentials in the `app/etc/env.php` file.
1. The merchant then attempts to change the credentials later.

<u>Expected results</u>:

 The merchant can set the values in the Admin field settings and save them.

 <u>Actual results</u>:

 The fields in the Admin are locked, or the values can be changed but will not save in the Admin.

## Cause

When the configuration is saved to `env.php` or `config.php`, you will not be able to modify the setting in the Admin. To allow editing of the setting, you will have to remove the configuration from `env.php` or `config.php`.

## Solution

Make sure that the configuration has not been saved to `app/etc/env.php` or `app/etc/config.php`. If it has been saved, try the following steps:

* `config.php` - Remove the setting and then redeploy.
* `env.php` - Modify this directly on the server and remove the setting, then run `bin/magento app:config:import`.

## Related Reading

* [Export the Configuration](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/cli/configuration-management/export-configuration) in our developer documentation.
* [Set Configuration values](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/cli/configuration-management/set-configuration-values) in our developer documentation.
* [Adobe Commerce on cloud infrastructure: reduce deployment downtime with Configuration Management](/help/how-to/general/magento-cloud-reduce-deployment-downtime-with-configuration-management.md) in our support knowledge base.
