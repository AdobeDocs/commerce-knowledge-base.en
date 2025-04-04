---
title: Extension Manager shows no extensions in Adobe Commerce 2.3.x
description: This article provides a workaround for missing extensions in the Admin Extension Manager in Adobe Commerce 2.3.x after you purchase extensions via the Commerce Marketplace.
exl-id: bed8506d-39b9-449a-891b-466d214a0fe8
feature: Extensions
role: Developer
---
# Extension Manager shows no extensions in Adobe Commerce 2.3.x

This article provides a workaround for missing extensions in the Admin Extension Manager in Adobe Commerce 2.3.x after you purchase extensions via the Commerce Marketplace.

## Affected products and versions

* Adobe Commerce version (all deloyment methods) 2.3.x

## Issue

When you purchase extensions via the Commerce Marketplace, you are unable to install them using the core Adobe Commerce Extension Manager. When you add your access keys and sync to the Marketplace, the Extension Manager shows no extensions.

The **Workaround** for the issue is to use the command line Adobe Commerce installation as shown in [General CLI installation](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/tutorials/extensions) in our developer documentation.

 <u>Steps to reproduce</u>:

1. Purchase an extension via the Commerce Marketplace.
1. Add your extension's access keys and sync to the Marketplace.
1. Go to the Extension Manager section of the Admin.

 <u>Expected result</u>:

The extension appears on the Extension Manager section of the Commerce Admin.

 <u>Actual result</u>:

**No extension appears on the Extension Manager section of the Commerce Admin, similar to the image below:**


![KB-607_Image_1.png](assets/KB-607_Image_1.png)

## Workaround

Use the command line Adobe Commerce installation as shown in [General CLI installation](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/tutorials/extensions) in our developer documentation.
