---
title: Import CSV product information for same name product fails
description: This article provides a patch for the known Adobe Commerce 2.2.3 issue related to getting errors when trying to import a `.csv` file with products information if there are products with the same name.
exl-id: 420b0283-455a-4bd5-ba51-18f341ddacd5
feature: Data Import/Export, Products
role: Developer
---
# Import CSV product information for same name product fails

This article provides a patch for the known Adobe Commerce 2.2.3 issue related to getting errors when trying to import a `.csv` file with products information if there are products with the same name.

## Issue

When a `.csv` file with products information is imported, and there are products with the same name, you get the following error on the Check Data step: *"`URL Key XYZ was already generated for an item with the SKU %sku%"`*. The issue is caused by rewriting the products' URLs during import, even when there's no column for products' URLs in the imported `.csv` file.

<u>Steps to reproduce</u>:

1. Create two configurable products with the same name in the Commerce Admin.
1. Create a `.csv` file to import data for those products, which has for example these columns: `sku` | `product_type` | `name` | `product_websites` | `store_view_code`
1. Go to **System** > **Data Transfer** > **Import** and select the `.csv` file.
1. Click **Check Data**.

<u>Expected result</u>:

 No issues found; you can import the `.csv` file successfully.

 <u>Actual result</u>:

 The following error message is displayed: *"URL Key XYZ was already generated for an item with the SKU %sku%"*, it is not possible to import the file.

## Patch

The patch is attached to this article. To download it, scroll down to the end of the article and click the file name or click the following link:

 [Download MDVA-12899\_EE\_2.2.3\_COMPOSER\_v2.patch](assets/MDVA-12899_EE_2.2.3_COMPOSER_v2.patch.zip)

### Compatible Adobe Commerce versions:

The patch was created for:

* Adobe Commerce on-premises 2.2.3

The patch is also compatible (but might not solve the issue) with the following Adobe Commerce editions and versions:

* Adobe Commerce on cloud infrastructure from 2.2.0 to 2.2.7, and 2.3.0
* Adobe Commerce on-premises from 2.2.0 to 2.2.2, from 2.2.4 to 2.2.7, and 2.3.0

## How to apply the patch

See [How to apply a composer patch provided by Adobe Commerce](/help/how-to/general/how-to-apply-a-composer-patch-provided-by-magento.md) in our support knowledge base for instructions.

## Useful links

 [Apply custom patches to Adobe Commerce on cloud infrastructure](https://devdocs.magento.com/guides/v2.3/cloud/project/project-patch.html)

## Attached Files
