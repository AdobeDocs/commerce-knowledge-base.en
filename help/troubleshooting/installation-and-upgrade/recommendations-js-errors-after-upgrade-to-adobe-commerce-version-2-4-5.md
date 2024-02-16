---
title: "[!UICONTROL Recommendations] [!DNL JS] errors after upgrade to Adobe Commerce version 2.4.5"
description: 'This article provides a fix for when after the upgrade to Adobe Commerce (all deployment methods), there are [!DNL JS] errors in the console related to the product [!UICONTROL Recommendations] modules.'
feature: Install, Upgrade
role: Developer
---
# [!UICONTROL Recommendations] [!DNL JS] errors after upgrade to Adobe Commerce version 2.4.5

This article provides a fix for when after the upgrade to Adobe Commerce (all deployment methods), there are [!DNL JS] errors in the console related to the product [!UICONTROL Recommendations] modules/units.

There are currently no plans to address this issue in future versions.

## Affected versions and products

* Adobe Commerce (all deployment methods) when upgrading to version 2.4.5

## Issue

The issue is caused by the storefront webpage still referring to some deleted product [!UICONTROL Recommendations] modules/units (blocks and/or widgets) on its home page [!DNL CMS].

<u>Steps to reproduce</u>:

1. Upgrade to Adobe Commerce 2.4.5.
1. Access the storefront webpage.
1. Right-click your mouse, and select **Inspect** to open the web inspector on your web browser.
1. Click the **[!UICONTROL Console]** tab.
1. Review the [!DNL JS] errors.

<u>Expected results</u>:

Successful upgrade with no [!DNL JS] errors.

<u>Actual results</u>:

Several different types of [!DNL JS] errors show in the web browser console.

## Workaround

As a workaround, you can review all the [!UICONTROL Recommendations] units you have used on the page and remove any deleted units.
