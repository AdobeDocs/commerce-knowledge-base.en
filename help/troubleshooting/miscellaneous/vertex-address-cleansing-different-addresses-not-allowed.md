---
title: 'Vertex Address Cleansing: different addresses not allowed'
description: This article talks about the solution for the issue where when the user tries to enter a **different** billing and shipping address, with Vertex address validation enabled, the storefront will not let the user enter it.
exl-id: a481b044-3b74-4792-abc6-249a182c49e1
feature: B2B, Orders, Shipping/Delivery, Checkout
role: Developer
---
# Vertex Address Cleansing: different addresses not allowed

This article talks about the solution for the issue where when the user tries to enter a **different** billing and shipping address, with Vertex address validation enabled, the storefront will not let the user enter it.

## Affected products and versions

* Adobe Commerce on-premises and Adobe Commerce on cloud infrastructure 2.3.5-p1

## Issue

<u>Steps to reproduce</u>:

1. Go to Admin > **Stores** > **Configuration** > **Sales** > **Address Cleansing**.
1. Select *Enabled* from the **Use Vertex Address Cleansing** drop-down and **Save Config**.
1. Go to the frontend as a guest and add a product to the cart.
1. Click on the Cart icon and **Proceed to Checkout**.
1. Fill in the address fields.
1. Select desired **Shipping Method** and click **Next**.
1. Click on the **Next** button again.
1. Uncheck **My billing and shipping address** **are the same**, and enter a new billing address (different to Address).
1. Click the **Update** button, then click **Update address**.

<u>Expected results</u>:

The user sees different billing and shipping addresses.

<u>Actual results</u>:

When the user hits update, the billing and shipping addresses revert to being the same.

## Cause

Vertex address verification has failed.

## Solution

Disable Vertex Address verification or upgrade to 2.4.0.

## Related reading

* [Adobe Commerce 2.4.0 known issue: Error message selecting local payment method displayed for some countries during checkout](/help/troubleshooting/payments/magento-2.4.0-checkout-error-selecting-local-payments.md)
* [Adobe Commerce 2.4.0 known issue: 404 error when removing rewards points on multi-shipping checkout](/help/troubleshooting/storefront/magento-2.4.0-404-error-removing-rewards-points-on-multi-shipping-checkout.md)
* [Adobe Commerce 2.4.0 known issue: orders display error](/help/troubleshooting/storefront/magento-2.4.0-known-issue-orders-display-error.md)
* [Adobe Commerce 2.4.0 B2B Admin can't add configurable product to quote](/help/troubleshooting/miscellaneous/magento-2.4.0-b2b-admin-can-t-add-configurable-product-to-quote.md)
* [Adobe Commerce 2.4.0 known issue: Braintree payment methods do not show up in Multiple Addresses checkout](/help/troubleshooting/payments/magento-2.4.0-braintree-not-in-multiple-addresses-checkout.md)
* [Shipping labels creation known issue in Adobe Commerce 2.4.0](/help/troubleshooting/known-issues-patches-attached/shipping-labels-creation-known-issue-in-magento-2.4.0.md)
* [Adobe Commerce 2.4.0 known issue - refresh on Customer's Activities does not work](/help/troubleshooting/miscellaneous/magento-2.4.0-refresh-on-customer-activities-does-not-work.md)
* [Adobe Commerce 2.4.0 known issue - Export Tax Rates does not work](/help/troubleshooting/miscellaneous/magento-2.4.0-known-issue-export-tax-rates-does-not-work.md)
* [Adobe Commerce 2.4.0 known issue: "Add selections to my cart" button does not work](/help/troubleshooting/miscellaneous/magento-2.4.0-add-selections-to-my-cart-does-not-work.md)
* [Adobe Commerce 2.4.0 known issue: raw message data display on storefront](/help/troubleshooting/storefront/magento-2.4.0-issue-storefront-raw-message-data-display.md)
* [Adobe Commerce 2.4.0 known issue: missing "Refund" label in Klarna](/help/troubleshooting/payments/magento-2.4.0-known-issue-missing-refund-label-in-klarna.md)
* [Adobe Commerce 2.4.0 known issue: two buttons missing on Create New Order page in Admin](/help/troubleshooting/miscellaneous/magento-2.4.0-known-issue-create-new-order-buttons-missing.md)
* [Adobe Commerce 2.4.0 known issue: when Braintree is enabled, Venmo partial invoice issue](/help/troubleshooting/payments/magento-2.4.0-2.4.1-enable-braintree-venmo-partial-invoice-issue.md)
* [Adobe Commerce 2.4.0 known issue: Error message selecting local payment method displayed for some countries during checkout](/help/troubleshooting/payments/magento-2.4.0-checkout-error-selecting-local-payments.md)
* [Adobe Commerce 2.4.0 known issue: Amazon Pay enabled, payment methods missing when Return to standard checkout used](/help/troubleshooting/payments/magento-2.4.0-known-issue-amazon-pay-no-payment-methods.md)
* [Adobe Commerce 2.4.0 known issue: 2.4.0 installation fails with outdated stores cache](/help/troubleshooting/installation-and-upgrade/magento-2.4.0-known-issue-2.4.0-installation-fails-with-outdated-stores-cache.md)
