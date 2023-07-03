---
title: 'ACSD-50949: The price filter in advanced search does not return proper results when used along with the SKU filter'
description: Apply the ACSD-50949 patch to fix the Adobe Commerce issue where the price filter in advanced search does not return proper results when used along with the SKU filter.
---
# ACSD-50949: The price filter in advanced search does not return proper results when used along with the SKU filter

The ACSD-50949 patch fixes the issue where the price filter in advanced search does not return proper results when used along the SKU filter. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.33 is installed. The patch ID is ACSD-50949. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.7. 

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.5-p1

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.4.2 - 2.4.6-p1

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](<https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html>). Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.7.

## Issue

The price filter in advanced search does not return proper results when used along the SKU filter.

<u>Steps to reproduce</u>:

1. Create several products, for example

<table>
  <tr>
    <th>SKU</th>
    <th>Name</th>
    <th>Price</th>
    <th>Quantity</th>
  </tr>
  <tr>
    <td>MJ1</td>
    <td>Product 1</td>
    <td>$10</td>
    <td>10</td>
  </tr>
  <tr>
    <td>MJ2</td>
    <td>Product 2</td>
    <td>$15</td>
    <td>10</td>
  </tr>
  <tr>
    <td>MJ3</td>
    <td>Product 3</td>
    <td>$21</td>
    <td>10</td>
  </tr>
  <tr>
    <td>MJ4</td>
    <td>Product 4</td>
    <td>$32</td>
    <td>10</td>
  </tr>
  <tr>
    <td>MJ5</td>
    <td>Product 5</td>
    <td>$33</td>
    <td>10</td>
  </tr>
  <tr>
    <td>MJ6</td>
    <td>Product 6</td>
    <td>$34</td>
    <td>10</td>
  </tr>
  <tr>
    <td>MJ7</td>
    <td>Product 7</td>
    <td>$44</td>
    <td>10</td>
  </tr>
  <tr>
</table>
2. Open the **[!UICONTROL Advanced Search]** on the Storefront and search by SKU: "MJ".
1. Click the **[!UICONTROL Modify your search]** link.
1. Add a **[!UICONTROL price range]** to the criteria from *1* to *21*, and click the Search button.

<u>Expected results</u>:

Only products with prices in the defined range are returned.

<u>Actual results</u>:

Products with prices higher than *$21* are returned.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [[!DNL Quality Patches Tool] > Usage](<https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html>) in the [!DNL Quality Patches Tool] guide.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/upgrade/apply-patches.html) in the Commerce on Cloud Infrastructure guide.

## Related reading

To learn more about [!DNL Quality Patches Tool], refer to:

* [[!DNL Quality Patches Tool] released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using [!DNL Quality Patches Tool]](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [[!DNL Quality Patches Tool]: Search for patches](<https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html>) in the [!DNL Quality Patches Tool] guide.
