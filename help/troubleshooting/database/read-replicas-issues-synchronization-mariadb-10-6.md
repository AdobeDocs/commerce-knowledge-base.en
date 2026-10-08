---
title: Read Replicas issues on Adobe Commerce Cloud 2.4.6 with MariaDB 10.6
description: This article explains how to troubleshoot Read Replicas issues on Adobe Commerce Cloud 2.4.6 with MariaDB 10.6.
feature: Configuration
role: Developer,Admin
exl-id: b7af1cc3-93ff-40c5-8959-076cedddb56d
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: dac87252-6066-4d6e-a9d2-f6d84c323de7
    internal-label: Configuration
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
---
# Read Replicas issues on Adobe Commerce Cloud 2.4.6 with MariaDB 10.6

This article provides solutions for unexpected behavior when using Read Replicas on Adobe Commerce Cloud 2.4.6 with MariaDB 10.6+. 

## Affected products and versions

* MariaDB 10.6+
* Adobe Commerce on cloud infrastructure 2.4.6

## Issue

Non-critical reads are showing incorrect information. 

## Cause

The `slave_parallel_mode` config on the database was changed by default to *optimistics* when the value should be *conservative*, and the `synchronous_replication` value in Ece-Tools is defaulting to *true* when the value should be *false*.

## Solution

1. Check that the `slave_parallel_mode` parameter is set to *conservative* (you will need to [raise a support ticket](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide.html?lang=en#submit-ticket) if the value is  not showing as *conservative*). To check, run the following command:

    ```
     MariaDB [main]> show variables like 'slave_parallel_mode';
     +---------------------+--------------+
     | Variable_name       | Value        |
     +---------------------+--------------+
     | slave_parallel_mode | conservative |
     +---------------------+--------------+
     1 row in set (0.001 sec)
    ```

1. Update `.magento.env.yaml` database configurations to:

    ```yaml
        DATABASE_CONFIGURATION:
         _merge: true
            slave_connection:
                default:
                    synchronous_replication: false
    ```



For steps on updating the database configuration, refer to [DATABASE_CONFIGURATION](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure/env/stage/variables-deploy.html#database_configuration) in the Deploy variables topic in the Commerce on Cloud Infrastructure Guide. 


## Related reading

* [Configure environment variables for deployment](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure/env/configure-env-yaml.html) in the Commerce on Cloud Infrastructure Guide.
* [Best practices for database configuration](https://experienceleague.adobe.com/docs/commerce-operations/implementation-playbook/best-practices/planning/database-on-cloud.html) in the Implementation Playbook.
