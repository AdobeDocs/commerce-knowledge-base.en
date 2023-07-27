---
title: "MDVA-35569: FPT won't show in GraphQL"
description: The MDVA-35569 patch solves the issue when FPT (fixed product tax) doesn't show in GraphQL when the state is specified in the cart. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.19 is installed. The patch ID is MDVA-35569. Please note that the issue was fixed in Adobe Commerce version 2.4.3.
exl-id: 3c38f7f9-9372-4f22-819c-c53efb9b5f78
feature: GraphQL
role: Admin
---
# MDVA-35569: FPT won't show in GraphQL

The MDVA-35569 patch solves the issue when FPT (fixed product tax) doesn't show in GraphQL when the state is specified in the cart. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.19 is installed. The patch ID is MDVA-35569. Please note that the issue was fixed in Adobe Commerce version 2.4.3.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.3.4-p2

**Compatible with Adobe Commerce versions:**

Adobe Commerce (all deployment methods) 2.3.4-2.4.1-p2

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

<u>Steps to reproduce</u>:

1. Enable FPT.
1. Create an attribute (Example: *weee\_tax*).
1. Create a test product (Example: *weeetax*) with the *weee\_tax* attribute added.
1. Assign FPT to California or to another state on the *weee\_tax* attribute.
1. Create a customer in GraphQL.
1. Create a cart in GraphQL.
1. Add the *weetax* product to the cart with GraphQL.
1. Query the cart:

```php
{cart(cart_id: "xxx") {    items {    id    product {    name    sku    price_range {    minimum_price {    final_price {    value    }    fixed_product_taxes {    label    amount {    value    }    }    }    maximum_price {    final_price {    value    }    fixed_product_taxes {    label    amount {    value    }    }    }    }    }    prices {    price {    value    }    }    quantity    }    prices {    subtotal_excluding_tax {    value    }    applied_taxes {    amount {    value    }    }    grand_total {    value    currency    }    discounts {    amount {    value    }    label    }    }}}
```

<u>Expected results</u>:

The FPT would be populated normally, as expected.

<u>Actual results</u>:

* The FPT does not populate with data and is empty.
* The cart query gives this response:

```php
{
 "data": {
 "cart": {
 "items": [
 {
 "id": "1",
 "product": {
 "name": "fpt",
 "sku": "fpt",
 "price_range": {
 "minimum_price": {
 "final_price": {
 "value": 10
 },
 "fixed_product_taxes": []
 },
 "maximum_price": {
 "final_price": {
 "value": 10
 },
 "fixed_product_taxes": []
 }
 }
 },
 "prices": {
 "price": {
 "value": 10
 }
 },
 "quantity": 1
 }
 ],
 "prices": {
 "subtotal_excluding_tax": {
 "value": 10
 },
 "applied_taxes": [],
 "grand_total": {
 "value": 21,
 "currency": "USD"
```

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
