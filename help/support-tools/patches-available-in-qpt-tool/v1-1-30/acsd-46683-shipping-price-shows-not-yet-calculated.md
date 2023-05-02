---
title: 'ACSD-46683: Shipping price shows "Not yet calculated"'
description: Apply the ACSD-46683 patch to fix the Adobe Commerce issue where the shipping price shows *Not yet calculated*.
---
# ACSD-46683: Shipping price shows "Not yet calculated"

The ACSD-46683 patch fixes the issue where the shipping price shows *Not yet calculated*. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.30 is installed. The patch ID is ACSD-46683. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.7.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.3-p2

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.4.2 - 2.4.6

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

The shipping price shows *Not yet calculated*.

<u>Prerequisites</u>:

[!DNL Adobe Commerce] *[!UICONTROL Inventory Management]* (MSI) modules are installed.

<u>Steps to reproduce</u>:

1. Create a simple product and set its price to *$34*.
1. Configure the free shipping delivery method.
1. Configure at least one more delivery method.
1. Go to **[!UICONTROL Marketing]** > **[!UICONTROL Cart Price Rules]** and create a new rule.
    * Name = *75more* rule:
    * Coupon = None
    * Priority = 1
    * Conditions: Subtotal is or greater than *$75*
    * Actions:
        * 