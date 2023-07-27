---
title: 'Adobe Commerce 2.4.0: "Add selections to my cart" does not work'
description: This article provides a workaround for a broken button known issue in the Commerce Admin when managing a customer's shopping cart. When trying to add selected products to a customer's shopping cart, the **Add selections to my cart** button located on the bottom of the section does not work. This issue occurs on any Admin panel page that contains two **Add selections to my cart** buttons. A permanent fix will be available in Adobe Commerce 2.4.1.
exl-id: b0830ec2-2aea-4afb-8d02-e9c8f54283be
feature: "Orders, Shopping Cart"
role: Developer
---
# Adobe Commerce 2.4.0: "Add selections to my cart" does not work

This article provides a workaround for a broken button known issue in the Commerce Admin when managing a customer's shopping cart. When trying to add selected products to a customer's shopping cart, the **Add selections to my cart** button located on the bottom of the section does not work. This issue occurs on any Admin panel page that contains two **Add selections to my cart** buttons. A permanent fix will be available in Adobe Commerce 2.4.1.

## Affected products and versions

* Adobe Commerce 2.4.0 (all deployment methods)

## Issue

<u>Steps to reproduce</u>

1. Navigate to any Admin panel page that contains two **Add selections to my cart** buttons.
1. Select items to add to my cart.
1. Click the **Add selections to my cart** button located on the bottom of the section.

<u>Expected result</u>

All selections are added to my cart as expected.

<u>Actual result</u>

Adobe Commerce does not add your selections to my cart.

## Solution

The **Add selections to my cart** button located on the top of the page is still working. The issue is expected to be fixed in Adobe Commerce version 2.4.1, which is scheduled for release in Q4 1.

## Related reading

* [MerchDocs' Managing a Shopping Cart](https://docs.magento.com/user-guide/sales/shopping-assisted-cart-manage.html) in our user guide.
* [Adobe Commerce 2.4.0 known issue: raw message data display on storefront](/help/troubleshooting/storefront/magento-2.4.0-issue-storefront-raw-message-data-display.md) in our support knowledge base.
* [Adobe Commerce 2.4.0 known issue: Export Tax Rates does not work](/help/troubleshooting/miscellaneous/magento-2.4.0-known-issue-export-tax-rates-does-not-work.md) in our support knowledge base.
* [Adobe Commerce 2.4.0 known issue: Braintree payment methods do not show up in Multiple Addresses checkout](/help/troubleshooting/payments/magento-2.4.0-braintree-not-in-multiple-addresses-checkout.md) in our support knowledge base.
