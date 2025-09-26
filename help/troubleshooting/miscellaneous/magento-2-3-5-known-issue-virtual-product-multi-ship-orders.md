---
title: 'Adobe Commerce 2.3.5 known issue: virtual product multi-ship orders'
description: This article explains a known issue in Adobe Commerce 2.3.5 where a multi-shipping order containing a virtual product is not processed correctly.
exl-id: 34ce79a2-5157-492b-8ee4-bdc09aae0c40
feature: Orders, Products, Shipping/Delivery
role: Developer
---
# Adobe Commerce 2.3.5 known issue: virtual product multi-ship orders

This article explains a known issue in Adobe Commerce 2.3.5 where a multi-shipping order containing a virtual product is not processed correctly.

## Affected products and versions

* Adobe Commerce on-premises 2.3.5
* Adobe Commerce on cloud infrastructure 2.3.5

## Issue

<u>Steps to reproduce</u>:

1. On the storefront, add physical and virtual products to the cart.
1. Proceed to checkout and select **Check Out with Multiple Addresses**.
1. Add all the required information and place the order.

<u>Expected result</u>:

Orders are placed for all products successfully.

<u>Actual result</u>:

The order for the virtual product is empty.

## Fix

A fix will be available in Adobe Commerce 2.3.6, which is scheduled for release in Q4 2020.

## Related reading

In our support knowledge base:

* [Bulk action product count known issue in Adobe Commerce 2.3.5](/help/troubleshooting/miscellaneous/bulk-action-product-count-known-issue-in-magento-2-3-5.md)

In our developer documentation:

* [Adobe Commerce 2.3.5 Release Notes](https://commerce-docs.github.io/devdocs-archive/2.3/guides/v2.3/release-notes/release-notes-2-3-5-commerce.html#known-issues)
