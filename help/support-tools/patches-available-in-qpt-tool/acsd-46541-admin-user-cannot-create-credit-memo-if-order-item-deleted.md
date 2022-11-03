---
 title: "ACSD-46541: An admin user cannot create a credit memo if an order item is deleted"
 description: "The ACSD-46541 patch fixes the issue where an admin user cannot create a credit memo if an order item is deleted. This patch is available when the [!DNL Quality Patches Tool (QPT)](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/announcements/commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.html) 1.1.21 is installed. The patch ID is ACSD-46541. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.6."
 ---

 # ACSD-46541: An admin user cannot create a credit memo if an order item is deleted

 The ACSD-46541 patch fixes the issue where an admin user cannot create a credit memo if an order item is deleted. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/announcements/commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.html) 1.1.21 is installed. The patch ID is ACSD-46541. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.6.

 ## Affected products and versions

 **The patch is created for Adobe Commerce version:**

 * Adobe Commerce (all deployment methods) 2.4.3-p1

 **Compatible with Adobe Commerce versions:**

 * Adobe Commerce (all deployment methods) 2.4.0 - 2.4.3-p3

 >[!NOTE]
 >
 >The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

 ## Issue

 Once a product is deleted you cannot create a credit memo in the Commerce admin. 

 <u>Steps to reproduce</u>:

 1. Log in to the Commerce Admin.
 1. Create an order.
 1. Invoice the order.
 1. Delete the product from the order.
 1. Click on the **Credit Memo** link on the order edit page.
 1. Click on **Refund Offline** to create a credit memo.

<u>Expected results</u>:

Credit Memo is created successfully.

<u>Actual results</u>:

**Following products with requested SKUs were not found: SKU001** error displays.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Quality Patches Tools > Usage](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html) in Adobe Experience League.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Additional steps required after the patch installation

 For On-premises users:

* Run: `composer require symfony/intl:"~5.4.11"`

For Cloud users:

* Run: `composer require symfony/intl:"~5.4.11"`
* Push `composer.json` and `composer.lock` files to the git repository along with the patch file.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/announcements/commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.html) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/support-tools/patches/check-patch-for-magento-issue-with-magento-quality-patches.html?lang=en) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) in Adobe Experience League.