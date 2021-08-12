#!/bin/zsh

sed -i '/cron:/d' .github/workflows/run.yml

if [[ $(date '+%H') == 01 ]];then
    time=$(($RANDOM%10))" 3 * * *"
elif [[ $(date '+%H') == 03 ]];then
    time=$(($RANDOM%10))" 5 * * *"
elif [[ $(date '+%H') == 05 ]];then
    time=$(($RANDOM%10))" 7 * * *"
elif [[ $(date '+%H') == 07 ]];then
    time=$(($RANDOM%10))" 9 * * *"
elif [[ $(date '+%H') == 09 ]];then
    time=$(($RANDOM%10))" 11 * * *"
elif [[ $(date '+%H') == 11 ]];then
    time=$(($RANDOM%5))" 13 * * *"
elif [[ $(date '+%H') == 13 ]];then
    time=$(($RANDOM%10))" 1 * * *"
else
    time=$(($RANDOM%10))" 1,3,5,7,9,11,13 * * *"
fi
echo 当前时间为$(date '+%H')时，计划运行时间$time
sed -i '/schedule/a\    - cron: '$time'' .github/workflows/run.yml

exit 0
