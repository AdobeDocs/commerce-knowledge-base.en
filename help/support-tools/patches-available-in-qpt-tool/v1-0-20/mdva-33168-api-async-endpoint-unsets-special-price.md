---
title: 'MDVA-33168: API async endpoint unsets special price'
description: The MDVA-33168 patch fixes the issue where using the API async endpoint to update a product attribute unsets a special price.
exl-id: 4dd26215-b140-4924-8f4d-0d062e5fda2d
feature: REST, Orders, Personalization
role: Admin
---
# MDVA-33168: API async endpoint unsets special price

The MDVA-33168 patch fixes the issue where using the API async endpoint to update a product attribute unsets a special price.

This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.20 is installed. The patch ID is MDVA-33168. Please note that the issue is planned to be fixed in Adobe Commerce version 2.4.3.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.3.3-p1

**Compatible with Adobe Commerce versions:**

Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.3.3 - 2.4.2

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

<u>Steps to reproduce</u>:

1. Create two websites with stores.
1. Go to **Stores > Configurations > Catalog > Catalog > Price > Catalog** and Set **Price Scope** = *Website*.
1. Create a *text-type* product attribute. Leave all the options to default.
1. Add the attribute created to the default attribute set.
1. Create a simple product to use with a bundle product.
1. Create a bundle product with the following Example options:
    * **Enable Product** = *Yes*.
    * **Attribute Set** = *Default*.
    * **Product Name** = *bundle-1*.
    * **SKU** = *bundle-1*.
    * **Dynamic SKU** = *Yes*.
    * **Price** = *$100.00*.
    * **Tax Class** = *Taxable Goods*.
    * **Stock Status** = *In Stock*.
1. Under **Bundle Items**, set these Example options:
    * **Ship Bundle Items** = *Together*.
    * **Option Title** = *test*, **Input Type** = *Radio Buttons*, **Required** checkbox = *checked*.
    * **Is Default** checkbox = *unchecked*.
    * **Name** = *simple-100*.
    * **SKU** = *simple-100*.
    * **Price** = *100.00*.
    * **Price Type** = *Fixed*.
    * **Default Quantity** = *1*.
    * **User Defined** checkbox = *unchecked*.
1. Switch the scope to the non-default store, and set the special price. (Example: on the **Advanced Pricing** page, set **Special Price** = *4%*, and **Price View** = *Price Range*.)
1. Update the new attribute only in the non-default store scope, like this Example:

    ```php
        PUT {{base_url}}/rest/en_au/async/V1/products/{{sku}}    {        "product": {            "custom_attributes": [                {                    "attribute_code": "text_attr",                    "value": 21                                   }            ]                    }    }
    ```

<u>Expected results</u>:

Other attribute values remain the same when updating a product attribute using async rest API, as expected.

<u>Actual results</u>:

The special price, that was set using async rest API under the store scope, gets removed.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to the [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
