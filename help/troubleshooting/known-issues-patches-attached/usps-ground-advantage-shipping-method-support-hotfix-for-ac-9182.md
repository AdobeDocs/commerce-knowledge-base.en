---
title: "[!DNL USPS] Ground Advantage shipping method support hotfix for AC-9182"
promoted: true
description: Apply a patch to deal with the [!DNL USPS] Ground Advantage shipping method issue AC-9182 for Adobe Commerce 2.4.4 - 2.4.6-p2.
feature: Shipping/Delivery
role: Developer
---
# [!DNL USPS] Ground Advantage shipping method support hotfix for AC-9182

This article provides a patch to resolve the issue AC-9182 for the new **[!DNL USPS] Ground Advantage** shipping method in Adobe Commerce 2.4.4 - 2.4.6-p2.

On July 9, 2023, The United States Postal Service ([!DNL USPS]) released a new shipping method, [[!DNL USPS] Ground Advantage](https://www.usps.com/ship/ground-advantage.htm).

This new shipping method is replacing their 3 main current shipping methods:

* [!DNL USPS] Retail Ground
* [!DNL USPS] First-Class Package Service
* [!DNL USPS] Parcel Select Ground

[[!DNL USPS] announced](https://faq.usps.com/s/article/USPS-Ground-Advantage#how_it_works) that starting from September 30, 2023, these 3 shipping methods will be discontinued and all customers must use the new **[!DNL USPS] Ground Advantage** method instead. 

So after September 30, 2023, all the Adobe Commerce merchants who are using the USPS shipping method will not be able to to get shipping rates from [!DNL USPS] by using these 3 legacy shipping methods anymore.

This issue will be fixed in scope of upcoming security-only patch releases in October, 2023, in versions 2.4.6-p3, 2.4.5-p5, and 2.4.4-p6.
 
## Affected products and versions

Adobe Commerce on cloud infrastructure and on-premises, and Magento Open Source:

* 2.4.4 
* 2.4.4-p1
* 2.4.4-p2
* 2.4.4-p3
* 2.4.4-p4 
* 2.4.4-p5
* 2.4.5
* 2.4.5-p1
* 2.4.5-p2 
* 2.4.5-p3
* 2.4.5-p4
* 2.4.6
* 2.4.6-p1
* 2.4.6-p2

## Cause

The [!DNL USPS] made an [!DNL API] update.

## Solution

To resolve the issue in the 2.4.4, 2.4.5, and 2.4.6 versions, you must apply AC-9182 patch below.

## Patch

The patch is attached to this article. To download it, click the following link:

[AC-9351_USPS_Ground_Advantage_shipping_method_COMPOSER_patch.zip](assets/AC-9351_USPS_Ground_Advantage_shipping_method_COMPOSER_patch.zip)

## How to apply the patch

Unzip the file and see [How to apply a composer patch provided by Adobe](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/how-to/how-to-apply-a-composer-patch-provided-by-magento.html) in our support knowledge base for instructions.

## How to tell whether the patches have been applied 

Considering that it is not possible to easily check if the issue was patched, you might want to check whether the AC-9182 patch has been successfully applied. 

<u>You can do this by taking the following steps</u>:

1. [Install the [!DNL Quality Patches Tool]](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html).
1. Run the command:

    ```bash
    vendor/bin/magento-patches -n status |grep "9182|Status"
    ```

1. You should see output similar to this, where AC-9182 returns the *Applied* status:

    ```bash
    ║ Id            │ Title                                                        │ Category        │ Origin                 │ Status      │ Details                                          ║ ║ N/A           │ ../m2-hotfixes/AC-9351_USPS_Ground_Advantage_shipping_method_COMPOSER_patch.patch      │ Other           │ Local                  │ Applied     │ Patch type: Custom                                
    ```

