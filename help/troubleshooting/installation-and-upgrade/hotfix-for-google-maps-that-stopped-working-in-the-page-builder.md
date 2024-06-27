---
title: Adobe commerce users should apply a hotfix from Adobe
description: 'This article provides a fix for Adobe Commerce users who are not compatible with any recent Google Maps versions from 3.54+.'
feature: Install, Upgrade
role: Developer
---
# Adobe commerce users should apply a hotfix from Adobe

It is currently noticed that Adobe Commerce users have no access to Google Maps in any version of Adobe Commerce anymore. This article provides a fix for Adobe Commerce users who are not compatible with any recent Google Maps versions from 3.54+.

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

* All the users on any 2.4.4, 2.4.5 or 2.4.6 patch version should apply these corresponding patches to your version 

## Patch 

Use the following attached patches, depending on your Adobe Commerce version:

**For versions 2.4.4:**
[ACSD-60245_Google_maps_API_2.4.4_2.4.5_2.4.6_composer.patch.zip](assets/ACSD-60245_Google_maps_API_2.4.4_2.4.5_2.4.6_composer.patch.zip)

**For versions 2.4.5:**
[ACSD-60245_Google_maps_API_2.4.4_2.4.5_2.4.6_composer.patch.zip](assets/ACSD-60245_Google_maps_API_2.4.4_2.4.5_2.4.6_composer.patch.zip)

**For versions 2.4.6:**
[ACSD-60245_Google_maps_API_2.4.4_2.4.5_2.4.6_composer.patch.zip](assets/ACSD-60245_Google_maps_API_2.4.4_2.4.5_2.4.6_composer.patch.zip)

**For versions 2.4.7:**
[ACSD-60245_Google_maps_API_2.4.7_composer.patch.zip](assets/ACSD-60245_Google_maps_API_2.4.7_composer.patch.zip)


**Please note** 
The issue will be permanently fixed in the scope of August security-only patch releases: 
*2.4.7-p2, 2.4.6-p7, 2.4.5-p9, 2.4.4-p10*

## Related Reading

[How to apply a composer patch provided by Adobe ](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/how-to/how-to-apply-a-composer-patch-provided-by-magento)