---
title: 'MDVA-30599: customer_is_guest is set incorrectly'
description: The MDVA-30599 patch fixes the issue where guest quotes created using API are incorrectly marked as quotes for logged-in customers. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.6 is installed. The issue was fixed in Adobe Commerce 2.4.2.
exl-id: e16bb926-241b-451e-89a5-33000f73c5b7
---
# MDVA-30599: customer_is_guest is set incorrectly

The MDVA-30599 patch fixes the issue where guest quotes created using API are incorrectly marked as quotes for logged-in customers. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.6 is installed. The issue was fixed in Adobe Commerce 2.4.2.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.3.5-p2

**Compatible with Adobe Commerce versions:**

Adobe Commerce (all deployment methods) 2.3.4 - 2.4.0

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Guest quotes created using API are incorrectly marked as quotes for logged-in customers.

<u>Steps to reproduce</u>:

1. On the Adobe Commerce storefront, add a product to the cart as a guest user.
1. In your Adobe Commerce DB, find the corresponding `quote_id_mask`.
1. Send an API request to `quoteGuestCartRepositoryV1` Cart Repository interface for guest carts. It can be done via Swagger or cURL request.

```curl
curl -X GET "http://web2-73.sparta.corp.magento.com/dev/support/ee24dev/rest/all/V1/guest-carts/ToOwPtSBxkorkCLq6ztwupPd99y8zhky" -H "accept: application/json"
```

<u>Expected results</u>:

In response you get `"customer_is_guest": true`

<u>Actual results</u>:

In response you get `"customer_is_guest": false`

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Additional steps required after the patch installation

The patch will be effective for all new guest carts. If you need to fix existing guest carts, set `quote.customer_is_guest = 1` for those records where `quote.customer_id` is NULL. You could run a query similar to the following:

```sql
UPDATE quote SET customer_is_guest = 1 WHERE customer_id IS NULL;
```

>[!WARNING]
>
>We strongly recommend testing the query on the Staging/Integration environment before running it in Production. We also recommend having a recent backup before any manipulations with DB.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
