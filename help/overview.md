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
>The Adobe Commerce Support Knowledge Base Guide will soon be discontinued, with its content being moved to other locations within Adobe Experience League. In the meantime, we will continue to maintain and update the content in this guide.

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
    <a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-25075">Security Scan Tool returns "Can't determine if your server uses 2FA":</a> To resolve the error, check whether the <code>Magento_TwoFactorAuth</code> module has been disabled. To pass the check, in general, it should be enabled.
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/patches-available-in-qpt/v1-1-51/acsd-60632-address-saved-on-every-order-attempt">ACSD-60632: Address saved with every order attempt:</a> The ACSD-60632 patch fixes the issue where a new address is saved with each order placement attempt, regardless of whether the order is successfully created or not. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.51 is installed.
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/patches-available-in-qpt/v1-1-51/acsd-60326-graphql-query-error-customer-return-status">ACSD-60326: GraphQL query on customer Returns status gives an error:</a> The ACSD-60326 patch fixes the issue where an error occurs in the GraphQL query for customer Returns status. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.51 is installed.
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/patches-available-in-qpt/v1-1-52/acsd-59925-sorting-items-in-media-gallery">ACSD-59925: Sorting items in the Media Gallery by position in GraphQL:</a> The ACSD-59925 patch fixes the issue where items in the Media Gallery are not sorted by position, leading to an incorrect display order. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.52 is installed.
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/patches-available-in-qpt/v1-1-52/acsd-61322-products-not-assigned-to-shared-catalogue">ACSD-61322: Products not assigned to Shared Catalogue are included in XML Sitemap:</a> The ACSD-61322 patch fixes the issue where products/categories not assigned to the Shared Catalog for the Default (General) group are still included in the XML Sitemap. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.52 is installed.
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/patches-available-in-qpt/v1-1-52/acsd-60590-optimized-bestseller-report-generation">ACSD-60590: Enhancing performance of Bestsellers Aggregated Daily Report generation:</a> The ACSD-60590 patch fixes the issue where the Bestsellers Aggregated Daily Report takes a significant amount of time to generate for a large volume of placed orders. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.52 is installed.
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/patches-available-in-qpt/v1-1-52/acsd-59865-cart-price-rule-fix-for-insufficient-quantity-issue">ACSD-59865: Cart Price Rule fails to cancel previous rules due to insufficient product quantity:</a> The ACSD-59865 patch fixes the issue where the <em>Discount quantity step</em> value in <em>Fixed amount discount</em>, <em>Percent of product price discount</em>, and <em>Buy X get Y</em> Cart Price Rules no longer cancels the action of previous rules. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.52 is installed.
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>
  
  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/known-issues-patches-attached/error-when-filtering-orders-in-admin">Error when filtering orders in the Admin:</a> This article provides a patch for the Adobe Commerce issue where an error occurs when attempting to filter orders in the Admin by date, displaying the message: <em>Integrity constraint violation: 1052 Column 'created_at' where clause is ambiguous</em>.
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-25030">Adobe Commerce: Inline JavaScript Issues on checkout page in Content Security Policy (CSP) restricted mode:</a> This article provides detailed explanations and solutions for issues encountered with custom JavaScript added via Adobe Commerce Admin and Google Tag Manager in Adobe Commerce 2.4.7 during checkout when <strong>CSP restricted mode</strong> is enabled.
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/patches-available-in-qpt/v1-1-51/acsd-61195-empty-cart-on-final-graphql-page">ACSD-61195: Cart GraphQL request fails to return items on final page:</a> The ACSD-61195 patch fixes the issue where no cart items are returned on the last page for the cart GraphQL request. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.51 is installed.
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/patches-available-in-qpt/v1-1-50/acsd-59514-forms-in-admin-with-page-builder-throw-error-in-browser-console">ACSD-59514: Forms in Admin with Page Builder throw error in browser console:</a> The ACSD-59514 patch fixes the issue where the forms in Admin with Page Builder throw the error <em>Page Builder was rendering for 5 seconds without releasing locks</em> in the browser console after submitting the form, and changes can't be saved. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.50 is installed.
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/patches-available-in-qpt/v1-1-51/acsd-60538-if-product-is-disabled-attributes-dont-show">ACSD-60538: Attributes don't show correctly if product is disabled in <em>All Store Views</em>:</a> The ACSD-60538 patch fixes the issue where if a product is disabled in <em>All Store Views</em> and enabled only in specific store view scopes, the product attributes don't show correctly in the GraphQL response, leading to the product not being displayed properly. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.51 is installed.
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/patches-available-in-qpt/v1-1-50/acsd-58352-return-attribute-labels-for-the-default-store-are-returned-via-graphql-api">ACSD-58352: Return attribute labels for the default store are returned via GraphQL API:</a> The ACSD-58352 patch fixes the issue where return attribute labels for the default store are returned via GraphQL API when a non-default store view is specified in the request header. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.50 is installed.
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>
  
  <tr>
    <td>
    <a href = "https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-24983">The <em>Switch Accounts</em> dropdown is missing from your account:</a> This article provides a solution to the Adobe Commerce issue where the <em>Switch Accounts</em> dropdown is missing from your account, and you have lost access to submit tickets on behalf of the merchant.
    </td>
    <td>New article</td>
    <td>October 17, 2024</td>
  </tr>

  <tr>  
    <td>
    <a href = "https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/support-tools/patches/v1-1-49/acsd-56979-product-images-removed-after-staging-update-deleted">ACSD-56979: Product images removed after staging update deleted:</a> The ACSD-56979 patch fixes the issue where product images are removed after deleting a staging update. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.49 is installed.  
    </td>
    <td>New article</td>
    <td>October 17, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/support-tools/patches/v1-1-50/acsd-48210-store-view-specific-scope-attribute-overrides-global-values">ACSD-48210: Store view specific scope attributes override global values:</a> The ACSD-48210 patch fixes the issue where when updating a <em>Website Scope</em> attribute within a specific store view overrides the attribute values in the global scope. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.50 is installed. 
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/support-tools/patches/v1-1-50/acsd-59280-fix-for-reflection-union-type-error">ACSD-59280: ReflectionUnionType::getName() error in 2.4.4-pX installations:</a> The ACSD-59280 patch fixes the issue where the call to undefined method <code>ReflectionUnionType::getName()</code> error occurs during the installation of 2.4.4-pX versions. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.50 is installed. 
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/support-tools/patches/v1-1-50/acsd-54887-customer-shopping-cart-gets-cleared-after-session-expiry">ACSD-54887: Customer shopping cart gets cleared after customer session has expired:</a> The ACSD-54887 patch fixes the issue where the customer's shopping cart gets cleared after the customer session has expired with <em>Persistent Shopping Cart</em> enabled. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.50 is installed. 
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/support-tools/patches/v1-1-50/acsd-60303-admin-order-placement-fix">ACSD-60303: Admin order placement issue resolved with HTML minification enabled:</a> The ACSD-60303 patch fixes the issue where an order from Admin cannot be placed if HTML minification is enabled. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.50 is installed. 
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/support-tools/patches/v1-1-49/acsd-57045-url-rewrites-cause-infinite-page-looping-after-website-root-unchecked-hierarchy">ACSD-57045: URL rewrites cause infinite page looping after <em>Website Root</em> unchecked from Hierarchy:</a> The ACSD-57045 patch fixes the issue where URL rewrites cause infinite page looping after <em>Website Root</em> is unchecked from Hierarchy. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.49 is installed.
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/support-tools/patches/v1-1-49/ascd-58446-deleting-a-team-with-child-users-or-teams-via-graphql-gives-an-uninformative-error-message">ACSD-58446: Deleting a team with child users or teams via GraphQL gives an uninformative error message:</a> The ACSD-58446 patch fixes the Adobe Commerce issue where deleting a team with child users or teams via GraphQL returns an uninformative error message inconsistent with the UI. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.49 is installed. 
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/support-tools/patches/v1-1-49/acsd-58375-wrong-youtube-api-key-configuration-causes-an-error-when-adding-a-youtube-video-at-the-store-view-level">ACSD-58735: Incorrectly configured YouTube API key causes error when adding video at store view level:</a> The ACSD-58735 patch fixes the issue where where wrong YouTube API key configuration causes an error when adding a YouTube video at the store view level. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.49 is installed. 
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/support-tools/patches/v1-1-49/acsd-57086-orders-placed-from-non-default-websites-with-terms-conditions-processed-incorrectly">ACSD-57086: Orders from non-default websites with terms and conditions enabled are processed incorrectly:</a> The ACSD-57086 patch fixes the issue where orders placed from non-default websites with terms and conditions enabled are not processed correctly. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.49 is installed. 
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/support-tools/patches/v1-1-50/acsd-58141-phpsessid-regenerates-on-post-requests-for-logged-in-customers-with-l2-redis-cache-enabled">ACSD-58141: PHPSESSID regenerates on POST requests for logged-in customers if the L2 Redis cache is enabled:</a> The ACSD-58141 patch fixes the issue where PHPSESSID regenerates on POST requests for a logged-in customer if the L2 Redis cache is enabled, and the customer is updated from Admin. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.50 is installed. 
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/support-tools/patches/v1-1-50/acsd-58790-fixes-pinch-to-zoom-functionality-on-the-product-detail-page-images-in-mobile-view-on-chrome">ACSD-58790: Fixes pinch-to-zoom functionality on the product detail page images in mobile view on Chrome:</a> The ACSD-58790 patch fixes the Adobe Commerce issue where the image in mobile view on Chrome did not zoom in on the image as expected. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.50 is installed. 
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>

  <tr>
    <td>
    <a href="https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/support-tools/patches/v1-1-50/acsd-58442-fixes-issue-devices-768px-mobile-view-instead-desktop">ACSD-58442: Fixes the issue where devices with 768px width treated as mobile, causing menu and header to load in mobile view not desktop:</a> The ACSD-58442 patch fixes the Adobe Commerce issue where devices with a width of 768px are treated as mobile, causing the menu and header to load in a mobile view instead of a desktop. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.50 is installed.
    </td>
    <td>New article </td>
    <td>October 17, 2024</td>
  </tr>
</table>
