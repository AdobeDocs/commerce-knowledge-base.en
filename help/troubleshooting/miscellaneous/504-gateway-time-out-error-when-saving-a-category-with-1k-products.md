---
title: 504 gateway time-out error when saving a category with 1k+ products
description: This article suggests a solution for the timeout issue you might have, when performing operations with large categories (1k+ plus products).
exl-id: 1f4b0385-215d-4d3d-8704-986c090824aa
feature: Cache, Categories, Marketing Tools, Products
role: Developer
---
# 504 gateway time-out error when saving a category with 1k+ products

This article suggests a solution for the timeout issue you might have, when performing operations with large categories (1k+ plus products).

## Affected products and versions:

* Adobe Commerce on cloud infrastructure 2.3.3
* Adobe Commerce on-premises 2.3.3
* Magento Open Source 2.3.3

## Issue

Prerequisites: The **Stores** > **Configuration** > **CATALOG** > **Catalog** > **Use Categories Path for Product URLs** option is set to *Yes* for your store view.

 <u>Steps to reproduce</u>

1. In the Commerce Admin, go to **Catalog** > **Categories**.
1. Open a large category, like more than 1000 assigned products.
1. Add a product to the category.
1. Click **Save Category**.

 <u>Expected result:</u>

Category is saved successfully.

 <u>Actual result:</u>

After five minutes of saving process, the 504 gateway timeout error page appears.

## Cause

The process takes longer than the server's configured timeout.

## Solution

Disabling the **Generate "category/product" URL Rewrites** option will remove all category/product URL rewrites from the database, and significantly decrease the time required for the operations with big categories.

>[!WARNING]
>
>Turning this option off will result in permanent removal of category/product URL rewrites without an ability to restore them.

To disable the **Generate "category/product" URL Rewrites** option:

1. In the Commerce Admin, navigate to **Stores** > **Configuration** > **CATALOG** > **Catalog**.
1. In the top left corner of the configuration page, in the **Scope** field, set your configuration scope to *Default Config*.
1. Set **Generate "category/product" URL Rewrites** to *No*.
1. Click **Save Config**.
1. Clean cache by running    ```bash    bin/magento cache:clean    ```    or in the Commerce Admin under **System** > **Tools** > **Cache Management**.

Now you can proceed to adding products to categories, or moving categories with a large number of products, and these operations will take much less time and should not cause timeout.

## Related reading

[Automatic Product Redirects](https://experienceleague.adobe.com/en/docs/commerce-admin/marketing/seo/url-rewrites/url-redirect-product-automatic) in our user guide.
