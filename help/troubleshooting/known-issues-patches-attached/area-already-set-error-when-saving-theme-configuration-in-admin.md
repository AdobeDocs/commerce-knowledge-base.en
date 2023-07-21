---
title: '"Area already set" error when saving theme configuration in Admin'
description: This article provides a patch for the known Adobe Commerce on cloud infrastructure 2.2.4 issue related to getting the *"Area is already set"* error message when trying to set a theme for the Default Store View in the Commerce Admin.
exl-id: c4e34a73-b774-4447-ba8e-aaf208ad54c5
feature: Admin Workspace, Configuration
---
# "Area already set" error when saving theme configuration in Admin

This article provides a patch for the known Adobe Commerce on cloud infrastructure 2.2.4 issue related to getting the *"Area is already set"* error message when trying to set a theme for the Default Store View in the Commerce Admin.

## Issue

You get the " *Something went wrong while saving this configuration: Area is already set* " error message when trying to set a theme for the Default Store View.

<u>Steps to reproduce</u>:

1. Log in to the Commerce Admin.
1. Navigate to **Content** > **Design** > **Configuration**.
1. Set the configuration scope to *Default Store View*.
1. Change the theme in the **Applied Theme** drop-down. For example, from *Luma* to *Blank.*
1. Click **Save Configuration**.

 <u>Expected result</u>: The selected theme is applied for the default store view.

 <u>Actual result</u> : Theme is not applied, the *"Something went wrong while saving this configuration: Area is already set"* error message is displayed.

## Patch

The patch is attached to this article. To download it, click the following link or scroll down to the end of the article and click the attached file:

 [Download MDVA-11106\_EE\_2.2.4\_v1.composer.patch](assets/MDVA-11106_EE_2.2.4_v1.composer.patch.zip)

## Compatible Adobe Commerce versions:

The patch was created for:

* Adobe Commerce on cloud infrastructure 2.2.4

The patch is also compatible (but might not solve the issue) with the following Adobe Commerce versions and editions:

* Adobe Commerce on cloud infrastructure 2.0.X
* Adobe Commerce on cloud infrastructure 2.1.X
* Adobe Commerce on cloud infrastructure 2.2.0 - 2.2.5
* Adobe Commerce on-premises 2.0.X
* Adobe Commerce on-premises 2.1.X
* Adobe Commerce on-premises 2.2.0 - 2.2.5

## How to apply the patch

For instructions, see [How to apply a composer patch provided by Adobe](/help/how-to/general/how-to-apply-a-composer-patch-provided-by-magento.md) in our support knowledge base.

## Attached Files
