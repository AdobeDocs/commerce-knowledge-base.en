---
title: 'Adobe Commerce 2.4.0 known issue: Create New Order buttons missing'
description: This article provides a workaround for a known issue in the Commerce Admin for two missing buttons on the order creation page. When creating a new order for a new or existing customer, it is not possible to add products to the order from the catalog since the **Add Products By SKU** and **Add Products** buttons are missing. This is caused by JS bundling being enabled. A fix will be available in Adobe Commerce 2.4.1.
exl-id: 24ae880e-6d74-4444-9165-2744b12af81a
feature: B2B
---
# Adobe Commerce 2.4.0 known issue: Create New Order buttons missing

This article provides a workaround for a known issue in the Commerce Admin for two missing buttons on the order creation page. When creating a new order for a new or existing customer, it is not possible to add products to the order from the catalog since the **Add Products By SKU** and **Add Products** buttons are missing. This is caused by JS bundling being enabled. A fix will be available in Adobe Commerce 2.4.1.

## Affected products and versions

* Adobe Commerce on-premises 2.4.0
* Adobe Commerce on cloud infrastructure 2.4.0

## Issue

<u>Steps to reproduce</u>

1. Go to **Customers > All Customers**.
1. Click the **Edit** link on a customer.
1. Click the **Create Order** button.

<u>Expected result</u>

The **Add Products By SKU** and **Add Products** buttons appear on the **Create New Order** page.

<u>Actual result</u>

The **Add Products By SKU** and **Add Products** buttons are missing on the **Create New Order** page.

## Workaround

The workaround for this issue is to disable JS bundling for the Adobe Commerce instance. The issue is expected to be fixed in Adobe Commerce 2.4.1, which is scheduled for release in Q4 2020.

## Related readings in our support knowledge base

* [Adobe Commerce 2.4.0 known issue: raw message data display on storefront](/help/troubleshooting/storefront/magento-2.4.0-issue-storefront-raw-message-data-display.md)
* [Adobe Commerce 2.4.0 known issue: Export Tax Rates does not work](/help/troubleshooting/miscellaneous/magento-2.4.0-known-issue-export-tax-rates-does-not-work.md)
* [Adobe Commerce 2.4.0 known issue: Braintree payment methods do not show up in Multiple Addresses checkout](/help/troubleshooting/payments/magento-2.4.0-braintree-not-in-multiple-addresses-checkout.md)
* [Adobe Commerce 2.4.0 known issue: Error message selecting local payment method displayed for some countries during checkout](/help/troubleshooting/payments/magento-2.4.0-checkout-error-selecting-local-payments.md)
* [Adobe Commerce 2.4.0 known issue: 404 error when removing rewards points on multi-shipping checkout](/help/troubleshooting/storefront/magento-2.4.0-404-error-removing-rewards-points-on-multi-shipping-checkout.md)
* [Adobe Commerce 2.4.0 known issue: orders display error](/help/troubleshooting/storefront/magento-2.4.0-known-issue-orders-display-error.md)
* [Adobe Commerce 2.4.0 B2B Admin can't add configurable product to quote](/help/troubleshooting/miscellaneous/magento-2.4.0-b2b-admin-can-t-add-configurable-product-to-quote.md)
* [Shipping labels creation known issue in Adobe Commerce 2.4.0](/help/troubleshooting/known-issues-patches-attached/shipping-labels-creation-known-issue-in-magento-2.4.0.md)
* [Adobe Commerce 2.4.0 known issue - refresh on Customer's Activities does not work](/help/troubleshooting/miscellaneous/magento-2.4.0-refresh-on-customer-activities-does-not-work.md)
* [Adobe Commerce 2.4.0 known issue: “Add selections to my cart” button does not work](/help/troubleshooting/miscellaneous/magento-2.4.0-add-selections-to-my-cart-does-not-work.md)
