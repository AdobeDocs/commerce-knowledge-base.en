---
title: 'PWA Studio: Venia GraphQL queries to Adobe Commerce produce validation errors'
description: This article provides recommendations on how to solve the issue where Venia storefront GraphQL queries to Adobe Commerce instance produce validation errors.
exl-id: ba268945-2a10-4af5-8089-cde21f0687bd
feature: GraphQL
role: Developer
---
# PWA Studio: Venia GraphQL queries to Adobe Commerce produce validation errors

This article provides recommendations on how to solve the issue where Venia storefront GraphQL queries to Adobe Commerce instance produce validation errors.

## Affected products and versions

* Adobe Commerce on-premises 2.2.x, 2.3.x
* Adobe Commerce on cloud infrastructure 2.2.x, 2.3.x
* PWA Studio project for Adobe Commerce

## Issue

Venia GraphQL queries to Adobe Commerce on-premises or Adobe Commerce on cloud infrastructure produce validation errors.

## Cause

One of the reasons causing the problem, might be Venia and its GraphQL queries being out of sync with the schema of the connected Adobe Commerce instance.

## Solution

To test whether your queries are up to date, run the following command in the project root:

```bash
yarn run validate-queries
```

This will show a compatibility report. If you have incompatibilities, you need to upgrade your PWA Studio or Adobe Commerce instance. Check the [Adobe Commerce compatibility matrix](https://developer.adobe.com/commerce/pwa-studio/integrations/adobe-commerce/version-compatibility/) to see what exactly versions you need.

Reference the following documentation for instructions on how to upgrade:

* For PWA Studio upgrades, search for the "Upgrading from a previous version" section of the [PWA release notes](https://github.com/magento/pwa-studio/releases/) for the version that you need to upgrade to.
* [Upgrade Adobe Commerce on cloud infrastructure version](https://devdocs.magento.com/cloud/project/project-upgrade.html) in our developer documentation
* [Upgrade Adobe Commerce on-premises (installed using "composer create-project" or archive)](https://devdocs.magento.com/guides/v2.3/comp-mgr/cli/cli-upgrade.html) in our developer documentation
* [Upgrade Adobe Commerce on-premises (installed by cloning Adobe Commerce repo)](https://devdocs.magento.com/guides/v2.3/install-gde/install/cli/dev_update-magento.html) in our developer documentation

## Related reading

* [PWA Studio: Webpack hangs before beginning compilation](/help/troubleshooting/miscellaneous/pwa-studio-webpack-hangs-before-beginning-compilation.md) in our support knowledge base
* [PWA Studio: Validation errors when running developer mode](/help/troubleshooting/miscellaneous/pwa-studio-validation-errors-when-running-developer-mode.md) in our support knowledge base
* [PWA Studio: Browser displays “Cannot proxy to“ error](/help/troubleshooting/miscellaneous/pwa-studio-browser-displays-cannot-proxy-to-error.md) in our support knowledge base
* [Configure NPM to be able to use PWA Studio](/help/how-to/general/configure-npm-to-be-able-to-use-pwa-studio.md) in our support knowledge base
* [PWA for Adobe Commerce Documentation](https://magento.github.io/pwa-studio/)
