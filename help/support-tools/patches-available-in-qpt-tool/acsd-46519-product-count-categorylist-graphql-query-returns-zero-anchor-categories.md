---
title: "ACSD-46519: product count in `categoryList` graphql query returns 0 for anchor categories"
description: Apply the ACSD-CSD-46519 patch to fix the Adobe Commerce issue where when we use `categoryList` Graphql method to get child categories it shows the `product_count` as 0 for parent categories.
---

# ACSD-46519: product count in categoryList graphql query returns _0_ for anchor categories

The ACSD-46519 patch solves the issue where the product count in `categoryList` [!DNL Graphql] query returns _0_ for anchor categories. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.23 is installed. The patch ID is ACSD-46519. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.6. 

## Affected products and versions

**The patch is created for Adobe Commerce version:**
* Adobe Commerce (all deployment methods) 2.4.4

**Compatible with Adobe Commerce versions:**
* Adobe Commerce (all deployment methods) 2.4.1 - 2.4.5-p1

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

<u>Steps to reproduce</u>:

1. Log in to the Adobe Commerce Admin.
1. Create a category and subcategory.
1. Set the parent category as an anchored category.
1. Assign a product only to the child category.
1. Use the following [!DNL Graphql] request to get the category hierarchy with product count:

```
{
 categoryList(filters: { ids: { eq: "2" } }) {
    id
    name
    product_count
    level
    children {
      name
      product_count
      level
      children {
        name
        product_count
        level
        children {
          name
          product_count
          level
          children {
            name
            product_count
            level
          }
        }
      }
    }
  }
}
```

The response:

```
{
"data": {
"categoryList": [
{
"id": 2,
"name": "Default Category",
"product_count": 186,
"level": 1,
"children": [
{ "name": "What's New", "product_count": 0, "level": 2, "children": [] }
,
{
"name": "Women",
"product_count": 0,
"level": 2,
"children": [
{ "name": "Tops", "product_count": 0, "level": 3, "children": [] }
,
{ "name": "Bottoms", "product_count": 0, "level": 3, "children": [] }
]
},
{
"name": "Men",
"product_count": 0,
"level": 2,
"children": [
{ "name": "Tops", "product_count": 0, "level": 3, "children": [] }
,
{ "name": "Bottoms", "product_count": 0, "level": 3, "children": [] }
]
},
{
"name": "Gear",
"product_count": 33,
"level": 2,
"children": [
{ "name": "Bags", "product_count": 13, "level": 3, "children": [] }
,
{ "name": "Fitness Equipment", "product_count": 11, "level": 3, "children": [] }
]
},
{
"name": "Training",
"product_count": 6,
"level": 2,
"children": [
{ "name": "Video Download", "product_count": 6, "level": 3, "children": [] }
]
},
{ "name": "Sale", "product_count": 0, "level": 2, "children": [] }
]
}
]
}
}
```

<u>Expected results</u>:

If the parent category is an anchored category then the products count should show the sum of child category product counts.

<u>Actual results</u>:

If the parent category is an anchored category then the products is shown as _0_ unless you assign product directly to the parent category.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [[!DNL Quality Patches Tool] > Usage](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html) in the [!DNL Quality Patches Tool] guide.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about [!DNL Quality Patches Tool], refer to:

* [[!DNL Quality Patches Tool] released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using [!DNL Quality Patches Tool]](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) in the [!DNL Quality Patches Tool] guide.
