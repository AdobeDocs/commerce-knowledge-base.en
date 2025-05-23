---
title: '"Updater application is not available" error'
description: This article talks about the solution for the "updater application is not available" issue you might face when trying to update/install Adobe Commerce on-premises using the Web Setup Wizard.
exl-id: 85e55ed8-0bc9-4378-b722-46be98ce2638
feature: Configuration
role: Developer
---
# "Updater application is not available" error

This article talks about the solution for the "updater application is not available" issue you might face when trying to update/install Adobe Commerce on-premises using the Web Setup Wizard.

## Issue

The following message is displayed in the readiness check:

![Screen_Shot_2019-08-29_at_1.39.12_PM.png](assets/Screen_Shot_2019-08-29_at_1.39.12_PM.png)

## Affected products/versions

* Adobe Commerce on-premises 2.2.x, 2.3.x
* Magento Open Source 2.2.x, 2.3.x


## Solution

To resolve this issue, see if there is a `<magento_root>/update` directory that contains files and subdirectories. Otherwise, see [Set up the updater](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/updater-application-is-not-available-error) in our developer documentation.
