---
title: Bundle options order is not updated by import
description: This article provides a solution for the issue when after importing products from a .csv file, the bundle product options appear in a different order than they are listed in the import file.
exl-id: 7f7bf782-4b35-4067-aa94-417097079f1f
feature: Data Import/Export
role: Developer
---
# Bundle options order is not updated by import

This article provides a solution for the issue when after importing products from a .csv file, the bundle product options appear in a different order than they are listed in the import file.

## Affected products and versions

* Adobe Commerce on cloud infrastructure 2.2.x, 2.3.x
* Adobe Commerce on-premises 2.2.x, 2.3.x
* Magento Open Source

## Issue

<u>Prerequisites</u>:

You have a valid .csv file containing bundle products.

<u>Steps to reproduce</u>:

1. Import the file using the [Import functionality](https://experienceleague.adobe.com/en/docs/commerce-admin/systems/data-transfer/import/data-import).
1. Open the bundle product page.

<u>Expected results</u>:

The options order is the same as in the .csv file.

<u>Actual results</u>:

The options order is different from that in the .csv file.

## Cause

The options position was not declared explicitly.

## Solution

1. Declare a position explicitly for each option in the `position` parameter of the `bundle_values` column in the .csv file. For detailed instructions, see [Edit the Product Data](https://experienceleague.adobe.com/en/docs/commerce-admin/systems/data-transfer/examples/data-transfer-bundle-products#method-2-edit-the-product-data) in our user guide.
1. Repeat the import operation.

For general information on Import, see the [Importing Bundle Product](https://experienceleague.adobe.com/en/docs/commerce-admin/systems/data-transfer/examples/data-transfer-bundle-products) in our user guide.
