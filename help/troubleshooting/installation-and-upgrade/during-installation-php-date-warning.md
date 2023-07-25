---
title: During installation, PHP date warning
description: This article provides a fix for a PHP date warning during installation.
exl-id: f82c77a9-bbcd-4426-96a0-b3f4b704860b
feature: Install
---
# During installation, PHP date warning

This article provides a fix for a PHP date warning during installation.

## Details {#details}

During the installation, the following message displays:

```text
PHP Warning:  date(): It is not safe to rely on the system's timezone settings. [more]
```

### Solution {#solution}

Check the PHP time zone setting carefully. Refer to [Installation Guide > PHP Settings](https://devdocs.magento.com/guides/v2.3/install-gde/prereq/php-settings.html) in our developer documentation.
