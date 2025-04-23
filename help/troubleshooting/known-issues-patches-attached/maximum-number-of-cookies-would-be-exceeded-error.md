---
title: 'Maximum number of cookies would be exceeded error in Adobe Commerce'
description: Learn how to resolve the Adobe Commerce issue where an error occurs stating maximum number of cookies would be exceeded.
feature: Deploy, Support, Upgrade, Tools and External Services
role: Admin, Developer
---
# *Maximum number of cookies would be exceeded* error in Adobe Commerce

This article provides patches to resolve the error stating *Maximum number of cookies would be exceeded* in Adobe Commerce.

## Affected products and versions

Adobe Commerce (all deployment methods) 2.4.4 - 2.4.7, with one of the following patches applied:

* MDVA-12304 patch applied using the [[!DNL Quality Patches Tool (QPT)]](https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/release-notes)
* [APSB25-08 isolated security patch](/help/troubleshooting/known-issues-patches-attached/security-update-available-for-adobe-commerce-apsb25-08.md)
* [Cloud Patches for [!DNL Commerce] 1.1.4](https://experienceleague.adobe.com/en/docs/commerce-on-cloud/user-guide/release-notes/cloud-patches)

## Issue

Issues related to cookies in Adobe Commerce is causing the following error to appear in the error logs:

*report.WARNING: Unable to send the cookie. Maximum number of cookies would be exceeded.*

### Cause

The issue occurs because the maximum number of allowed cookies is set to *50*.

## Solution

1. Remove the MDVA-12304 patch if you applied it using the [!DNL Quality Patches Tool (QPT)].

    * For Adobe Commerce on cloud infrastructures, remove the patch from `.magento.env.yaml`.
    * For Adobe Commerce on-premises installations, run the following command to revert the patch:

        `vendor/bin/magento/quality-patches revert MDVA-12304`

1. Apply the attached patches according to your Adobe Commerce version:

    * For versions 2.4.4-p12, 2.4.5-p11, 2.4.6-p9 and 2.4.7-p4, apply the [ACSD-64710 patch](assets/acsd-64710_2.4.5-p11.patch.zip).
    
    * For versions 2.4.4-p13, 2.4.5-p12, 2.4.6-p10, 2.4.7-p5 and 2.4.8, apply the [ACSD-65562 patch](assets/acsd-65562_2.4.5-p12.patch.zip).

### Related reading

* [Apply patches](https://experienceleague.adobe.com/en/docs/commerce-operations/upgrade-guide/patches/apply) in the Adobe Commerce Upgrade guide
* [Best practices for distributing Adobe Commerce patches at scale](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/maintenance/patching-at-scale) in the Adobe Commerce Implementation Playbook
* [Release notes for Commerce Cloud Tools Suite](https://experienceleague.adobe.com/en/docs/commerce-on-cloud/user-guide/release-notes/cloud-tools-suite) in the Commerce on Cloud Guide. 
