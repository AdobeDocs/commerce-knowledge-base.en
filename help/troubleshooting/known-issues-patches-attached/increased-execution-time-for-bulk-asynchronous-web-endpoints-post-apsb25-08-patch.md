---
title: increased-execution-time-for-bulk-asynchronous-web-endpoints-post-apsb25-08-security-patch
description: This article provides a hotfix for the issue where POST rest/all/async/bulk/V1/products requests for 1000+ entries experience significantly increased execution time after applying the APSB25-08 security patch.
feature: Security, Cache, REST, Products, Customers
role: Admin, Developer
---
# Increased execution time for all bulk asynchronous web endpoints post APSB25-08 security patch

This article provides a hotfix for all bulk asynchronous web endpoints such as `POST rest/all/async/bulk/V1/products` with 1000+ entries that are experiencing significantly longer execution times after applying the APSB25-08 security patch.

## Affected products and versions

* Adobe Commerce (all deployment methods) 2.4.4, 2.4.4-p1, 2.4.4-p2, 2.4.4-p3, 2.4.4-p4, 2.4.4-p5, 2.4.4-p6, 2.4.4-p7, 2.4.4-p8, 2.4.4-p9, 2.4.4-p10, 2.4.4-p11, 2.4.4-p12

* Adobe Commerce (all deployment methods) 2.4.5, 2.4.5-p1, 2.4.5-p2, 2.4.5-p3, 2.4.5-p4, 2.4.5-p5, 2.4.5-p6, 2.4.5-p7, 2.4.5-p8, 2.4.5-p9, 2.4.5-p10, 2.4.5-p11

* Adobe Commerce (all deployment methods) 2.4.6, 2.4.6-p1, 2.4.6-p2, 2.4.6-p3, 2.4.6-p4, 2.4.6-p5, 2.4.6-p6, 2.4.6-p7, 2.4.6-p8, 2.4.6-p9

* Adobe Commerce (all deployment methods) 2.4.7, 2.4.7-p1, 2.4.7-p2, 2.4.7-p3, 2.4.7-p4

* Adobe Commerce (all deployment methods) 2.4.8

## Issue

After applying the APSB25-08 security patch, `POST rest/all/async/bulk/V1/products` requests with 1000+ entries are taking significantly longer time to execute.

<u>Steps to reproduce</u>:

1. Make a `POST rest/all/async/bulk/V1/products` request with 1000+ entries (name, SKU, and description are sufficient).
1. Note the time taken for the request.
1. Apply the APSB25-08 security patch and clean up generated data and cache using `se:di:co`.
1. Run `bin/magento c:f`.
1. Go to storefront to ensure cache and generated files are in place.
1. Repeat the request from step 1.
1. Note the increased time taken for the request.
1. Remove the APSB25-08 security patch, flush the cache, regenerate the code, and repeat the request from step 1 to confirm the execution time returns to normal. (Optional)

<u>Expected results</u>:

The execution time for `async/bulk` requests has increased significantly after applying the security patch.

<u>Actual results</u>:

The execution time for `async/bulk` requests should not have increased significantly after applying the security patch, although some increase in time is expected.

## Solution

To resolve the issue, apply the [AC-14078-2-4x-composer-patch.zip](assets/AC-14078-2-4x-composer-patch.zip).

## How to apply the patch

Unzip the file and see [How to apply a composer patch provided by Adobe](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/how-to/how-to-apply-a-composer-patch-provided-by-magento.html) in our support knowledge base for instructions.

## Related reading

* [Security update available for Adobe Commerce - APSB25-08](/help/troubleshooting/known-issues-patches-attached/security-update-available-for-adobe-commerce-apsb25-08.md)