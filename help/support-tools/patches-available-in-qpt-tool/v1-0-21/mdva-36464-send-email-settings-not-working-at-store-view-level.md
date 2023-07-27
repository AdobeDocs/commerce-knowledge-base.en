---
title: 'MDVA-36464: Send email settings not working at store-view level'
description: The MDVA-36464 patch fixes the issue where send email settings are not working at the store-view level. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.21 is installed. The patch ID is MDVA-36464. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.3.
exl-id: cdf7e208-90ee-4711-8407-026da42fe3c8
feature: Communications
role: Admin
---
# MDVA-36464: Send email settings not working at store-view level

The MDVA-36464 patch fixes the issue where send email settings are not working at the store-view level. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.21 is installed. The patch ID is MDVA-36464. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.3.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.4.0-p1

**Compatible with Adobe Commerce versions:**

Adobe Commerce (all deployment methods) 2.4.0 - 2.4.2

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

<u>Prerequisite:</u>

Install clean Adobe Commerce.

<u>Steps to reproduce</u>:

1. Create an additional website, store, and store view (In this Example, the second website is *website2*).
1. Disable **Email notification** on the global level in **Store** > **Config** > **Advanced** > **System** > **Mail Sending Settings**.
1. Enable **Email notification** on the *website2* level (**Disable Email Communications** = *No*).
1. In Admin, create a new user, and assign it to the *website2*.
1. In Admin, on the customer edit page, click **Reset Password** for the customer created above in Step 4.

<u>Expected results</u>:

Both the **welcome email** and the **reset password email** are sent, as expected, because **Disable Email Communications** = *No* for the second website (Example: *website2*).

<u>Actual results</u>:

* The **welcome email** after the creation of the new customer is not triggered.
* The **reset password email** is not triggered.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
