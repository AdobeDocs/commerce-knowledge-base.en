---
title: "ACSD-50345: reCAPTCHA issues during the checkout"
description: Apply the ACSD-50345 patch to fix the Adobe Commerce issue where the reCAPTCHA v2 and v3 validations are failed while placing orders and during the checkout.
---
# ACSD-50345: reCAPTCHA issues during the checkout

The ACSD-502345 patch fixes the issue where where the reCAPTCHA v2 and v3 validations are failed while placing orders and during the checkout. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.31 is installed. The patch ID is ACSD-50345. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.6 and 2.4.7.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.5-p1

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.4.3 - 2.4.5-p2

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

**Case #1**

Google reCAPTCHA v2 does not reload after submitting a failed payment.

<u>Steps to reproduce</u>

1. Configure **[!UICONTROL Google reCAPTCHA v2]** (*I'm not a robot*).
1. Enable the **[!UICONTROL reCAPTCHA]** for checkout.
1. Try to place an order without clicking on **[!UICONTROL reCAPTCHA]**.
1. Once you receive the error message for the missing reCAPTCHA (*reCAPTCHA validation failed, please try again*).
1. Click on the **[!UICONTROL reCAPTCHA]** and then try placing an order.

<u>Expected results</u>

Order will not be placed with an incorrect reCAPTCHA.

<u>Actual results</u>

Thrown an error *reCAPTCHA validation failed, please try again* and *No such cart with id = 4*

**Case #2**

Google reCAPTCHA v3 Invisible is not working on checkout and the order cannot be placed, `PlaceOrder` event was not triggered.