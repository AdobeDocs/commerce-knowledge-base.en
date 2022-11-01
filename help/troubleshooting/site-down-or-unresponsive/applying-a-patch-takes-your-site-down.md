---
title: Applying a patch takes your site down
description: "This article talks about the issue where a patch you just applied takes your site down. To resolve it, you can remove the patch."
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

* [How to apply a composer patch provided by Adobe](https://support.magento.com/hc/en-us/articles/360028367731) in our support knowledge base.
 

