---
title: Product Recommendations not shown in Page Builder
description: This article provides a solution for the issue where the Product Recommendations option is not shown in Page Builder.
exl-id: e96a446b-2e64-47a6-ac1b-e73183da9fb8
feature: Page Builder, Configuration, Personalization, Products, Recommendations
role: Developer
---
# Product Recommendations not shown in Page Builder

This article provides a solution for the issue where the Product Recommendations option is not shown in Page Builder.

## Affected products and versions

* Adobe Commerce (all deployment methods)

## Issue

Product Recommendations option not showing in Page Builder.

## Cause

There is no option in Page Builder to add Product Recommendations. Product Recommendations for Page Builder is an optional module and is installed separately.

## Solution

1. Check if you have installed the module separately by running the command: `composer show magento/module-page-builder-product-recommendations`
1. If it returns the following message: *Package magento/module-page-builder-product-recommendations not found*, you will have to install it by running the command: `composer require magento/module-page-builder-product-recommendations`

By enabling Product Recommendations in Page Builder, you will be able to [add a recommendation unit](https://experienceleague.adobe.com/docs/commerce-admin/page-builder/add-content/recommendations.html) to any content created in Page Builder.

## Related reading

* [Add Content - Product Recommendations](https://experienceleague.adobe.com/docs/commerce-admin/page-builder/add-content/recommendations.html) in our user guide.
* [Install and Configure Product Recommendations](https://experienceleague.adobe.com/en/docs/commerce-merchant-services/product-recommendations/getting-started/install-configure) in our developer documentation.
* [Adobe Commerce User Guide](https://experienceleague.adobe.com/en/docs/commerce-admin/user-guides/home)
