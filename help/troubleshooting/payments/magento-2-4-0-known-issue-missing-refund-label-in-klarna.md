---
title: 'Adobe Commerce 2.4.0 known issue: missing "Refund" label in Klarna'
description: This article provides a workaround for a known issue in Admin for a missing **Refund** label in Klarna VBE (Vendor Bundled Extension). When in the Klarna portal conducting a refund, the **Refund** label is not displayed next to the Bundled product which was refunded.
exl-id: f08039b2-7f8b-481e-8ec8-1659e227744f
feature: B2B, Orders, Payments
role: Developer
---
# Adobe Commerce 2.4.0 known issue: missing "Refund" label in Klarna

This article provides a workaround for a known issue in Admin for a missing **Refund** label in Klarna VBE (Vendor Bundled Extension). When in the Klarna portal conducting a refund, the **Refund** label is not displayed next to the Bundled product which was refunded.

## Affected products and versions

* Adobe Commerce on-premises 2.4.0
* Adobe Commerce on cloud infrastructure 2.4.0

## Issue

<u>Prerequisites:</u>

* Klarna is enabled.
* A Bundled product is created.

<u>Steps to reproduce</u>

1. Go to Adobe Commerce frontend, and add a Bundled product to **cart**.
1. Navigate to checkout.
1. Input consumer information into checkout and click **Next**.
1. Select **KP option** and click **Place Order**.
1. Go to **Admin** > **Sales** > **Orders**.
1. Open the order.
1. Create Invoice for product.
1. Go to **Invoices** > **Select invoice** > Click **Credit Memo** > Click **Refund** (Not **Refund Offline**).
1. Go to Klarna portal.
1. Open the order.
1. The **Refund** label is present.

<u>Expected result</u>

On the Klarna portal, the **Refund** label is displayed next to the product which was refunded.

<u>Actual result</u>

On the Klarna portal, the **Refund** label is not displayed next to the product which was refunded.

## Workaround

The workaround for this issue is to ignore the missing **Refund** label in the Klarna portal for refunded bundled products. The refund has occurred, even though the **Refund** label did not display. The issue is expected to be fixed in Adobe Commerce 2.4.1, which is scheduled for release in Q4 2020.

## Related readings in our support knowledge base:

* [Adobe Commerce 2.4.0 known issue: raw message data display on storefront](/help/troubleshooting/storefront/magento-2-4-0-issue-storefront-raw-message-data-display.md)
* [Adobe Commerce 2.4.0 known issue: Export Tax Rates does not work](/help/troubleshooting/miscellaneous/magento-2-4-0-known-issue-export-tax-rates-does-not-work.md)
* [Adobe Commerce 2.4.0 known issue: Braintree payment methods do not show up in Multiple Addresses checkout](/help/troubleshooting/payments/magento-2-4-0-braintree-not-in-multiple-addresses-checkout.md)
* [Adobe Commerce 2.4.0 known issue: Error message selecting local payment method displayed for some countries during checkout](/help/troubleshooting/payments/magento-2-4-0-checkout-error-selecting-local-payments.md)
* [Adobe Commerce 2.4.0 known issue: 404 error when removing rewards points on multi-shipping checkout](/help/troubleshooting/storefront/magento-2-4-0-404-error-removing-rewards-points-on-multi-shipping-checkout.md)
* [Adobe Commerce 2.4.0 known issue: orders display error](/help/troubleshooting/storefront/magento-2-4-0-known-issue-orders-display-error.md)
* [Adobe Commerce 2.4.0 B2B Admin can't add configurable product to quote](/help/troubleshooting/miscellaneous/magento-2-4-0-b2b-admin-can-t-add-configurable-product-to-quote.md)
* [Shipping labels creation known issue in Adobe Commerce 2.4.0](/help/troubleshooting/known-issues-patches-attached/shipping-labels-creation-known-issue-in-magento-2-4-0.md)
* [Adobe Commerce 2.4.0 known issue - refresh on Customer's Activities does not work](/help/troubleshooting/miscellaneous/magento-2-4-0-refresh-on-customer-activities-does-not-work.md)
* [Adobe Commerce 2.4.0 known issue: “Add selections to my cart” button does not work](/help/troubleshooting/miscellaneous/magento-2-4-0-add-selections-to-my-cart-does-not-work.md)
