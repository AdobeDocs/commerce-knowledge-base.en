---
title: "[!DNL UPS] shipping method integration migration from [!DNL SOAP] to [!DNL RESTful API]"
promoted: true
description: Apply a patch to deal with the [!DNL UPS] shipping method integration migration from [!DNL SOAP] to [!DNL RESTful API] for Adobe Commerce 2.4.4 - 2.4.6-pX.
feature: Shipping/Delivery
role: Developer
---
# [!DNL UPS] shipping method integration migration from [!DNL SOAP] to [!DNL RESTful API]

This article provides a patch to resolve issues with the [!DNL United Parcel Service (UPS)] shipping method integration migration from [!DNL SOAP] to [!DNL RESTful API] for Adobe Commerce 2.4.4 - 2.4.6-pX.

According to the latest updates to the [!DNL UPS API] Security Model, [!DNL UPS] has implemented an [!DNL OAuth 2.0] security model for all [!DNL APIs] (More details available in the [[!DNL UPS] Developer Portal Access Key Migration Guide](https://developer.ups.com/oauth-developer-guide?loc=en_US&sp_rid=NTA5MzQ1OTE2NjEyS0&sp_mid=72989914)) to enhance the overall security to reduce fraud and provide enhanced [!DNL API] capabilities.

This change impacts our current [!DNL UPS] shipping method integration implementation in Adobe Commerce and requires us to fix our current implementation and to migrate from [!DNL SOAP API] to the [!DNL RESTful API] to be able to support [!DNL OAuth 2.0] authentication protocols.

**Beginning in June 2024**, Adobe Commerce merchants will not be able to transact with our current [!DNL UPS] integration, so we are releasing this hotfix, which allows Adobe Commerce 2.4.4+/2.4.5+/2.4.6+ merchants to migrate to the latest [!DNL UPS REST APIs].

This issue will be fixed in Adobe Commerce/Magento Open Source version 2.4.7, and the fix will also be included in the 2.4.7-beta2 release in October 2023.
 
## Affected products and versions

Adobe Commerce on cloud infrastructure and on-premises, and Magento Open Source:

* 2.4.4 
* 2.4.4-pX
* 2.4.5
* 2.4.5-pX
* 2.4.6
* 2.4.6-pX

## Cause

The [!DNL UPS] released a [security update for their [!DNL API]](https://developer.ups.com/oauth-developer-guide?loc=en_US&sp_rid=NTA5MzQ1OTE2NjEyS0&sp_mid=72989914).

## Solution

Use the following attached patches, depending on your Adobe Commerce/Magento Open Source version:

To resolve the issue in the 2.4.4+, 2.4.5+, and 2.4.6+ versions, you must apply the corresponding patch to your version of Adobe Commerce/Magento Open Source below.

## Patch

Use the following attached patches, depending on your Adobe Commerce/Magento Open Source version:

### For versions 2.4.4, 2.4.4-pX:

* [AC-9363_UPS_Shipping_Method_Migration_REST_API_2.4.4x_COMPOSER.patch.zip](assets/AC-9363_UPS_Shipping_Method_Migration_REST_API_2.4.4x_COMPOSER.patch.zip)

### For versions 2.4.5, 2.4.5-pX:

* [AC-9358_UPS_Shipping_Method_Migration_REST_API_2.4.5x_COMPOSER.patch.zip](assets/AC-9358_UPS_Shipping_Method_Migration_REST_API_2.4.5x_COMPOSER.patch.zip)

### For versions 2.4.6, 2.4.6-pX:

* [AC-9345_UPS_Shipping_Method_Migration_REST_API_2.4.6x_COMPOSER.patch.zip](assets/AC-9345_UPS_Shipping_Method_Migration_REST_API_2.4.6x_COMPOSER.patch.zip)

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

