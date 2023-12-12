---
title: Deployment errors where patches not found
description: "This article provides a solution to the issue where you see an error *Next patches weren't found: MDVA-XXXXX, ACSD-XXXXX. Please, check with "status" command availability of these patches for the current Magento version*."
---

# Deployment errors where patches not found

This article provides a solution to the issue when upgrading your instance the deployment fails and you see an error in the deployment logs: *Next patches weren't found: MDVA-XXXXX, ACSD-XXXXX. Please, check with "status" command availability of these patches for the current Magento version*.

## Affected products and versions

* Adobe Commerce on cloud infrastructure, [all supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf).


## Issue

You are experiencing an error when upgrading Adobe Commerce; *Next patches weren't found*.

## Cause

Previously applied patches for your older version(s) are not applicable or no longer available for your new version.

## Solution

1. Check your `.magento.env.yaml` file under the QUALITY_PATCHES section, e.g.,

      ```yaml
      QUALITY_PATCHES:
       - MDVA-XXXXX
       - ACSD-XXXXX
      ```
      
1. Look up the patch IDs in the [Quality Patches Release Notes](/docs/commerce-operations/tools/quality-patches-tool/release-notes.html) to check whether each one can be applied to the new version of Adobe Commerce you are upgrading to. 
1. If the patch does not apply to the new version of Adobe Commerce you want to upgrade to, remove the patch ID from the `.magento.env.yaml` file.
1. Once you have reviewed all the patch IDs indicated by the error, push the changes and redeploy. 

## Related reading

* [Apply patches](/docs/commerce-cloud-service/user-guide/develop/upgrade/apply-patches.html?lang=en#apply-a-patch-in-a-local-environment) in Commerce on Cloud Infrastructure Guide.

