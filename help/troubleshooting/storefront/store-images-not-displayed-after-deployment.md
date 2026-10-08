---
title: Store images not displayed after deployment
description: This article provides a solution for when images are not being displayed correctly after deployment.
exl-id: 7e6bcebd-edff-437a-9103-2743443d2ed9
feature: Cache, Categories, Deploy, Storefront
role: Admin
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: bcd8874c-7b93-5596-bdaa-22660e84df14
    internal-label: Deploy
  - id: d1e21356-0064-4f48-9089-16e3f0dbd2a6
    internal-label: Storefront
  - id: e7dae43f-215c-4cdf-90d3-c5a461a6e669
    internal-label: Admin tools and workspace
  - id: c18ed297-2187-4aec-affb-9d9654eca6fc
    internal-label: Catalog management
subfeature_v2:
  - id: b673188e-f9fa-492a-b470-c8f949bf7827
    internal-label: Cache
  - id: e91a50b1-0b31-436e-9033-00e4776e94cb
    internal-label: Categories
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
---
# Store images not displayed after deployment

This article provides a solution for when images are not being displayed correctly after deployment.

## Affected products and versions

* Adobe Commerce on cloud infrastructure 2.2.x, 2.3.x

## Issue

When you use a storefront theme with image resizing, the images do not display or disappear from catalog pages when deployed.

## Cause

This may occur due to loading the images from the cache.

## Solution

If this happens, you can use the Magento command to regenerate the image cache and properly display the images.

To perform this, you need the SSH information and the store URL available through the [Cloud Console](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/overview.html).

1. SSH to your project that was a source for the [database dump](/help/how-to/general/create-database-dump-on-cloud.md), as described in [SSH to environment](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/secure-connections) in our developer documentation.
1. Regenerate the image cache by running:

    ```bash
    php bin/magento catalog:images:resize
    ```

1. Test the category pages through the store URL.
