---
title: '[!DNL FedEx] shipping method integration migration from SOAP to RESTful API'
promoted: true
description: Apply a patch to deal with the [!DNL FedEx] shipping method integration migration from SOAP to RESTful API for Adobe Commerce 2.4.4-p4 - 2.4.6-pX.
feature: Shipping/Delivery
role: Developer
exl-id: 7e11a171-6924-41d0-a5c7-7b794d0da84c
---
# [!DNL FedEx] shipping method integration migration from SOAP to RESTful API

>[!WARNING]
>
>Use the ACSD-61622 patch from [!DNL Quality Patches Tool] (QPT) 1.1.57 release instead of the previously provided patch. The new patch is compatible with Adobe Commerce versions (all deployment methods) 2.4.6-p1 - 2.4.6-p8. It might become applicable to other versions with new [!DNL Quality Patches Tool] releases. 
>
>For more information, refer to the [ACSD-61622 patch article](https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/patches-available-in-qpt/v1-1-57/acsd-61622-fedex-account-specific-rates-missing-from-response) in our Adobe Commerce Tools guide.

>[!WARNING]
>
>Before installing the new patch, you need to uninstall the previous patch provided in this article. For instructions on uninstalling patches, refer to [Revert a Custom Patch](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/upgrade/apply-patches#revert-a-custom-patch) in our user guide.


This article provides a patch to resolve issues with the [!DNL FedEx] shipping method integration migration from SOAP to RESTful API for Adobe Commerce 2.4.4-p4 - 2.4.6-pX. 

[!DNL FedEx Web Services] tracking, Address Validation, and Validate Postal Codes Web Services Definition Languages (WSDLS) was retired on May 15, 2024. The SOAP based [!DNL FedEx Web Services] is in development containment and has been replaced with [!DNL FedEx] RESTFUL APIs. To learn more, refer to [[!DNL FedEx Web Services]](https://www.fedex.com/en-us/developer/web-services.html).

This change impacts our current [!DNL FedEx] shipping method integration implementation in Adobe Commerce and requires we fix our current implementation and migrate from deprecated SOAP APIs to the latest [!DNL FedEx] RESTFUL APIs.

Beginning on May 15, 2024, Adobe Commerce customers will not be able to use our current [!DNL FedEx] shipping method integration, so Adobe is releasing this hotfix that allows Adobe Commerce 2.4.4+ customers to use the latest [!DNL FedEx] RESTFUL APIs instead of the deprecated SOAP ones.


## Affected products and versions

Adobe Commerce on cloud infrastructure and on-premises, and Magento Open Source:

* 2.4.4-p4
* 2.4.5
* 2.4.5-pX
* 2.4.6
* 2.4.6-pX

## Cause

The [!DNL FedEx] deprecated their SOAP based APIs and replaced them with the RESTful ones instead. Refer to [[!DNL FedEx Web Services]](https://www.fedex.com/en-us/developer/web-services.html).

## Solution

Use the following attached patches, depending on your Adobe Commerce/Magento Open Source version:

To resolve the issue in the 2.4.4+, 2.4.5+, and 2.4.6+ versions, you must apply the corresponding patch to your version of Adobe Commerce/Magento Open Source below.

## Patch

Use the following attached patches, depending on your Adobe Commerce/Magento Open Source version:

### For versions 2.4.4-p4:

* [FedexPatch-Composer-245p5-244p6develop.patch.zip](assets/FedexPatch-Composer-245p5-244p6develop.patch.zip)

### For versions 2.4.5, 2.4.5-pX:

* [FedexPatch-Composer-245p5-244p6develop.patch.zip](assets/FedexPatch-Composer-245p5-244p6develop.patch.zip)


### For versions 2.4.6, 2.4.6-pX:


* [FedexPatch-Composer-246p3develop.patch.zip](assets/FedexPatch-Composer-246p3develop.patch.zip)


## How to apply the patch

Unzip the file and see [How to apply a composer patch provided by Adobe](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/how-to/how-to-apply-a-composer-patch-provided-by-magento.html) in our support knowledge base for instructions.

## How to tell whether the patches have been applied

Considering that it is not possible to easily check if the issue was patched, you might want to check whether the patch has been successfully applied. This uses (Example: *AC-9363*) as the patch to check.

<u>You can do this by taking the following steps</u>:

1. [Install the [!DNL Quality Patches Tool]](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html).
1. Run the command:

    ```bash
    vendor/bin/magento-patches -n status |grep "9363|Status"
    ```

1. You should see output similar to this, where AC-9363 returns the *Applied* status:

    ```bash
    ║ Id            │ Title                                                        │ Category        │ Origin                 │ Status      │ Details                                          ║ ║ N/A           │ ../m2-hotfixes/AC-9363_USPS_Ground_Advantage_shipping_method_COMPOSER_patch.patch      │ Other           │ Local                  │ Applied     │ Patch type: Custom                                
    ```
