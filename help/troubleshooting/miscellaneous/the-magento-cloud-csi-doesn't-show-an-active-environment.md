---
title: The Magento-cloud CLI doesn't show an active environment
description: This article describes a known Adobe Commerce issue where the Magento-cloud CLI doesn't show an active environment. 
feature:  Configuration
role: Developer
---

# The Magento-cloud CLI doesn't show an active environment

## Issue

There are several active environments and you are trying to interact with an environment by running a Magento-cloud CLI command `(For example: ssh, db:size, db:sql, etc.)`

However, the prompt to choose the desired environment doesn't list this environment, e.g., the integration environment:

Enter a number to choose an environment:
Default: master

```
  [0] integration2 (type: development)
  [1] master (type: development)
  [2] production
  [3] staging
 >
```

<u>Steps to reproduce:</u>

You have to manually specify the environment with the e|-environment flag.

1. Find the list of active environments and take note of the environment name:

```
    $ Magento-cloud environment:list |grep "Active\|ID"
    Your environments are:
    | ID                                                            | Title                                                                | Status   | Type        |
    | master                                                        | Master                                                               | Active   | development |
    |   production                                                  | Production                                                           | Active   | production  |
    |     staging                                                   | Staging                                                              | Active   | staging     |
    |       integration                                             | Integration                                                          | Active   | development |
    |       integration2                                            | Integration2                                                         | Active   | development |
```

1. Specify the environment's ID with your command:
Magento-cloud ssh -e integration

## Cause

The environment might not be available due to a deployment that is in progress, stuck, or one that had failed.

## Related reading

* [Manage message queues](https://devdocs.magento.com/guides/v2.4/config-guide/mq/manage-message-queues.html) in our developer documentation.
