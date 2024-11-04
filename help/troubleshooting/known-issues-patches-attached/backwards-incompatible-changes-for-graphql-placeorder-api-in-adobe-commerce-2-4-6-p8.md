---
title: 'Backwards incompatible changes for [!DNL GraphQL] `placeOrder` [!DNL API] in Adobe Commerce 2.4.6-p8'
promoted: true
description: This article provides a patch for the known Adobe Commerce version 2.4.6-p8 Cloud and On-premises issue when the `placeOrder` [!DNL GraphQL API] doesn't return an expected error response from previous version 2.4.6 patch versions, which may lead to a broken checkout experience for merchants using PWA storefront or any other [!DNL GraphQL API]-based storefront for their stores.
feature: Checkout, REST, GraphQL
role: Developer
---
# Backwards incompatible changes for [!DNL GraphQL] `placeOrder` [!DNL API] in Adobe Commerce 2.4.6-p8

This article provides a patch for the known Adobe Commerce version 2.4.6-p8 Cloud and On-premises issue when the `placeOrder` [!DNL GraphQL API] doesn't return an expected error response from previous version 2.4.6 patch versions, which may lead to a broken checkout experience for merchants using [!DNL PWA] storefront or any other [!DNL GraphQL API]-based storefront for their stores.

>[!NOTE]
>
>Please contact Support Services if you encounter any issues applying the patch.
 
## Affected products and versions

* Adobe Commerce on Cloud 2.4.6-p8
* Adobe Commerce on-premises 2.4.6-p8

## Issue

After the upgrade on Adobe Commerce 2.4.6-p8 security-only patch, the [`placeOrder` [!DNL GraphQL API]](https://developer.adobe.com/commerce/webapi/graphql/schema/cart/mutations/place-order/) doesn't return an expected error response as seen in any previous 2.4.6 patch versions. This may lead to a broken checkout experience for merchants using [!DNL PWA] storefront or any other [!DNL GraphQL API]-based storefront for their stores.

<u>Step to reproduce</u>:

Run the `placeOrder` [!DNL GraphQL] request where you expect an error response.

<u>Expected result</u>:

You receive an expected error response.

<u>Actual result</u>:

Instead of an expected error response, you receive a successful response, but with a new `errors` key that looks like this:

```
{
    "data": {
        "placeOrder": {
            "order": null,
            "__typename": "PlaceOrderOutput"
        }
    }
}
```

## Solution for Adobe Commerce on Cloud and Adobe Commerce On-premises Software

To solve the issue, apply the patch.
To download it, click the following link:

[ac-13283-composer-patch.zip](assets/ac-13283-composer-patch.zip)

## How to apply the patch

Unzip the file and see [How to apply a composer patch provided by Adobe](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/how-to/how-to-apply-a-composer-patch-provided-by-magento.html) in our support knowledge base for instructions.

## For Adobe Commerce on Cloud merchants only - How to tell whether patches have been applied

Considering that it isn't possible to easily check if the issue was patched, you might want to check whether the patch has been successfully applied. 

<u>You can do this by taking the following steps, using the sample file `VULN-27015-2.4.7_COMPOSER.patch` **as an example</u>**:

1. [Install the Quality Patches Tool](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html).
1. Run the command:<br>
 ![ac-13283-tell-if-patch-applied-code](assets/cve-2024-34102-tell-if-patch-applied-code.png)
1. You should see output similar to this, where VULN-27015 returns the *Applied* status:

    ```bash
    ║ Id            │ Title                                                        │ Category        │ Origin                 │ Status      │ Details                                          ║ ║ N/A           │ ../m2-hotfixes/VULN-27015-2.4.7_COMPOSER_patch.patch      │ Other           │ Local                  │ Applied     │ Patch type: Custom                                
    ```

<!-- For Step 2:
     ```bash
    vendor/bin/magento-patches -n status |grep "27015\|Status"
     ```
-->

