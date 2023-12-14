---
title: "Changing search engine in app/etc/env.php"
description: This article provides a solution to the issue where you try to change the search engine in the admin but the fields are locked.
---

# Changing search engine in `app/etc/env.php`

This article provides a solution to the issue when you try to remove the search engine configuration from the `app/etc/env.php` file. However, when you redeployed the instance, it reverted to the previous setting, or was changed to opensearch by default.

## Affected products and versions

* Adobe Commerce on cloud infrastructure, [all supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf).


## Issue

You try to change the search engine in the Commerce Admin but the fields are locked.

## Cause

The search engine configuration is locked in the `app/etc/env.php` file or the search engine is explicitly defined in the `.magento.env.yaml` file.

## Solution

1. Check the `.magento.env.yaml` file under the deploy stage and see whether the `SEARCH_CONFIGURATION` variable has been configured, e.g.,:

      ```yaml
      SEARCH_CONFIGURATION:
        engine: elasticsearch7
        ...
      <VARIABLE X>
      ```

1. Is this variable present? No - the engine configuration is locked to Opensearch by default. To change the configuration, you must add the variable to the `.magento.env.yaml` file with the appropriate value for the search engine. Yes - if you wish to modify the engine, replace the existing value of engine in `.magento.env.yaml`. Possible/known values: opensearch, livesearch, elasticsuite, amasty_elastic, and amasty_elastic_opensearch.
1. Redeploy the instance.
1. The search engine field in the Commerce Admin will remain locked, but it should get updated with the value you have specified.

## Related reading

* [Locked fields in Commerce Admin](commerce-knowledge-base/troubleshooting/miscellaneous/locked-fields-in-magento-admin.html) in Commerce on Cloud Infrastructure Guide.
