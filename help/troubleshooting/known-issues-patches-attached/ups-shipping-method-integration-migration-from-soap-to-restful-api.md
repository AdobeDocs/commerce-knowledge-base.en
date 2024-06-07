---
title: '[!DNL UPS] shipping method integration migration from [!DNL SOAP] to [!DNL RESTful API]'
promoted: true
description: Apply a patch to deal with the [!DNL UPS] shipping method integration migration from [!DNL SOAP] to [!DNL RESTful API] for Adobe Commerce 2.4.4 - 2.4.6-pX.
feature: Shipping/Delivery
role: Developer
exl-id: 8ab5d4a8-0155-4b2c-ab67-d0bd2f949a07
---
# [!DNL UPS] shipping method integration migration from [!DNL SOAP] to [!DNL RESTful API]

>[!NOTE]
>
>If you uploaded any of the three patches from this article prior to **June 6, 2024**: If you are facing this issue because of the [!DNL Metric System/SI] measurements (kilograms and centimeters) not being used, you should re-apply one of these new, updated patches now published in this article for your 2.4.4+/2.4.5+/2.4.6+ version of Adobe Commerce/Magento Open Source once again, because otherwise you will not be able to select the [!DNL Metric System/SI] measurements of **kilograms** and **centimeters** in the [!DNL UPS] shipping methods in the **[!DNL Admin configuration]**. These new patches are compatible with the previously released patches. This issue will be fixed permanently in scope of upcoming Adobe Commerce version 2.4.7-p1 release planned for **June 11, 2024**.

>[!NOTE]
>
>If you uploaded any of the three patches from this article prior to **October 10, 2023**, you should reapply one of these patches now published in this article for your 2.4.4+/2.4.5+/2.4.6+ version of Adobe Commerce/Magento Open Source once again, because otherwise you will not be able to select and configure specific [!DNL UPS] shipping methods in the **[!DNL Admin configuration]**, and you will have to have all of them enabled. These new patches are compatible with the previously released patches.

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

## Causes

The [!DNL UPS] released a [security update for their [!DNL API]](https://developer.ups.com/oauth-developer-guide?loc=en_US&sp_rid=NTA5MzQ1OTE2NjEyS0&sp_mid=72989914).

If you have European Union (other origins may experience the same problem) as Origin of the Shipment this will cause an error in the [!DNL UPS REST] request:
"*A shipment cannot have a KGS/IN or LBS/CM or OZS/CM as its unit of measurements.*"

## Solution

Use the following attached patches, depending on your Adobe Commerce/Magento Open Source version:

To resolve the issue in the 2.4.4+, 2.4.5+, and 2.4.6+ versions, you must apply the corresponding patch to your version of Adobe Commerce/Magento Open Source below.

## Patch

Use the following attached patches, depending on your Adobe Commerce/Magento Open Source version:

### For versions 2.4.4, 2.4.4-pX:

* [AC-11984_UPS_Shipping_Method_Migration_REST_API_2.4.4x_COMPOSER.patch.zip](assets/AC-11984_UPS_Shipping_Method_Migration_REST_API_2.4.4x_COMPOSER.patch.zip)

### For versions 2.4.5, 2.4.5-pX:

* [AC-11983_UPS_Shipping_Method_Migration_REST_API_2.4.5x_COMPOSER.patch.zip](assets/AC-11983_UPS_Shipping_Method_Migration_REST_API_2.4.5x_COMPOSER.patch.zip)

### For versions 2.4.6, 2.4.6-pX:

* [AC-11916_UPS_Shipping_Method_Migration_REST_API_2.4.6x_COMPOSER.patch.zip](assets/AC-11916_UPS_Shipping_Method_Migration_REST_API_2.4.6x_COMPOSER.patch.zip)

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
