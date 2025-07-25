---
title: Cannot change search engine in `app/etc/env.php`
description: This article provides a solution to the issue where you try to change the search engine in the Commerce Admin, but the fields are locked.
exl-id: 61006ce7-34f9-4e4d-a197-f3d627dd277f
---
# Cannot change search engine in `app/etc/env.php`

This article provides a solution to the issue where you try to remove the search engine configuration from the `app/etc/env.php` file, but after redeployment, the configuration reverts to the previous setting or is changed to [!DNL OpenSearch] by default.

## Affected products and versions

* Adobe Commerce on cloud infrastructure, [all supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf)

## Issue

You try to change the search engine in the Commerce Admin, but the fields are locked.

## Cause

The search engine configuration is locked in the `app/etc/env.php` file, or the search engine is explicitly defined in the `.magento.env.yaml` file.

## Solution

1. Check the `.magento.env.yaml` file under the deploy stage and see whether the `SEARCH_CONFIGURATION` variable has been configured. Example:

      ```yaml
      SEARCH_CONFIGURATION:
        engine: elasticsearch7
        ...
      <VARIABLE X>
      ```

1. Is the  `SEARCH_CONFIGURATION` variable present? If not present, the search engine configuration is locked to [!DNL OpenSearch] by default. To change the configuration, you must add the variable to the `.magento.env.yaml` file with the appropriate value for the search engine. If the `SEARCH_CONFIGURATION` variable is present and you wish to modify the engine, replace the existing value for the engine in `.magento.env.yaml`. Possible/known values: [!DNL opensearch], [!DNL livesearch], [!DNL elasticsuite], [!DNL amasty_elastic], and [!DNL amasty_elastic_opensearch].
1. Redeploy the instance.
1. The search engine field in the Admin will remain locked, but it should get updated with the value you have specified.

## Related reading

* [Locked (grayed out) fields in Commerce Admin](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26879) in Commerce on Cloud Infrastructure Guide.
