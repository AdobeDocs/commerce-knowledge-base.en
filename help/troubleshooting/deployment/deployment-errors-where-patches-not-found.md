---
title: Patch not found errors during deployment or manual application
description: "This article provides a solution to the issue where you see an error *Next patches weren't found: MDVA-XXXXX, ACSD-XXXXX. Check the availability of these patches for the  current Magento version using the 'status' command*."
exl-id: 5a2fd35a-892a-48af-a41f-f275297b3e2e
---
# Patch not found errors during deployment or manual application

This article provides a solution to the issue when upgrading your instance the deployment fails and you see an error in the deployment logs: *Next patches weren't found: MDVA-XXXXX, ACSD-XXXXX. Check the availability of these patches for the  current Magento version using the "status" command*.

## Affected products and versions

* Adobe Commerce on cloud infrastructure, [all supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf).

## Issue

You are experiencing an error when upgrading Adobe Commerce: *Next patches weren't found*.

## Cause

Previously applied patches for your older version(s) are not applicable or no longer available for your new version.

This issue can also occur when the installed Quality Patches Tool package (`magento/quality-patches`) is outdated.
 
For example:
 
Case 1:
- A patch may have originally been available for 2.4.7-p9 in QPT 1.1.71
- A newer QPT release (for example, 1.1.72) may later add support for 2.4.7-p10
- If the customer upgrades Commerce to 2.4.7-p10 but keeps an older QPT version installed, QPT may not recognize that a compatible patch variant exists for 2.4.7-p10
 
Case 2:
- A patch may have been added in QPT 1.1.72
- If the customer keeps an older QPT version installed, QPT will not recognize that the patch exists
 
In these cases, applying the patch can fail with a message such as:

```
Next patches weren't found: ACSD-12345.
Check the availability of these patches for the  current Magento version using the "status" command.
```
 
This happens because the installed QPT version cannot map the current Commerce version to an applicable version of the patch.

## Solution

This issue is not limited to deployments that apply patches through `.magento.env.yaml`. The same underlying issue can also occur when applying a patch manually with:

```bash
vendor/bin/magento-patches apply <PATCH_ID>
```
For example:

```
Next patches weren't found: ACSD-12345
Check the availability of these patches for the  current Magento version using the "status" command.
```
In this case, the patch is not available for the Adobe Commerce version installed in the environment where the command is being run.

1. Check your `.magento.env.yaml` file under the QUALITY_PATCHES section, e.g.,

      ```yaml
      QUALITY_PATCHES:
       - MDVA-XXXXX
       - ACSD-XXXXX
      ```
      
1. Look up the patch IDs in the [Quality Patches Release Notes](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/release-notes.html) to check whether each one can be applied to the new version of Adobe Commerce you are upgrading to. 
1. If the patch does not apply to the new version of Adobe Commerce you want to upgrade to, remove the patch ID from the `.magento.env.yaml` file.
1. Once you have reviewed all the patch IDs indicated by the error, push the changes and redeploy. 

## Related reading

* [Apply patches](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/upgrade/apply-patches.html?lang=en#apply-a-patch-in-a-local-environment) in Commerce on Cloud Infrastructure Guide.
