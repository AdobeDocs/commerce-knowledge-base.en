---
title: Cannot save shipping as a URL key
description: This article provides a workaround for the issue when you are not able to save shipping as a URL key (_e.g., /shipping_) for products or CMS pages. When you try to save the URL key, you receive an error that indicates that the URL key is a duplicate a URL.
exl-id: df19b597-f615-4b19-82c1-59cc179fa720
feature: Marketing Tools, Shipping/Delivery, Storefront
role: Admin
---
# Cannot save _shipping_ as a URL key

This article provides a workaround for the issue when you are not able to save shipping as a URL key (_e.g., /shipping_) for products or CMS pages. When you try to save the URL key, you receive an error that indicates that the URL key is a duplicate URL.

## Affected products and versions

Adobe Commerce (all deployment methods) 2.4.x

## Issue

You cannot save a CMS page with the term _shipping_ in the URL key.

<u>Steps to reproduce</u>:

Create a **[!UICONTROL CMS page]** with the URL key as _shipping_.

<u>Expected result</u>:

The page saves with _shipping_ as the URL key.

<u>Actual result</u>:

You are not able to save as this error occurs:
*The value specified in the URL Key field would generate a URL that already exists.*

## Cause

Shipping is a reserved word defined in `vendor/magento/module-shipping/etc/frontend/routes.xml`.

```xml

<router id="standard">
      <route id="shipping" frontName="shipping">
          <module name="Magento_Shipping" />
      </route>
  </router>
```

## Solution

You cannot use the term _shipping_ in your URL key - however you can use the term _shipping_ combined with another letter or number (_For example, shipping1 and shipping2_). 

Although the term does not have to be _shipping_+&lt;another number or letter&gt; - the term could be any string as long as the length does not exceed *255* characters.

## Perform the following steps:

1. Log in to the Adobe Commerce Admin.
1. Go to **[!UICONTROL Marketing]** > **[!UICONTROL SEO & Search]** > **[!UICONTROL URL Rewrites]**.
1. Click **[!UICONTROL Add URL Rewrite]**.
1. Select **[!UICONTROL Custom]** on the  **[!UICONTROL Create URL Rewrite]** drop down.
    1. Type the Request Path as  **[!UICONTROL shipping]**. 
    1. In the **[!UICONTROL Target Path]**, type the new URL key. (_For example, "shipping1"_).
    1. Select  **[!UICONTROL No]** in the Redirect drop down.


       (**Note**: _The Request Path is what a user enters in the browser and the Target Path is where it should redirect to._)

In addition, avoid using these keywords that are labelled as *reserved* keywords which cause the same exception to appear. Using any of these keywords listed below as a URL key value will cause the same error to appear.


   ```
   "admin"
   "adminAnalytics"
   "analytics"
   "api"
   "backup"
   "bulk"
   "captcha"
   "catalog"
   "catalogsearch"
   "checkout"
   "cms"
   "contact"
   "cookie"
   "customer"
   "directory"
   "downloadable"
   "giftmessage"
   "groupedProduct"
   "indexer"
   "instantpurchase"
   "loginascustomer"
   "marketplace"
   "mui"
   "multishipping"
   "newsletter"
   "oauth"
   "paypal"
   "persistent"
   "productalert"
   "releaseNotification"
   "reports"
   "review"
   "robots"
   "rss"
   "sales"
   "search"
   "security"
   "sendfriend"
   "shipping"
   "stores"
   "swagger"
   "swatches"
   "tax"
   "theme"
   "translation"
   "vault"
   "wishlist"
   ```

## Related reading

* [URL Rewrites](https://docs.magento.com/user-guide/marketing/url-rewrite.html) in our user guide.
* [SEO Best Practices](https://docs.magento.com/user-guide/marketing/seo-best-practices.html) in our user guide.
