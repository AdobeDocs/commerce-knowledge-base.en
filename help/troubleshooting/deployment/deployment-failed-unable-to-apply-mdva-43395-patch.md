---
title: 'Deployment failed: unable to apply MDVA-43395 patch'
description: This article provides a solution for the issue, where trying to apply the MDVA-43395 patch results in failed deployment.
exl-id: 5341be3a-a9d7-4a4b-9755-8c585c6922a4
feature: Deploy
role: Developer
---
# Deployment failed: unable to apply MDVA-43395 patch

This article provides a solution for the issue, where trying to apply the MDVA-43395 patch results in failed deployment.

## Affected products and versions

* Adobe Commerce on cloud infrastructure (all versions)

## Issue

You are not able to apply the MDVA-43395 patch.

## Cause

Cloud merchants do not need to apply the MDVA-43395 patch separately if they have [magento/magento-cloud-patches 1.0.16](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/release-notes/cloud-patches#v1016) installed, which already includes the patch.

## Solution

To resolve the issue, remove the MDVA-43395 and MDVA-43443 patches from the `m2-hotfixes` directory and redeploy.

If you were able to apply the MDVA-43443 patch via the `m2-hotfixes` directory, you would still need to remove it as mentioned above. Future versions of Adobe Commerce will have these patches already contained in them, so it could cause the deployment to fail if you were to upgrade later.

To verify if the patch has been applied, run the `vendor/bin/magento-patches -n status |grep 43443` command.
If it shows multiple results like this, then you should remove the MDVA-43443 patch from the `m2-hotfixes` folder:

```bash
$ vendor/bin/magento-patches -n status |grep 43443
║ MDVA-43443              │ Parser token new fix                                         │ Other           │ Adobe Commerce Support │ Applied     │ Patch type: Required                                     ║
║ N/A                     │ ../m2-hotfixes/MDVA-43443_EE_2.4.2-p2_COMPOSER_v1.patch      │ Other           │ Local                  │ Applied     │ Patch type: Custom                                       ║
```

## Related reading

* [How to apply a composer patch provided by Adobe](/help/how-to/general/how-to-apply-a-composer-patch-provided-by-magento.md) in our support knowledge base.
* [Cloud Patches for Commerce](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/release-notes/cloud-patches#v1016) in our developer documentation.
