---
title: '[!UICONTROL Recommendations] [!DNL JS] errors after upgrade to Adobe Commerce version 2.4.5'
description: This article provides a fix for when after the upgrade to Adobe Commerce (all deployment methods), there are [!DNL JS] errors in the console related to the product [!UICONTROL Recommendations] modules.
feature: Install, Upgrade
role: Developer
exl-id: 51d899eb-48f7-48c5-8bda-bd72a4d28945
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 6388cf7b-8a81-5248-a1e4-7bb57bbe250f
    internal-label: Install
  - id: a8ae7a5a-6cdc-5922-bd0d-6feb44b04984
    internal-label: Upgrade
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
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
