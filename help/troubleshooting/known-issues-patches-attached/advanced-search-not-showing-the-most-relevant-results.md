---
title: Advanced search not showing the most relevant results
description: This article provides a patch for the known Adobe Commerce issue, where the Advanced search does not show most relevant results first.
exl-id: 88f0782d-ba7d-4f19-9761-7894d978d334
---
# Advanced search not showing the most relevant results

This article provides a patch for the known Adobe Commerce issue, where the Advanced search does not show most relevant results first.

## Affected versions {#Advancedsearchnotshowingmostrelevantresults-Affectedversions}

* Adobe Commerce (all deployment options) 2.x.x
* Magento Open Source 2.x.x

## Issue {#Advancedsearchnotshowingmostrelevantresults-Description}

The advanced search function is not returning the most relevant results first, like the quick search is doing. The issue does not depend on the selected search engine type.

 <u>Steps to reproduce:</u>

1. On the storefront, go to the quick search and search for "Fitted Jacket".
1. Notice "Orion Two-Tone Fitted Jacket" is the first result.
1. Go to advanced search and search for "Fitted Jacket" in the name field.

 <u>Expected result:</u>

The "Orion Two-Tone Fitted Jacket" is the first result when using Advanced search, as the most relevant result.

 <u>Actual result:</u>

The "Orion Two-Tone Fitted Jacket" is not the first result, though it is the most relevant.

## Solution {#Advancedsearchnotshowingmostrelevantresults-Solution}

To solve the issue, apply the patch attached to this article. To download it, scroll down to the end of the article and click the file name, or click the following link:

 [Download MDVA-7256\_EE\_2.1.7\_v1.composer.patch](assets/MDVA-7256_EE_2.1.7_v1.composer.patch.zip)

The patch adds the implementation for sorting by relevance for advanced search results as the default sorting field.

The patch is compatible with all affected versions and editions.

## How to apply the patch

For instructions, see [How to apply a composer patch provided by Adobe](https://support.magento.com/hc/en-us/articles/360028367731) in our support knowledge base.

## Attached files
