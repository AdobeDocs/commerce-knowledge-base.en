---
title: Deployment errors where patches are not found
description: "This article provides a solution to the issue where you see an error Next patches weren't found: <MDVA-XXXXX>, <ACSD-XXXXX>. Please, check with 'status' command availability of these patches for the current Magento version."
---

# Deployment errors where patches are not found

This article provides a solution to the issue when upgrading your instance the deployment fails and you see an error in the deployment logs: *Next patches weren't found: <MDVA-XXXXX>, <ACSD-XXXXX>. Please, check with "status" command availability of these patches for the current Magento version*

## Affected products and versions

* Adobe Commerce on cloud infrastructure, [supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf)


## Issue

You are experiencing an error when trying to update your Magento version. During the deployment you encounter the following error: * Next patches weren't found: <MDVA-XXXXX>, <ACSD-XXXXX>. Please, check with "status" command availability of these patches for the current Magento version.*

## Cause

Previously applied patches for your older version(s) are not applicable/no longer available for your new version.

## Solution

Check your `.magento.env.yaml` file under the QUALITY_PATCHES section, e.g.,

    ```yaml
QUALITY_PATCHES:
      - MDVA-12304
      - ACSD-55100
         ```

## Related reading

[Apply patches](/docs/commerce-cloud-service/user-guide/develop/upgrade/apply-patches.html?lang=en#apply-a-patch-in-a-local-environment) in Commerce on Cloud Infrastructure Guide
