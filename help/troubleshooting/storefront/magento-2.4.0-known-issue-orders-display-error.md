---
title: 'Adobe Commerce 2.4.0 known issue: orders display error'
description: 'This article provides a workaround for a known issue in Adobe Commerce for an orders display error. When logged-in customers review their orders in the **My Account** menu (**My Account &gt; My Orders**), the orders grid is unable to switch the number of orders per page to 20 from page 2 when there are 11 orders. Also, if there are more orders than is configured to be shown per page, when navigating to the last page with orders, changing the number of orders shown per page produces the error message: *You have placed no orders*. This issue will be resolved in Adobe Commerce 2.4.1.'
exl-id: a6d300e1-1cbc-42b9-997d-d72f8765517b
feature: B2B, Categories
---
# Adobe Commerce 2.4.0 known issue: orders display error

This article provides a workaround for a known issue in Adobe Commerce for an orders display error. When logged-in customers review their orders in the **My Account** menu (**My Account > My Orders**), the orders grid is unable to switch the number of orders per page to 20 from page 2 when there are 11 orders. Also, if there are more orders than is configured to be shown per page, when navigating to the last page with orders, changing the number of orders shown per page produces the error message: *You have placed no orders*. This issue will be resolved in Adobe Commerce 2.4.1.

## Affected products and versions

* Adobe Commerce on-premises 2.4.0
* Adobe Commerce on cloud infrastructure 2.4.0

## Issue

<u>Prerequisites</u>

* Adobe Commerce 2.4.0 is installed.
* Create at least one category and one simple product.

<u>Steps to reproduce</u>

1. Create 11 orders with products.
1. Go to **My Account**.
1. Go to **My Orders**.
1. Click the second page to display the 11th order on the orders grid.
1. Select **Show = 20 per page** from the drop-down menu.

<u>Expected result</u>

All 11 orders are displayed on the first page, as expected.

<u>Actual result</u>

The *You have placed no orders* error message is displayed.

## Workaround

The workaround is to have the buyer reopen **My Orders** page, and then the orders list will be displayed correctly. The issue will be fixed in the next release, Adobe Commerce 2.4.1, which is scheduled for release in Q4 2020.

## Related readings in our support knowledge base

* [Adobe Commerce 2.4.0 known issue - refresh on Customer's Activities does not work](/help/troubleshooting/miscellaneous/magento-2.4.0-refresh-on-customer-activities-does-not-work.md)
* [Adobe Commerce 2.4.0 Known Issue: Raw message data display on Storefront](/help/troubleshooting/storefront/magento-2.4.0-issue-storefront-raw-message-data-display.md)
* [Adobe Commerce 2.4.0 Known Issue: Export Tax Rates does not work](/help/troubleshooting/miscellaneous/magento-2.4.0-known-issue-export-tax-rates-does-not-work.md)
* [Adobe Commerce 2.4.0 B2B Admin can't add configurable product to quote](/help/troubleshooting/miscellaneous/magento-2.4.0-b2b-admin-can-t-add-configurable-product-to-quote.md)
