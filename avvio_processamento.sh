#!/bin/bash
x="Not Nifi"
while getopts x: flag
do
    case "${flag}" in
        x) x=${OPTARG}
            ;;
    esac
done

if [[ $x == "Not Nifi" || $x == "Not" ]]
then
    echo "Run without Nifi";
    docker exec -it flink /bin/bash ../flinks-app/start_run.sh
elif [[ $x == "Nifi" ]]
then
    echo "Run with Nifi";
    docker exec -it flink /bin/bash ../flinks-app/NifiComputation/start_run.sh
else
    echo "Valore non valido";
fi

