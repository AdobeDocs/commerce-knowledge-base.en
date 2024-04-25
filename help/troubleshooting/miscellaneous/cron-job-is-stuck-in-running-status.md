---
title: "[!DNL Cron] job is stuck in **running** status"
description: This article provides solutions for when Adobe Commerce [!DNL cron] jobs do not finish executing and persist in a "running" status, which prevents other [!DNL cron] jobs from running. This can happen for a number of reasons, such as network issues, application crashes, re-deployment issues.
exl-id: 11e01a2b-2fcf-48c2-871c-08f29cd76250
feature: Configuration
role: Developer
---
# [!DNL Cron] job is stuck in "running" status

This article provides solutions for when Adobe Commerce [!DNL cron] jobs do not finish executing and persist in a "running" status, which prevents other [!DNL cron] jobs from running. This can happen for a number of reasons, such as network issues, application crashes, re-deployment issues.

## Affected products and versions

Adobe Commerce on cloud infrastructure, all versions

## Symptom {#symptom}

Symptoms of [!DNL cron] jobs that must be reset include:

* Large quantity of jobs appear in the `cron_schedule` queue
* Site performance starts to degrade
* Jobs fail to execute on schedule

## Solutions {#solutions}

### Solution for stopping all [!DNL cron] jobs at once {#solution-stop-all-crons-at-once}

>[!WARNING]
>
>Running this command without the `--job-code` option resets *all* [!DNL cron] jobs, including those currently running, so we recommend using it only in exceptional cases, such as after you have verified that all [!DNL cron] jobs must be reset. Re-deployment runs this command by default to reset [!DNL cron] jobs, so they recover appropriately after the environment is back up. Avoid using this solution when indexers are running.

To resolve this issue, you must reset the [!DNL cron] job(s) using the `cron:unlock` command. This command changes the status of the [!DNL cron] job in the database, ending the job forcefully to allow other scheduled jobs to continue.

1. Open a terminal and use your [SSH keys](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/secure-connections) to connect to the affected environment.
1. Get the MySQL database credentials:    ```shell    echo $MAGENTO_CLOUD_RELATIONSHIPS | base64 -d | json_pp    ```
1. Connect to the database using `mysql` :    ```shell    mysql -hdatabase.internal -uuser -ppassword main    ```
1. Select the `main` database:    ```shell    use main    ```
1. Find all running [!DNL cron] jobs:    ```shell    SELECT * FROM cron_schedule WHERE status = 'running';    ```
1. Copy the `job_code` of any job running longer than usual.
1. Use the schedule IDs from the previous step to unlock specific [!DNL cron] jobs:    ```shell    ./vendor/bin/ece-tools cron:unlock --job-code=<job_code_1> [... --job-code=<job_code_x>]    ```

### Solution for stopping a single [!DNL cron] {#solution-stop-a-single-cron}

1. Open a terminal and use your [SSH keys](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/secure-connections) to connect to the affected environment.
1. Check long running tasks by using the following command:

    ```date; ps aux | grep '[%]CPU\|cron\|magento\|queue' | grep -v 'grep\|cron -f'```

1. In the output, like in the sample output below, you'll see current date and list of processes. The `START` column shows starting time or date of the process:

    ```
    Wed May  8 22:41:31 UTC 2019
    USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
    root       590  0.0  0.0  27528  2768 ?        Ss   Jan15   0:49 /usr/sbin/cron -f
    bxc2qly+ 25855  0.0  0.0  23724  2184 ?        S    20:51   0:00 logger -d -u /run/bxc2qlykqhbqe_stg-cron.sock -p cron.info -s -t cron-bxc2qlykqhbqe_stg-bxc2qlykqhbqe_stg
    bxc2qly+ 25860 57.7  1.3 584220 222692 ?       S    20:51   0:02 php bin/magento cron:run
    bxc2qly+ 25863  0.0  0.0  23724  2472 ?        S    20:51   0:00 logger -d -u /run/bxc2qlykqhbqe-cron.sock -p cron.info -s -t cron-bxc2qlykqhbqe-bxc2qlykqhbqe
    bxc2qly+ 25876 53.0  0.6 475472 111468 ?       R    20:51   0:01 /usr/bin/php7.1-zts /app/bxc2qlykqhbqe_stg/bin/magento cron:run --group=index --bootstrap=standaloneProcessStarted=1
    bxc2qly+ 25878 57.0  0.6 475472 112080 ?       R    20:51   0:01 /usr/bin/php7.1-zts /app/bxc2qlykqhbqe_stg/bin/magento cron:run --group=staging --bootstrap=standaloneProcessStarted=1
    bxc2qly+ 25880 50.5  0.6 475472 111312 ?       R    20:51   0:01 /usr/bin/php7.1-zts /app/bxc2qlykqhbqe_stg/bin/magento cron:run --group=catalog_event --bootstrap=standaloneProcessStarted=1
    bxc2qly+ 25882 48.5  0.6 475472 111220 ?       R    20:51   0:00 /usr/bin/php7.1-zts /app/bxc2qlykqhbqe_stg/bin/magento cron:run --group=consumers --bootstrap=standaloneProcessStarted=1
    bxc2qly+ 25884 50.5  0.6 475472 111372 ?       R    20:51   0:01 /usr/bin/php7.1-zts /app/bxc2qlykqhbqe_stg/bin/magento cron:run --group=ddg_automation --bootstrap=standaloneProcessStarted=1
    bxc2qly+ 25890 32.5  0.6 475368 110672 ?       R    20:51   0:00 /usr/bin/php7.1-zts /app/bxc2qlykqhbqe/bin/magento cron:run --group=staging --bootstrap=standaloneProcessStarted=1
    bxc2qly+ 25892 34.5  0.6 475472 110724 ?       R    20:51   0:00 /usr/bin/php7.1-zts /app/bxc2qlykqhbqe/bin/magento cron:run --group=catalog_event --bootstrap=standaloneProcessStarted=1
    bxc2qly+ 25894 31.5  0.6 475368 110136 ?       R    20:51   0:00 /usr/bin/php7.1-zts /app/bxc2qlykqhbqe/bin/magento cron:run --group=consumers --bootstrap=standaloneProcessStarted=1
    bxc2qly+ 25896 29.0  0.6 475320 109876 ?       R    20:51   0:00 /usr/bin/php7.1-zts /app/bxc2qlykqhbqe/bin/magento cron:run --group=ddg_automation --bootstrap=standaloneProcessStarted=1
    ```

1. If you see a long running [!DNL cron] jobs which may the block deployment process, you can terminate the process using the `kill` command. You can identify the **Process ID** (found the `PID` column), and then put that `PID` in the command to kill the process.
The **kill process** command is:

    ```kill -9 <PID>```

1. Then you can re-deploy, if you were trying to re-deploy.
