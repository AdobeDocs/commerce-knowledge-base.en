---
title: Store credit issue during checkout in Adobe Commerce 2.3.5
description: This article provides a workaround for the known store credit-related issue during checkout in Adobe Commerce 2.3.5, where shoppers get errors during checkout after selecting and later removing store credit usage. A permanent fix will be available in Adobe Commerce 2.3.6.
exl-id: a0cca226-4d95-40b3-bd37-f13d28591366
---
# Store credit issue during checkout in Adobe Commerce 2.3.5

This article provides a workaround for the known store credit-related issue during checkout in Adobe Commerce 2.3.5, where shoppers get errors during checkout after selecting and later removing store credit usage. A permanent fix will be available in Adobe Commerce 2.3.6.

## Affected products and versions

* Adobe Commerce on-premises 2.3.5
* Adobe Commerce on cloud infrastructure 2.3.5

## Issue

<u>Steps to reproduce</u>:

1. Customer adds products to the cart and proceeds to checkout.
1. Customer specifies store credit as payment method.
1. Customer removes store credit and changes the payment method.
1. Customer proceeds through checkout.

<u>Expected results</u>:

All order information is displayed correctly.

<u>Actual results</u>:

Adobe Commerce throws an error on the Order Summary section of the Order page.

## Solution

Customers can refresh the Order page, and the information in the Order Summary will load correctly. A fix will be available in Adobe Commerce 2.3.6, which is scheduled for release in Q4 2020.

## Related reading

Articles for Adobe Commerce 2.3.5 known issues in our support knowledge base:

* [Multi-shipping orders with a virtual product not processed correctly in Adobe Commerce 2.3.5](/help/troubleshooting/miscellaneous/magento-2.3.5-known-issue-virtual-product-multi-ship-orders.md)

* [Country payment method issue in Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.3.5 and 2.3.5-p1](/help/troubleshooting/known-issues-patches-attached/magento-2.3.5-2.3.5-p1-patch-country-payment-issue.md)

* [Adobe Commerce prompts customers to log in but provides invalid link](/help/troubleshooting/known-issues-patches-attached/magento-prompts-customers-log-in-invalid-link.md)

* [Bulk action product count known issue in Adobe Commerce 2.3.5](/help/troubleshooting/miscellaneous/bulk-action-product-count-known-issue-in-magento-2.3.5.md)

* [Patch for Amazon Pay checkout issue in Adobe Commerce 2.3.5-p1](/help/troubleshooting/payments/patch-for-amazon-pay-checkout-issue-in-magento-2.3.5-p1.md)

* [Product comparison issue in Adobe Commerce 2.3.5](/help/troubleshooting/storefront/product-comparison-known-issue-in-magento-2.3.5.md)

In our developer documentation:

* [Adobe Commerce 2.3.5 Known Issues](https://devdocs.magento.com/guides/v2.3/release-notes/release-notes-2-3-5-commerce.html#known-issues)
