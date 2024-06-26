---
title: Adobe commerce customers should apply a hotfix from Adobe
description: 'This article provides a fix for Adobe Commerce customers who are not compatible with any recent Google Maps versions from 3.54+.'
feature: Install, Upgrade
role: Developer
---
# Adobe commerce customers should apply a hotfix from Adobe

It is currently noticed that Adobe Commerce customers have no access to Google Maps in any version of Adobe Commerce anymore. This article provides a fix for Adobe Commerce customers who are not compatible with any recent Google Maps versions from 3.54+.

## Affected versions and products

* Versions of Adobe Commerce and/or other used technologies.
* Adobe Commerce *2.4.4* - *2.4.7* cloud and On-premises versions.

## Issue

On *June 14, 2024* Google Maps version *3.53* reached the end of life and was switched off by Google [https://developers.google.com/maps/documentation/javascript/versions#documentation-for-the-api-versions]

Adobe Commerce was not compatible with any recent Google Maps versions from 3.54+.

The incompatibility was caused by legacy `prototype.js script`, which loaded through `lib/web/legacy-build.min.js` overrides native Array.from function, which leads to a direct conflict with Google Maps API. [https://developers.google.com/maps/documentation/javascript/best-practices]

<u>Steps to reproduce</u> :

1. Go to **Content** > **Pages** > and click on a **New Page**.
1. Expand the content block and click on the edit **[!DNL PageBuilder]** button.
1. Drag the Map content block from the **[!DNL PageBuilder]** menu to page.

<u>Expected result:</u>

Google Maps should work as expected.

<u> Actual result:</u>

When dropping Map content block from **[!DNL PageBuilder]** menu to page, an error message is displayed. 

## Solution

In order to fix this issue, all the Adobe commerce customers should apply a hotfix from Adobe.

