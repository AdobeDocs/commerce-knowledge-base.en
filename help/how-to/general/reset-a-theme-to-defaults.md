---
title: Reset a theme to defaults
description: Depending on issues you may be encountering when customizing your themes and developing your store, you may not have access through the Commerce Admin. You can clear and reset to your theme default without accessing the Admin. After you clear the theme, the default Luma theme will be applied.
exl-id: 86304dd5-f448-4dcc-ad07-04ecc6c85b6d
feature: Cache
---
# Reset a theme to defaults

Depending on issues you may be encountering when customizing your themes and developing your store, you may not have access through the Commerce Admin. You can clear and reset to your theme default without accessing the Admin. After you clear the theme, the default Luma theme will be applied.

While you’re developing Adobe Commerce (all deployments) and Magento Open Source components (modules, themes, and language packages), your rapidly changing environment requires you to periodically clear certain directories and caches. Otherwise, your code runs with exceptions and won’t function properly. For details, see [Clear directories during development](https://developer.adobe.com/commerce/php/development/components/clear-directories/) in our developer documentation.

## Environment and technologies

* Adobe Commerce on-premises
* Adobe Commerce on cloud infrastructure
* Magento Open Source

## Prerequisites

* Database tools

## Steps

If you need to reset the store theme, but cannot access the Admin panel, you can reset it in the database by doing the following:

1. Use a database tool such as [phpMyAdmin](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/prerequisites/optional-software#phpmyadmin) or access the DB manually from the command line to execute the following SQL query: `UPDATE core_config_data SET value=NULL WHERE path='design/theme/theme_id'`
1. Clear the following directories:
    * `pub/static/frontend`
    * `var/view_preprocessing`
    * `var/cache`
    * `var/page_cache`

This way there will be no theme set on the store view level, and when you reload the store front pages, the default Luma theme will be applied.

## Additional Information

* [Clear directories during development](https://developer.adobe.com/commerce/php/development/components/clear-directories/) in our developer documentation
