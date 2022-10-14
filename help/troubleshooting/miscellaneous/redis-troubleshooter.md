---
title: Redis troubleshooter on Adobe Commerce
labels: Magento Commerce,Magento Commerce Cloud,Redis,cache,caching,database,ece-tools,patches,troubleshooting,Adobe Commerce,cloud infrastructure,on-premises
description: "This article is a troubleshooter tool for Adobe Commerce on-premises and Adobe Commerce on cloud infrastructure merchants having issues with Redis. Click on each question to reveal the answer in each step of the troubleshooter. Depending on your symptoms and configuration, the troubleshooter will explain how to troubleshoot version and memory issues and optimize performance."
---

# Redis troubleshooter on Adobe Commerce

This article is a troubleshooter tool for Adobe Commerce on-premises and Adobe Commerce on cloud infrastructure merchants having issues with Redis. Click on each question to reveal the answer in each step of the troubleshooter. Depending on your symptoms, the troubleshooter will explain how you can troubleshoot version and memory issues, and optimize performance.

## Step 1 {#step}

+++Redis issue?

a. YES – Proceed to [Step 2](#step2)</a>.

b. NO – Return to [support.magento.com](https://support.magento.com/hc/en-us) and search for relevant troubleshooting articles.

+++

## Step 2 {#step2}

+++Current Redis patches installed?

a. YES – Proceed to [Step 3](#step3)</a>.

b. NO – Make sure you have the latest version of the package `magento-cloud-patches` installed. This package has the necessary patches for Redis. To access go to [GitHub magneto-cloud-patches](https://github.com/magento/magento-cloud-patches/).

+++

## Step 3 {#step3}

+++On Redis versions 3.2 or 5.0? 

Check by running the following commands in the CLI. Pro or Staging: `$ redis-cli -p %port-number% info | grep redis_version`, where `%port-number%` is the number of the port, which can be found in the `app/etc/env.php` file or by running one of these commands: `$ vendor/bin/ece-tools env:config:show | grep -i redis -A 3` or `$ cat app/etc/env.php | grep redis -A 3` Starter or Integration: `$ redis-cli -h 'redis.internal' info | grep redis_version`

a. YES – Proceed to [Step 4](#step4).

b. NO – Adobe Commerce supports Redis versions 3.2 and 5.0. If you are running Adobe Commerce on cloud infrastructure 2.3.3 or higher, we recommend upgrading to Redis 5. For setup steps on Adobe Commerce on cloud infrastructure Pro plan architecture, Integration and Starter environments including the master branch, refer to [Adobe Commerce on cloud infrastructure > Set up Redis service](https://devdocs.magento.com/cloud/project/services-redis.html)</a> in our developer documentation. **You must [submit a support ticket](https://support.magento.com/hc/en-us/articles/360019088251) to change the service configuration on Pro architecture Production and Staging environments. Also, for Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.3.5+, extended Redis cache implementation is recommended. This type of Redis cache implementation provides enhancements that minimize the number of queries to Redis that are performed on each Adobe Commerce request. For steps, refer to [Extended Redis cache implementation Adobe Commerce 2.3.5+](https://support.magento.com/hc/en-us/articles/360049292532) in our support knowledge base. For all other Adobe Commerce users, refer to [Adobe Commerce Configuration Guide > Configure Redis](https://devdocs.magento.com/guides/v2.4/config-guide/redis/config-redis.html) in our developer documentation, for steps.

+++

## Step 4 {#step4}

+++Do you have the latest version of [ECE Tools > v2002.1.1](https://github.com/magento/ece-tools/releases)?

Check what version you have by running the command in the CLI/Terminal: `$php vendor/bin/composer info magento/ece-tools`.

a. YES - Proceed to [Step 5](#step5).

b. NO – [Upgrade ECE-Tools](https://devdocs.magento.com/cloud/project/ece-tools-update.html) to the latest release.

+++

## Step 5 {#step5}

+++Is there a lot of network traffic between the app and Redis?

a. YES – Try the following: For a non-split architecture, make sure a [secondary connection](https://support.magento.com/hc/en-us/articles/360037391972) is used. For split architecture, the [L2 cache must be enabled](https://devdocs.magento.com/guides/v2.4/config-guide/cache/two-level-cache.html).

b. NO – Configure L2 cache configuration by [Updating Redis Backend](https://devdocs.magento.com/cloud/env/variables-deploy.html#redis_backend). Proceed to [Step 6](#step6).

+++

## Step 6 {#step6}

+++Is the site still working slowly, after enabling L2 cache?

a. YES - Check the temp directory `/dev/shm` to see if you need to increase space. If you need more space, [submit a support ticket](https://support.magento.com/hc/en-us/articles/360019088251).
b. NO – Enabling L2 cache appears to have solved your Redis issues.

+++

[Back to step 1](#step1)
 

