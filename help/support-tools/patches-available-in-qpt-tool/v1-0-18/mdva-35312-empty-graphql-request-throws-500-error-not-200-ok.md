---
title: 'MDVA-35312: empty GraphQL request throws 500 error not 200 OK'
description: The MDVA-35312 patch fixes the issue where an empty GraphQL request throws error response code 500. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.18 is installed. The patch ID is MDVA-35312. Please note that the issue was fixed in Adobe Commerce 2.4.3.
exl-id: 345fdbd4-8a43-4aab-a318-72792c8a7a78
feature: GraphQL
---
# MDVA-35312: empty GraphQL request throws 500 error not 200 OK

The MDVA-35312 patch fixes the issue where an empty GraphQL request throws error response code 500. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.18 is installed. The patch ID is MDVA-35312. Please note that the issue was fixed in Adobe Commerce 2.4.3.

## Affected products and versions

**The patch is created for Magento version:**

Adobe Commerce on cloud infrastructure 2.4.2

**Compatible with Magento versions:**

Adobe Commerce on-premises and Adobe Commerce on cloud infrastructure 2.4.1-p1-2.4.2

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Empty GraphQL request throws error response code 500 instead of 200 code.

<u>Steps to reproduce</u>:

Send a GraphQL request, for example:

```curl
curl -i -X OPTIONS http://inv.test/graphql
```

<u>Expected results</u>:

Response: *200 OK*.

<u>Actual results</u>:

Response: *HTTP/1.1 500 Internal Server Error*.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
