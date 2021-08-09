#!/bin/zsh

sed -i '/cron:/d' .github/workflows/run.yml

if [[ $(date '+%H') == 0 ]];then
    time=$(($RANDOM%60))" 2 * * *"
elif [[ $(date '+%H') == 2 ]];then
    time=$(($RANDOM%60))" 5 * * *"
elif [[ $(date '+%H') == 5 ]];then
    time=$(($RANDOM%60))" 7 * * *"
elif [[ $(date '+%H') == 7 ]];then
    time=$(($RANDOM%60))" 9 * * *"
elif [[ $(date '+%H') == 9 ]];then
    time=$(($RANDOM%60))" 11 * * *"
elif [[ $(date '+%H') == 11 ]];then
    time=$(($RANDOM%5))" 13 * * *"
elif [[ $(date '+%H') == 13 ]];then
    time=$(($RANDOM%60))" 0 * * *"
else
    time=$(($RANDOM%30))" 0,2,5,7,9,11,13 * * *"
fi
echo 当前时间为$(date '+%H')时，计划运行时间$time
sed -i '/schedule/a\    - cron: '$time'' .github/workflows/run.yml

exit 0
