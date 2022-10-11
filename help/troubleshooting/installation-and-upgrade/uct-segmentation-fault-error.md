---
title: Troubleshoot upgrade compatibility tool errors
labels: troubleshooting,upgrade compatibility tool,uct,upgrade,adobe commerce
description: "This article explains errors you may experience while using the Upgrade Compatibility Tool and provides solutions to fix those errors so that you can successfully execute the tool."
---

# Troubleshoot upgrade compatibility tool errors

This article explains errors you may experience while using the Upgrade Compatibility Tool and provides solutions to fix those errors so that you can successfully execute the tool.

## Affected products and versions

* [Upgrade Compatibility Tool](https://experienceleague.adobe.com/docs/commerce-operations/upgrade-guide/upgrade-compatibility-tool/overview.html) is compatible with Adobe Commerce versions from 2.3.0 onwards.

## Segmentation fault error

<u>Cause</u>:

When two modules have the same name, the Upgrade Compatibility Tool shows a segmentation fault error.

<u>Solution</u>:

To avoid this error it is recommended to specify the path to the module as an argument:

```bash
bin/uct upgrade:check --current-version=2.4.4 path/to/the/module
```

>[!WARNING]
>
> The Upgrade Compatibility Tool may not be able to analyse the codebase if it contains circular dependency between methods.

## Empty output

<u>Steps to reproduce</u>:

1. If after running this command:

   ```bash
   bin/uct upgrade:check INSTALLATION_DIR -c M2_VERSION
   ```

1. The only output is `Upgrade compatibility tool`:

   ```terminal
   bin/uct upgrade:check /var/www/project/magento/ -c 2.4.1
   Upgrade compatibility tool
   ```

<u>Cause</u>:

The likely cause is a PHP memory limitation.

There are two possible solutions to avoid this PHP memory limitation.

<u>Solution 1</u>:

Override the memory limitation by setting `memory_limit` to `-1`:

```bash
php -d memory_limit=-1 /bin/uct upgrade:check INSTALLATION_DIR -c M2_VERSION
```

>[!NOTE]
>
> The `M2_VERSION` is the target Adobe Commerce version you want to compare to your Adobe Commerce instance.

<u>Solution 2</u>:

Adding the `-m` option allows the Upgrade Compatibility Tool to analyze each specific module independently to avoid encountering two modules with the same name in your Adobe Commerce instance.

This command option also allows the Upgrade Compatibility Tool to analyze a folder containing several modules:

```bash
bin/uct upgrade:check /<dir>/<instance-name> -m /vendor/<vendor-name>/
```

See the [Run the tool in a command-line interface](https://experienceleague.adobe.com/docs/commerce-operations/upgrade-guide/upgrade-compatibility-tool/use-upgrade-compatibility-tool/run.html) page for more information on command-line interface options. 
