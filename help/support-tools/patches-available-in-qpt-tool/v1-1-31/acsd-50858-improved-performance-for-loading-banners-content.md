---
title: "ACSD-50858: Improved performance for loading banners' content"
description: Apply the ACSD-50858 patch to fix the Adobe Commerce issue where banner performance is impacted in the cart/checkout page due to excessive DB queries and increased page loading time.
---
# ACSD-50858: Improved performance for loading banners' content

The ACSD-50858 patch fixes a banner performance issue in the cart/checkout page: *excessive DB queries and increased page loading time*. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.31 is installed. The patch ID is ACSD-50858. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.7.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.5-p1

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.4.4 - 2.4.6

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

Banner performance is impacted in the cart/checkout page due to *excessive DB queries and increased page loading time*.

However, refactoring the way banners' contents load decreased the number of DB queries by 99.99% and the page loading time by ~99%.

<u>Steps to reproduce</u>:

1. Log in to Admin and create a simple product.
1. Create a customer, either from Admin or from frontend, and add a shipping address for it.
1. Move banners.php to `magento_root/pub/` folder.
1. Generate banners using  `php pub/banners.php` command. It will generate, 10,000 simple banners and 1,000 banners with sales rules.
1. Log in to the customer created previously in the frontend.
1. Add the product created previously in the cart.
1. Go to the checkout page (checkout/cart).
1. Monitor the `banner/ajax/load` request loading time:

    * Without `bin/magento dev:query-log:enable`
    * With `bin/magento dev:query-log:enable`

        ```
        grep 'magento_banner_content' var/debug/db.log  | wc -l
        ```

<u>Expected results</u>:


