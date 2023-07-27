---
title: "'Area code is not set' error when running setup:updgrade"
description: This article provides a patch for the known Adobe Commerce on cloud infrastructure 2.2.3 issue related to getting the *"Area code is not set"* error when running the
exl-id: ace92331-6022-49fa-a776-d06d841b3b32
feature: "Install, Upgrade"
role: Developer
---
# 'Area code is not set' error when running setup:updgrade

This article provides a patch for the known Adobe Commerce on cloud infrastructure 2.2.3 issue related to getting the *"Area code is not set"* error when running the

```bash
setup:upgrade
```

command.

>[!NOTE]
>
>The issue was fixed in Adobe Commerce 2.2.4.

## Issue

When running the

```bash
bin/magento setup:upgrade
```

command, you get the following error message: *"Module 'Magento\_AdvancedSalesRule': Installing data...Area code not set: Area code must be set before starting a session"* and the command execution is interrupted. The issue appears because area configuration is requested before it is actually set. The patch allows catching the error and not interrupting the upgrade process.

## Patch

The patch is attached to this article. To download it, scroll down to the end of the article and click the file name, or click the following link:

 [Download MDVA-10439\_EE\_2.2.3\_COMPOSER\_v1.patch](assets/MDVA-10439_EE_2.2.3_COMPOSER_v1.patch.zip)

## Compatible Adobe Commerce versions:

The patch was created for:

* Adobe Commerce on cloud infrastructure 2.2.3

The patch is also compatible (but might not solve the issue) with the following Adobe Commerce versions and editions:

* Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.2.0 - 2.2.3

## How to apply the patch

For instructions, see [How to apply a composer patch provided by Adobe](/help/how-to/general/how-to-apply-a-composer-patch-provided-by-magento.md) in our support knowledge base.

## Attached Files
