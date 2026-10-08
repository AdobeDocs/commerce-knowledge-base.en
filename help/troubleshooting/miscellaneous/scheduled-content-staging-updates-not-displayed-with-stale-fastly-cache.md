---
title: Scheduled Content Staging updates not displayed with stale Fastly cache
description: This article provides a fix for when Adobe Commerce stores do not display scheduled updates when using Content Staging and Fastly. The issue is due to default enabled Fastly Soft Purge. This feature reduces application resource load and only regenerates a fresh cache on a second request. To resolve, you can enable Purge CMS page through the Commerce Admin to always regenerate and serve fresh content.
exl-id: becbffaa-b6dd-4e9b-894e-17901c40223a
feature: CMS, Cache, Page Content, Staging
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: ddbd0f6e-b569-5a04-8a70-55058777c373
    internal-label: CMS
  - id: 17d326fa-534a-55a5-b46f-8ae1de1e2f75
    internal-label: Page Content
  - id: 0054e3a7-7067-583b-bfd2-ab39dada9ab5
    internal-label: Staging
  - id: e7dae43f-215c-4cdf-90d3-c5a461a6e669
    internal-label: Admin tools and workspace
subfeature_v2:
  - id: b673188e-f9fa-492a-b470-c8f949bf7827
    internal-label: Cache
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Scheduled Content Staging updates not displayed with stale Fastly cache

This article provides a fix for when Adobe Commerce stores do not display scheduled updates when using Content Staging and Fastly. The issue is due to default enabled Fastly Soft Purge. This feature reduces application resource load and only regenerates a fresh cache on a second request. To resolve, you can enable Purge CMS page through the Commerce Admin to always regenerate and serve fresh content.

## Issue

Scheduled updates for a store content asset (page, product, block, etc.) are not displayed on storefront immediately after the start time of the update. This happens when updates have been scheduled using the [Content Staging](https://experienceleague.adobe.com/docs/commerce-admin/content-design/staging/content-staging.html) functionality.

## Cause

Due to Fastly's Soft Purge functionality (enabled by default), the Adobe Commerce storefront still receives the old (stale) cached content when sending **the first** request for the updated asset to Fastly. Fastly requires a second request to regenerate the site data.

As a result, Fastly may serve stale content until the second request for the updated content.

 **Expected caching:** After we schedule an update for a content asset using Content Staging, Adobe Commerce sends a request to update the cache to Fastly. Fastly invalidates the previous cached content (without deleting the content) and starts serving the updated content.

 **Actual caching:** If Fastly still serves the stale content when receiving **the first** request for the updated content, it will only send regenerated, correct content only after receiving **the second** request. This behavior has been implemented to reduce server load by renewing the cache only in areas with proven traffic, without regenerating the cache for the entire website. Fastly updates the cache gradually, saving the application resources.

## Solution

If serving stale content even for the first request is unacceptable, you may disable Soft Purge and enable Purge CMS page:

1. Log in to your local Commerce Admin as an administrator.
1. Go to **Stores** > **Configuration** > **Advanced** > **System** > **Full Page Cache**.
1. Expand **Fastly Configuration**, then expand **Advanced**.
1. Set **Use Soft Purge** to *No*.
1. Set **Purge CMS page** to *Yes*.
1. Click **Save Config** at the top of the page.


![purge_options.png](assets/purge_options.png)

## Related documentation

* [Configure purge options](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/cdn/setup-fastly/fastly-configuration.html) in the Commerce on Cloud Infrastructure Guide.
* [Content Staging](https://experienceleague.adobe.com/docs/commerce-admin/content-design/staging/content-staging.html) in the Content and Design documentation.
* [Serving stale content](https://docs.fastly.com/guides/performance-tuning/serving-stale-content) in Fastly documentation.
