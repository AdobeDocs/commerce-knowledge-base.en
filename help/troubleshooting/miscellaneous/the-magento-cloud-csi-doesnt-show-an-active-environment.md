---
<<<<<<< HEAD
title: The Magento-cloud CLI doesn't show an active environment
description: This article describes a known Adobe Commerce issue where the `Magento-cloud` CLI (command-line tool) doesn't show an active environment. 
feature:  Configuration
=======
title: The `magento-cloud` [!DNL CLI] doesn't show an active environment
description: This article describes a known Adobe Commerce issue where the Magento-cloud CLI (command-line tool) doesn't show an active environment. 
feature:  Cloud, Integration, Configuration
>>>>>>> 8c575c629cf26382fab7bd3d31ffc6055016ae52
role: Developer
---

# The `magento-cloud` CLI doesn't show an active environment

## Issue

<<<<<<< HEAD
There are several active environments and you are trying to interact with an environment by running a Magento-cloud CLI (command-line tool) command. `(For example: ssh, db:size, db:sql, etc.)`
=======
When there are several active environments and if someone is trying to interact with an environment by running a `magento-cloud` CLI command (for example: `ssh`, `db:size`, `db:sql`, etc.), the prompt to choose the desired environment doesn't list the required environment. (for example: the integration environment).
>>>>>>> 8c575c629cf26382fab7bd3d31ffc6055016ae52

However, the prompt to choose the desired environment doesn't list this environment. (For example: the integration environment)

```
Enter a number to choose an environment:
Default: master
  [0] integration2 (type: development)
  [1] master (type: development)
  [2] production
  [3] staging
 >
```

<<<<<<< HEAD
## Cause

The environment might not be available due to a deployment that is in progress, stuck, or one that had failed.

<u>Steps to reproduce:</u>
=======
## Solution
>>>>>>> 8c575c629cf26382fab7bd3d31ffc6055016ae52

It is necessary to specify the environment manually with the `-e|--environment` flag.

1. Find the list of active environments and take note of the environment's name:

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
`magento-cloud ssh -e integration`

<<<<<<< HEAD
=======
## Cause

The environment may be unavailable due to an ongoing, stalled, or failed deployment.
>>>>>>> 8c575c629cf26382fab7bd3d31ffc6055016ae52

## Related reading

* [Manage message queues](https://devdocs.magento.com/guides/v2.4/config-guide/mq/manage-message-queues.html) in our developer documentation.
