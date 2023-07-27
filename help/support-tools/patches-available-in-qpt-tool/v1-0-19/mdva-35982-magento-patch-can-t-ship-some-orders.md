---
title: "MDVA-35982: Can't ship some orders"
description: The MDVA-35982 patch fixes the error when admin user restricted to a specific website cannot create a shipment for the order placed on same website. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.19 is installed. The patch ID is MDVA-35982. Please note that the issue was fixed in Adobe Commerce 2.4.3.
exl-id: f41c6572-66bb-4697-93e3-da34b81829e2
feature: "Orders, Shipping/Delivery"
role: Admin
---
# MDVA-35982: Can't ship some orders

The MDVA-35982 patch fixes the error when admin user restricted to a specific website cannot create a shipment for the order placed on same website. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.19 is installed. The patch ID is MDVA-35982. Please note that the issue was fixed in Adobe Commerce 2.4.3.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.3.5-p1

**Compatible with Adobe Commerce versions:**

Adobe Commerce (all deployment methods) 2.3.0 - 2.4.2

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Merchant is unable to ship certain orders.

<u>Steps to reproduce</u>:

1. Choose any product website for the product except the default store. See [Product in Websites](https://docs.magento.com/user-guide/catalog/settings-basic-websites.html) in our user guide for detailed steps.
1. Create a user role for the Admin with Custom Role Scopes, in which the default website/store is not selected. See [Define a role](https://docs.magento.com/user-guide/system/permissions-user-roles.html#define-a-role) in our user guide for detailed steps.
1. Open the product in edit mode and set a Group Price for this product, in **Advanced Pricing**. See [Group Price](https://docs.magento.com/user-guide/catalog/product-price-group.html) in our user guide for detailed steps.
1. Create an order with this product.
1. Log in under the Admin with this user role and create a shipment. See [Creating a Shipment](https://docs.magento.com/user-guide/sales/shipments-create.html) in our user guide for detailed steps.

<u>Expected results</u>:

The shipment is created.

<u>Actual results</u>:

The following error is displayed:

 `"0":"Notice: Undefined offset: XX in \/vendor\/magento\/module-catalog\/Model\/Product\/Attribute\/Backend\/GroupPrice\/AbstractGroupPrice.php on line 290"`

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
