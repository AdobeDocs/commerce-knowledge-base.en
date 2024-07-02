---
title: Revised patches for Google Maps access loss on all Adobe Commerce versions
description: 'This article provides a fix for Adobe Commerce merchants who are not compatible with any recent [!DNL Google Maps] versions from 3.54+.'
feature: Install, Upgrade
role: Developer
---
# Revised patches for [!DNL Google Maps] access loss on all Adobe Commerce versions

This article provides a fix for Adobe Commerce merchants who are not compatible with any recent [!DNL Google Maps] versions from 3.54+. This fix is to solve the issue where Adobe Commerce merchants have no access to [!DNL Google Maps] in any version of Adobe Commerce anymore. 

## Affected versions and products

* Versions of Adobe Commerce and/or other used technologies.
* Adobe Commerce *2.4.4* - *2.4.7* on Cloud and On-Premises versions.

## Issue

On *June 14, 2024* [!DNL Google Maps] version *3.53* reached the end of life and was switched off by [!DNL Google].

For more information refer to [[!DNL Google Maps Platform: Maps JavaScript API]](https://developers.google.com/maps/documentation/javascript/versions#documentation-for-the-api-versions).

Adobe Commerce was not compatible with any recent [!DNL  Google Maps] versions from 3.54+.

The incompatibility was caused by legacy `prototype.js script`, which loaded through `lib/web/legacy-build.min.js` overrides native Array.from function, which leads to a direct conflict with [!DNL  Google Maps] API. 

Refer to [[!DNL Google Maps: JS Best Practices]](https://developers.google.com/maps/documentation/javascript/best-practices). 

<u>Steps to reproduce</u> :

1. Click on **[!UICONTROL Content]** > **[!UICONTROL Pages]** > and select a **[!UICONTROL New Page]**.
1. Expand the Content Block and click on the edit **[!DNL PageBuilder]** button.
1. Drag the Map Content Block from the **[!DNL PageBuilder]** menu to page.

<u>Expected result:</u>

[!DNL Google Maps] should work as expected.

<u> Actual result:</u>

When dropping the Map Content Block from **[!DNL PageBuilder]** menu to the page, an error message such as *"Sorry! Something went wrong"* is displayed.

## Solution

* All the merchants on any 2.4.4, 2.4.5, 2.4.6 or 2.4.7 patch version should apply these corresponding patches to their version.

## Patch 

Use the following attached patches, depending on the Adobe Commerce version:

**For versions 2.4.4:**
[ACSD-60245_Google_maps_API_2.4.4_2.4.5_2.4.6_composer.patch.zip](assets/ACSD-60245_Google_maps_API_2.4.4_2.4.5_2.4.6_composer.patch.zip)

**For versions 2.4.5:**
[ACSD-60245_Google_maps_API_2.4.4_2.4.5_2.4.6_composer.patch.zip](assets/ACSD-60245_Google_maps_API_2.4.4_2.4.5_2.4.6_composer.patch.zip)

**For versions 2.4.6:**
[ACSD-60245_Google_maps_API_2.4.4_2.4.5_2.4.6_composer.patch.zip](assets/ACSD-60245_Google_maps_API_2.4.4_2.4.5_2.4.6_composer.patch.zip)

**For versions 2.4.7:**
[ACSD-60245_Google_maps_API_2.4.7_composer.patch.zip](assets/ACSD-60245_Google_maps_API_2.4.7_composer.patch.zip)

**Please note** 

This issue will be permanently fixed in the scope of August security-only patch releases: 
2.4.7-p2, 2.4.6-p7, 2.4.5-p9, 2.4.4-p10

## Related Reading

[How to apply a composer patch provided by Adobe ](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/how-to/how-to-apply-a-composer-patch-provided-by-magento)