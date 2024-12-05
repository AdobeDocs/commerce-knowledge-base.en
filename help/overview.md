---
title: Adobe Commerce Support Knowledge Base
description: Everything you need to know to troubleshoot and maintain your Commerce store.
exl-id: feacf38f-2803-4170-a64f-5d7c4567432d
feature: Support
role: Admin
---
# Adobe Commerce Support Knowledge Base

>[!NOTE]
>
>The Adobe Commerce Support Knowledge Base Guide will soon be restructured, with its content being moved to other locations within Adobe Experience League. In the meantime, we will continue to maintain and update the content in this guide.

![Knowledge Base homepage](../help/assets/knowledge-base-home-page-cover.jpg){width="100%"}

The information in this Knowledge Base is designed as complementary to [Adobe Commerce Developer Documentation](https://developer.adobe.com/commerce/docs), and [Adobe Commerce Merchant Guide](https://experienceleague.adobe.com/docs/commerce-admin/user-guides/home.html), and other Adobe Commerce publications. It covers troubleshooting and best practices, hosts announcements, answers FAQs, and highlights specific scenarios that have not been mentioned (for any reason) in the official documentation.

## What is in this Knowledge Base?

| CATEGORY | DESCRIPTION | 
| --- | --- |
| [Support Tools](/help/support-tools/overview.md) | Improve your e-commerce store experience with the different support tools provided by Adobe Commerce. We provide personalized best practices, diagnostic and monitoring tools, and the most relevant information about your site. |
| [Announcements](/help/announcements/overview.md) | Get important updates from the Adobe Commerce teams. |
| [Troubleshooting](/help/troubleshooting/overview.md) | Get self-service solutions and patches from the Adobe Commerce Support team. |
| [Help Center User Guide](/help/help-center-guide/help-center/magento-help-center-user-guide.md) | Learn how to manage your support tickets, grant shared access, and browse the Knowledge Base effectively. |
| [How-To](/help/how-to/overview.md) | Get clear step-by-step instructions from the Adobe Commerce Support team. |
| [FAQ](/help/faq/overview.md) | Find frequently asked questions about Adobe Commerce policies, strategies, and specifics about Adobe Commerce features. | 

## What's New

<table style="width:100%">
  <tr>
    <th style="width:70%">Description</th>
    <th style="width:15%">Type</th>
    <th style="width:15%">Date</th>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-25301">Resolve New Relic agent issues with PHP 8.2 to 8.3 upgrade in Adobe Commerce:</a> When you upgrade PHP from version 8.2 to 8.3, you might notice that the New Relic agent stops working in your Adobe Commerce environment. This issue has been observed in staging and production environments. In this article, you'll find steps to troubleshoot and resolve this issue.
    </td>
    <td>New article </td>
    <td>December 5, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-25321">Security Scan Tool returns "APSByy-xx security updates available" even if the patch is already applied:</a> The Security Scan Tool reports APSByy-xx security updates available for Adobe Commerce and Magento Open Source even though you have already applied the patch. You may disregard this notification.
    </td>
    <td>New article </td>
    <td>December 5, 2024</td>
  </tr>
  
  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/patches-available-in-qpt/v1-1-54/acsd-61845-error-occurs-for-requests-with-text-html-accept-header">ACSD-61845: Error occurs for requests with text/html accept header:</a> The ACSD-61845 patch fixes the issue where an HTTP request with only a text/html accept header causes a 500 error due to media type mismatches in response handling. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.54 is installed.
    </td>
    <td>New article </td>
    <td>December 5, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/patches-available-in-qpt/v1-1-54/acsd-61200-fixes-discount-tax-compensation-in-sales-total-calculations">ACSD-61200: Incorrect discount tax compensation in sales total calculations:</a> The ACSD-61200 patch fixes the issue where Discount Tax Compensation Amount and Shipping Discount Tax Compensation Amount are missing from Total Amount and Total Amount Actual calculations, resulting in discrepancies between sales order data and coupon report data. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.54 is installed.
    </td>
    <td>New article </td>
    <td>December 5, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/patches-available-in-qpt/v1-1-54/acsd-61199-cms-page-hierarchy-tab-doesnt-display-proper-tree-structure">ACSD-61199: CMS page's Hierarchy tab doesn't display proper tree structure:</a> The ACSD-61199 patch fixes the issue where the CMS page's Hierarchy tab doesn't display a proper tree structure when editing a CMS page with an existing Hierarchy. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.54 is installed.
    </td>
    <td>New article </td>
    <td>December 5, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/patches-available-in-qpt/v1-1-53/acsd-60804-editing-customer-linked-to-deleted-company-causes-error">ACSD-60804: Editing a customer associated with a deleted company results in an error:</a> The ACSD-60804 patch fixes the issue where editing a customer associated with a deleted company causes an error <em>Call to a member function getSuperUserId() on null</em>. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.53 is installed.
    </td>
    <td>New article </td>
    <td>December 5, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/patches-available-in-qpt/v1-1-54/acsd-61522-email-in-name-fields-sends-invalid-order-confirmations">ACSD-61522: Email addresses in First and Last Name fields send invalid order confirmations:</a> The ACSD-61522 patch fixes the issue where it is possible to enter email addresses into a guest customer's First Name and Last Name fields, leading to invalid order confirmation emails being sent. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.54 is installed.
    </td>
    <td>New article </td>
    <td>December 5, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/patches-available-in-qpt/v1-1-54/acsd-62485-async-operations-all-consumer-stops-working-when-company-is-created">ACSD-62485: <code>async.operations.all</code> consumer stops working when company is created:</a> The ACSD-62485 patch fixes the issue where the <code>async.operations.all</code> consumer stops working when a B2B company is created. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.54 is installed.
    </td>
    <td>New article </td>
    <td>December 5, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/patches-available-in-qpt/v1-1-52/acsd-60684-graphql-product-sorting-by-multiple-fields-does-not-work-as-expected">ACSD-60684: GraphQL product sorting by multiple fields does not work as expected:</a> The ACSD-60684 patch fixes the issue where GraphQL product sorting by multiple fields doesn't work when the sorting is passed in variables. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.52 is installed.
    </td>
    <td>New article </td>
    <td>December 5, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/patches-available-in-qpt/v1-1-53/acsd-61553-cart-price-rule-discounts-are-incorrectly-calculated-when-multiple-discounts-with-different-priorities-are-applied">ACSD-61553: Cart Price Rule is incorrectly calculated when multiple discounts with different priorities are applied:</a> The ACSD-61553 patch fixes the issue where the Cart Price Rule is incorrectly calculated when multiple discounts with different priorities are applied. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.53 is installed.
    </td>
    <td>New article </td>
    <td>December 5, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/patches-available-in-qpt/v1-1-55/acsd-58383-duplicate-credit-memos-from-simultaneous-refund-requests-via-rest-api">ACSD-58383 Adobe Commerce patch: Duplicate credit memos from simultaneous refund requests via REST API:</a> The ACSD-58383 patch fixes the issue where issuing a refund via the REST API with two identical requests that are executed simultaneously, results in duplicate credit memos. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.55 is installed.
    </td>
    <td>New article </td>
    <td>December 5, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/patches-available-in-qpt/v1-1-55/acsd-58471-dynamic-content-fails-load-product-detail-page">ACSD-58471: Dynamic content fails to load on the product detail page, when the associated catalog price rules were scheduled:</a> The ACSD-58471 patch solves the issue where dynamic content fails to load on the product detail page, when the associated catalog price rules were scheduled. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.55 is installed.
    </td>
    <td>New article </td>
    <td>December 5, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/patches-available-in-qpt/v1-1-55/acsd-58735-restricted-admin-cant-view-abandoned-shopping-carts">ACSD-58735: Restricted admin can't view abandoned shopping carts on customer account for associated website:</a> The ACSD-58735 patch fixes the issue where an admin user with a restricted role is unable to view abandoned customers' shopping carts from the <strong>[!UICONTROL Commerce Admin]</strong> > <strong>[!UICONTROL Reports]</strong> > <strong>[!UICONTROL Abandoned Carts]</strong> > <strong>[!UICONTROL Select Cart]</strong> > <strong>[!UICONTROL Shopping Cart]</strong> tab. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.55 is installed.
    </td>
    <td>New article </td>
    <td>December 5, 2024</td>
  </tr>
</table>
