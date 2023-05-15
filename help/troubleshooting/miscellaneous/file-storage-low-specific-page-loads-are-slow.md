---
title: File storage low, specific page loads are slow
description: This article provides a solution for the issue of low disk space caused by large, rich images.
exl-id: 640c8f0d-f714-4cc1-a401-9264cfaf8e37
---
# File storage low, specific page loads are slow

This article provides a solution for the issue of low disk space caused by large, rich images.

## Affected products and versions

* Adobe Commerce on cloud infrastructure, all supported versions
* Adobe Commerce on-premises, all supported versions
* Magento Open Source, all supported versions

## Issue

Low disk storage and slow page loads can be caused by large, rich images using high amounts of storage in `pub/media/catalog/products` and the sharing of disk space between staging and production, (unless a dedicated staging environment is provisioned).

## Cause

Images are not optimized to balance performance with viewing quality.

## Solution

Before uploading images, optimize and compress them to balance performance with viewing quality. This helps increase space and reduce page load times. PNGs give smaller sizes for images with large areas of solid color. JPEGs give smaller sizes for everything else. Use the highest compression (without noticeable degradation). This is usually 60-80%.

Use [Fastly image optimization](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/cdn/fastly-image-optimization.html) to produce more storage efficient images.

## Related reading

To learn about managing your disk space (if you are on Adobe Commerce on cloud infrastructure) see [Manage disk space in Adobe Commerce](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/storage/manage-disk-space.html) in our developer documentation.
