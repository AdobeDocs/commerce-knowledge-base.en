---
title: Unknown module Magento_BundleSampleData
description: This article provides a fix for the unknown module error during installation of Adobe Commerce.
exl-id: c927bc8f-d70b-4305-87c1-223001212555
feature: Extensions
role: Developer
---
# Unknown module Magento_BundleSampleData

This article provides a fix for the unknown module error during installation of Adobe Commerce.

## Issue {#details}

During the installation, a message similar to the following displays:

```text
[ERROR] exception 'LogicException' with message 'Unknown module in the requested list: 'Magento_BundleSampleData''
```

## Solution {#solution}

Try each of the following one at a time, then try your installation again.

1. Run the Web Setup Wizard. Modules are listed in  **Advanced Modules Configurations**. To disable the **Magento\_BundleSampleData** module, clear the **Magento\_BundleSampleData** checkbox as the following figure shows.

    ![tshoot_bundlesampledata.png](assets/tshoot_bundlesampledata.png)

1. Clear all browser history and data from your web browser.
1. If you have Chrome, clear all browser data related to your site.  Go to **Settings** > **Advanced options** > **Privacy** > **Content Settings** > **All cookies and site data**. In the Site column, click the address of your Adobe Commerce server and click **Remove All**.
