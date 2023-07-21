---
title: 'Adobe Commerce 2.4.0: 404 error removing rewards points on multi-shipping checkout'
description: This article provides a workaround for a known issue in Adobe Commerce 2.4.0 for a "*404 Not Found*" web page error when removing rewards points on a multi-shipping checkout page. Currently, on the multi-shipping checkout page, when trying to remove reward points which were used to pay for an order,  a "*404 Not Found* " page is displayed instead of successful reward points cancellation. This issue will be resolved in with a Adobe Commerce 2.4.1 patch release.
exl-id: 59de4b3d-af28-4ae8-8f55-4ec958e6ee8b
feature: "B2B, Checkout"
---
# Adobe Commerce 2.4.0: 404 error removing rewards points on multi-shipping checkout

This article provides a workaround for a known issue in Adobe Commerce 2.4.0 for a "*404 Not Found*" web page error when removing rewards points on a multi-shipping checkout page. Currently, on the multi-shipping checkout page, when trying to remove reward points which were used to pay for an order,  a "*404 Not Found* " page is displayed instead of successful reward points cancellation. This issue will be resolved in with a Adobe Commerce 2.4.1 patch release.

## Affected products and versions

* Adobe Commerce 2.4.0 (all deployment methods)

## Issue

 <u>Steps to reproduce</u>

1. Navigate to the storefront and login as a customer.
1. Add at least two products to the **Shopping Cart**.
1. Open the **Mini-Cart**.
1. Click the **View and Edit Cart** link.
1. Click the **Check Out with Multiple Addresses** link.
1. Select shipping addresses on the **Ship to Multiple Addresses** page.
1. Click the **Go to Shipping Information** button.
1. Select the **Flat Rate &ndash; Fixed Shipping Method** for each address.
1. Click the **Continue to Billing Information** button.
1. Check the **Use Your Reward Points** checkbox on the **Billing Information** page.
1. Click the **Go to Review Your Order** button.
1. Click the **Remove** link for any address to remove the reward points.

 <u>Expected results</u>

* The **Shopping Cart** page should appear.
* The “*You removed the reward points from this order.* ” message should appear.

 <u>Actual result</u>

A "*404 Not Found* ” error page appears.

## Workaround

The workaround is to have the buyer navigate back to the **Cart** and remove the reward points from the **Cart** web page. The issue is expected to be fixed in the Adobe Commerce version 2.4.1 patch, which is scheduled for release in Q4 2020.

## Related reading

* [Adobe Commerce 2.4.0 known issue - refresh on Customer's Activities does not work](/help/troubleshooting/miscellaneous/magento-2.4.0-refresh-on-customer-activities-does-not-work.md)
* [Adobe Commerce 2.4.0 Known Issue: Raw message data display on Storefront](/help/troubleshooting/storefront/magento-2.4.0-issue-storefront-raw-message-data-display.md)
* [Adobe Commerce 2.4.0 Known Issue: Export Tax Rates does not work](/help/troubleshooting/miscellaneous/magento-2.4.0-known-issue-export-tax-rates-does-not-work.md)
* [Adobe Commerce 2.4.0 B2B Admin can't add configurable product to quote](/help/troubleshooting/miscellaneous/magento-2.4.0-b2b-admin-can-t-add-configurable-product-to-quote.md)
* [Adobe Commerce 2.4.0 known issue: Orders display error](/help/troubleshooting/storefront/magento-2.4.0-known-issue-orders-display-error.md)
