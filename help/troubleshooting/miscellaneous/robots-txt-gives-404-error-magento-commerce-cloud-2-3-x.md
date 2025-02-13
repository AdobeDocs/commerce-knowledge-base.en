---
title: robots.txt gives 404 error Adobe Commerce on cloud infrastructure
description: This article provides a fix for when the `robots.txt` file throws a 404 error in Adobe Commerce on cloud infrastructure.
exl-id: 6f0b9f47-1901-4c43-88d8-fd992015d70f
feature: Cloud, Marketing Tools, Paas
role: Developer
---
# robots.txt gives 404 error Adobe Commerce on cloud infrastructure

This article provides a fix for when the `robots.txt` file throws a 404 error in Adobe Commerce on cloud infrastructure.

## Affected products and versions

Adobe Commerce on cloud infrastructure (all versions)

## Issue

The `robots.txt` file is not working and throws a Nginx exception. The `robots.txt` file is generated dynamically "on the fly." The `robots.txt` file is not accessible by the `/robots.txt` URL because Nginx has a rewrite rule which forcibly redirects all `/robots.txt` requests to the `/media/robots.txt` file that does not exist.

## Cause

This typically happens when Nginx is not configured properly.

## Solution

The solution is to disable the Nginx rule which redirects `/robots.txt` requests to the `/media/robots.txt` file. Merchants with enabled self-service can do it on their own, and merchants without self-service enabled need to create a support ticket.

If you do not have the self-service enabled (or not sure if it enabled), [submit a Magento Support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket) requesting removal of the Nginx redirect rule from `/robots.txt` requests to `/media/robots.txt`.

If you do have the self-service enabled, please upgrade ECE-Tools to at least 2002.0.12 and remove the Nginx redirect rule in your `.magento.app.yaml` file. You can refer to [Add site map and search engine robots](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure-store/robots-sitemap.html) in our developer documentation for more information.

## Related Reading

* [How to block malicious traffic for Magento Commerce Cloud on Fastly level](/help/how-to/general/block-malicious-traffic-for-magento-commerce-on-fastly-level.md) in our support knowledge base.
* [Add site map and search engine robots](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/configure-store/robots-sitemap) in our developer documentation.
* [Search Engine Robots](https://experienceleague.adobe.com/docs/commerce-admin/marketing/seo/seo-overview.html#search-engine-robots) in our user guide.
