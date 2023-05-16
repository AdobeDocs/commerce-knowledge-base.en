---
title: Cannot save *contact* as URL key
description: This article provides a workaround for the issue when you are not able to save *contact* as a URL key (e.g., "/contact") for products or CMS pages. When you try to save the URL key, you receive an error that indicates that the URL key is a duplicate URL.
---
# Cannot save "contact" as URL key

This article provides a workaround for the issue when you are not able to save *contact* as a URL key (e.g., "/contact") for products or CMS pages.

## Affected products and versions

Adobe Commerce (all deployment methods) 2.4.x

## Issue

You cannot save a prodiuct or a CMS page with the term *contact* in the URL key. When you try to save the URL key, you receive an error that indicates that the URL key is a duplicate URL.

<u>Steps to reproduce</u>:

Create a CMS page with URL key as *contact*.

<u>Expected result</u>:

The page is saved with *contact* in the URL key.

<u>Actual result</u>:

You cannot save the page. You get the error: *The value specified in the URL Key field would generate a URL that already exists.*

## Cause

*Contact* is a reserved word defined in `vendor/magento/module-contact/view/frontend/layout/contact_index_index.xml`.

```xml

<router id="standard">
      <route id="contact" frontName="contact">
          <module name="Magento_Contact" />
      </route>
  </router>
```

## Solution

You cannot use the term *contact* in your URL key, however you can use the term *contact* combined with another letter or number (For example, *contact1* and *contact2*). Although the term does not have to be *contact+&lt;another number or letter&gt;*, the term could be any string as long as the length does not exceed 255 characters.

Perform the following steps:

1. Log in to the Commerce Admin.
1. Go to **[!UICONTROL Marketing]** > **[!UICONTROL SEO & Search]** > **[!UICONTROL URL Rewrites]**.
1. Click **[!UICONTROL Add URL Rewrite]**.
1. Select *[!UICONTROL Custom]* on the [!UICONTROL Create URL Rewrite] drop down.
    1. In the [!UICONTROL Request Path] type "contact". Note the [!UICONTROL Request Path] is what a user enters in the browser and the [!UICONTROL Target Path] is where it should redirect to.
    1. Type in the [!UICONTROL Target Path] the new URL key (For example, "contact1").
    1. Select *[!UICONTROL No]* in the [!UICONTROL Redirect] drop down.

## Related reading

* [URL Rewrites](https://docs.magento.com/user-guide/marketing/url-rewrite.html) in our user guide.
* [SEO Best Practices](https://docs.magento.com/user-guide/marketing/seo-best-practices.html) in our user guide.
