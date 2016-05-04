
params=(.1 .5 .9)
for alpha in ${params[*]}
do
  for gamma in ${params[*]}
  do
    for lambda in ${params[*]}
    do
      fileName="saves/run-$alpha-$gamma-$lambda-.006.dat"
      python Main.py $fileName $alpha $gamma $lambda .006
    done
  done
done

enotify "All parameters tested" "SARSA complete"
