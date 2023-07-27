---
title: Product comparison known issue in Adobe Commerce 2.3.5
description: This article provides recommendations on how to avoid a known [product comparison](https://docs.magento.com/user-guide/marketing/product-compare.html) issue in Adobe Commerce on-premises 2.3.5 and Adobe Commerce on cloud infrastructure 2.3.5.
exl-id: 1488e2db-4a5d-4963-b48e-b84f760582d1
feature: "Products, Storefront"
role: Admin
---
# Product comparison known issue in Adobe Commerce 2.3.5

This article provides recommendations on how to avoid a known [product comparison](https://docs.magento.com/user-guide/marketing/product-compare.html) issue in Adobe Commerce on-premises 2.3.5 and Adobe Commerce on cloud infrastructure 2.3.5.

## Affected products and versions

* Adobe Commerce on-premises 2.3.5
* Adobe Commerce on cloud infrastructure 2.3.5

## Issue

When a user tries to compare products from different store views and one product has an empty value for a comparable attribute, Adobe Commerce displays a corrupted Compare Products page.

## Solution

Specify non-empty values for comparable product attributes or use the default store view value for the attribute. Comparable attribute values cannot be empty.

>[!NOTE]
>
>Product attributes are set to be used for comparison using the **Comparable on Storefront** configuration setting. For more information, refer to the [Creating Product Attributes](https://docs.magento.com/user-guide/stores/attribute-product-create.html#step-4-describe-the-storefront-properties) in our user guide.

A fix will be available in Adobe Commerce 2.3.6, which is scheduled for release in Q4 2020.

You can view the fix in GitHub (please consider, that the fix did not go through regression testing and is not an official hot fix): <https://github.com/magento/magento2/pull/27662>

## Related reading

<ul><li>Adobe Commerce Support Knowledge Base articles for Adobe Commerce 2.3.5 known issues:<ul>
<li>
<p title="Multi-shipping orders with a virtual product not processed correctly in Adobe Commerce 2.3.5"><a href="/help/troubleshooting/miscellaneous/magento-2.3.5-known-issue-virtual-product-multi-ship-orders.md">Multi-shipping orders with a virtual product not processed correctly in Adobe Commerce 2.3.5</a></p>
</li>
<li><a href="/help/troubleshooting/miscellaneous/bulk-action-product-count-known-issue-in-magento-2.3.5.md">Bulk action product count known issue in Adobe Commerce 2.3.5</a></li>
<li>
<p title="Country payment method issue in Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.3.5 and 2.3.5-p1"><a href="/help/troubleshooting/known-issues-patches-attached/magento-2.3.5-2.3.5-p1-patch-country-payment-issue.md">Country payment method issue in Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.3.5 and 2.3.5-p1</a></p>
</li>
<li>
<p title="Adobe Commerce prompts customers to log in but provides invalid link"><a href="/help/troubleshooting/known-issues-patches-attached/magento-prompts-customers-log-in-invalid-link.md">Adobe Commerce prompts customers to log in but provides invalid link</a></p>
</li>
<li>
<p title="Patch for Amazon Pay checkout issue in Adobe Commerce 2.3.5-p1"><a href="/help/troubleshooting/payments/patch-for-amazon-pay-checkout-issue-in-magento-2.3.5-p1.md">Patch for Amazon Pay checkout issue in Adobe Commerce 2.3.5-p1</a></p>
</li>
</ul>
</li><li><a href="https://devdocs.magento.com/guides/v2.3/release-notes/release-notes-2-3-5-commerce.html#known-issues">Adobe Commerce 2.3.5 Known Issues</a> in our developer documentation</li></ul>
