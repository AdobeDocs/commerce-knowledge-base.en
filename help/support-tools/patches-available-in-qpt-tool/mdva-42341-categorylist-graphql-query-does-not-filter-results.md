---
title: 'MDVA-42341: "categoryList" GraphQL query does not filter results'
labels: QPT patches,Quality Patches Tool,QPT,MQP,Support Tools,Magento,Adobe Commerce,cloud infrastructure,on-premises,GraphQL,categoryList,filter,2.4.2,2.4.2-p1,2.4.2-p2,2.4.3,2.4.3-p1,QPT 1.1.8
---

The MDVA-42341 patch solves the issue where the "categoryList" GraphQL query does not filter results if a request has the Store header. This patch is available when the [Quality Patches Tool (QPT)](https://support.magento.com/hc/en-us/articles/360047139492) 1.1.8 is installed. The patch ID is MDVA-42341. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.4.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.3-p1

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.4.2 - 2.4.3-p1

>![info]
>
>Note: the patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

The "categoryList" GraphQL query does not filter results if a request has the Store header.

<ins>Steps to reproduce</ins>:

1. Create a new Root Category and name it **root2**.
1. Create a second Website/Store/Storeview and assign **root2** to the new Store.
1. Create a new category under Default root category = category1.
1. Using a GraphQL request, get a categories list for the second website (use Header store = new).

<pre>
<code class="language-graphql">
{
  categoryList(filters: {name: {match: "category1"}}) {
    uid
    level
    name
    breadcrumbs {
      category_uid
      category_name
      category_level
      category_url_key
    }
  }
}
</code>
</pre>

<ins>Expected results</ins>:

Categories from the default Root Category are not listed in response since we are using a "new" store Header.

<ins>Actual results</ins>:

Categories from the default Root Category are available in results.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](https://support.magento.com/hc/en-us/articles/360047139492) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](https://support.magento.com/hc/en-us/articles/360047125252) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
