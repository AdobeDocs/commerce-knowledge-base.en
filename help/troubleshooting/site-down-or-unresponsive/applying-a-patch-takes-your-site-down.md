---
title: Applying a patch takes your site down
description: This article talks about the issue where a patch you just applied takes your site down. To resolve it, you can remove the patch.
exl-id: dc765bcd-0761-4efd-a345-46a908d61272
feature: Cache
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: e7dae43f-215c-4cdf-90d3-c5a461a6e669
    internal-label: Admin tools and workspace
subfeature_v2:
  - id: b673188e-f9fa-492a-b470-c8f949bf7827
    internal-label: Cache
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Applying a patch takes your site down

This article talks about the issue where a patch you just applied takes your site down. To resolve it, you can remove the patch.

## Affected products and versions

* Adobe Commerce (all deployment methods), all supported versions
* Magento Open Source, all versions

## Issue

After you apply a patch, your site goes down.

## Cause

This issue might appear because of a version incompatibility between the patch you just applied to your website, your customizations, other patches you had applied in the past, or some other error.

## Solution

Remove the patch. The method of patch removal is different for Adobe Commerce on cloud infrastructure than for Adobe Commerce on-premises and Magento Open Source.

### Magento Open Source, all 1.X versions

For Magento Open Source 1.X versions,

* Run the following SSH command: `h SUPEE_patch --revert `

### Adobe Commerce on-premises, Magento Open Source, all 2.x versions

For Adobe Commerce on-premises and Magento Open Source 2.x versions,

1. Run the following SSH command:

    ```
    patch -p1 -R %patch_name%.composer.patch
    ```

    (If the above command does not work, try using `-p2` instead of `-p1`)

1. For the changes to be reflected, refresh the cache in the Admin under **System** > **Cache Management**.

### Adobe Commerce on cloud infrastructure, all versions

For Adobe Commerce on cloud infrastructure, all versions,

1. Remove the `%patch_name%.composer.patch` file(s) from the `m2-hotfixes` directory.
1. Commit and push your code changes:

    ```
    git commit -m "Remove %patch_name%.composer.patch patch" && git push origin
    ```

## Related reading

* [How to apply a composer patch provided by Adobe](https://experienceleague.adobe.com/en/docs/support-resources/adobe-support-tools-guide/adobe-commerce-support/how-to-apply-a-composer-patch-provided-by-magento) in our support knowledge base.
