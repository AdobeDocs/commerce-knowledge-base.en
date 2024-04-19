---
title: How to obtain and apply [!UICONTROL security patch]
description: This article provides instructions on how to obtain and apply a [!UICONTROL security patch] that has been released, but instructions are unavailable.
---
# How to obtain and apply a [!UICONTROL security patch]

This article provides instructions on how to obtain and apply a [!UICONTROL security patch] that has been released, but instructions are unavailable.

## Affected products and versions 

Adobe Commerce On-Premise and Cloud - All versions

## Cause

Most [!UICONTROL Security Patches] are released without any physical file or hotfix to apply.

## Solution


### Case I:

If a physical patch file/hotfix is mentioned in the Release Notes:

* Download the file from the download section of [https://account.magento.com](https://account.magento.com/downloads/view/). (Shared access users must first be given download privileges by the account owner/license holder) 

**Caveats:**

If you are on an older version of Adobe Commerce and have purchased Extended Support, your version must be one of the following to be able to apply the Security Patches:

* 2.4.2-p2
* 2.4.3-p3

If you don't have Extended Support, you may request Support to share the patches with you, but they will not be able to resolve any issues/errors you may encounter when applying them.

### Case II:

If a physical patch file/hotfix is not mentioned in the Release Notes:

* **Cloud:**

1. Some [!UICONTROL Security Patches] might be included/released in the latest version of Cloud Tools Suite (ECE Tools) under Cloud Patches for Commerce - check the [Release Notes](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/release-notes/cloud-tools-suite), and if a security fix is mentioned in the release, upgrade the package to that version.
1. If the Release Notes do not mention a security fix, continue reading.

* **Cloud or On-Premise:**

* If a physical patch file/hotfix is not available, [upgrade the Adobe Commerce version on Cloud](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/upgrade/commerce-version) 2.4.X to the latest patch version 2.4.X-pY. 
* If a physical patch file/hotfix is not available, [upgrade the Adobe Commerce version On-Premise](https://experienceleague.adobe.com/en/docs/commerce-operations/upgrade-guide/implementation/perform-upgrade) 2.4.X to the latest patch version 2.4.X-pY.

## Related reading

* See [Release notes for Commerce Cloud Tools Suite](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/release-notes/cloud-tools-suite) in the *Adobe Commerce on Cloud Infrastructure Guide*.
* See [upgrade the Adobe Commerce version](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/upgrade/commerce-version) in the *Adobe Commerce on Cloud Infrastructure Guide*.
