#!/bin/bash
rm ../list.txt
rm ../result.txt
rm ../score.txt
rm ../inputlist*.txt
rm ../outputlist*.txt
rm -rf ../workingggg/*
#ls ../gradebook_2020092_CSE24101_Homework201_2020-09-22-09-17-22/*.zip | sed 's/.zip /.zip\n/g' > ../list.txt
ls ../student_zip/*.zip | sed 's/.zip /.zip\n/g' > ../list.txt
ls ../problem1/input*.txt | sed 's/.txt /.txt\n/g' > ../inputlist1.txt
ls ../problem1/output*.txt | sed 's/.txt /.txt\n/g' > ../outputlist1.txt
ls ../problem2/input*.txt | sed 's/.txt /.txt\n/g' > ../inputlist2.txt
ls ../problem2/output*.txt | sed 's/.txt /.txt\n/g' > ../outputlist2.txt
for i in {1..68}
do
    file="$(sed -n $i,${i}p ../list.txt)"
    cp "$file" ./
    echo $i "--------------------------------------------------"
    unzip -o "$(echo $file| cut -d '/' -f3)" >> ../result.txt 2>&1
    stID="$(basename -s ".zip"  $file)"
    stID="$(echo $stID| cut -d '_' -f2)"
    echo ""
    echo $i $stID
    echo $i $stID >> ../score.txt
    echo "\n" $stID " problem1 output---------------------\n" >> ../result.txt

    score1=0
    for j in {1..5}
    do
        input1="$(sed -n $j,${j}p ../inputlist1.txt)"
        cp "$input1" ./input_1.txt
        output1="$(sed -n $j,${j}p ../outputlist1.txt)"
        cp "$output1" ./output_answer.txt
        g++ "$(find ./ \( -iname "*1.cpp" ! -iname ".*" \))" -w || echo "problem1 compile fail" >> ../result.txt
        if [ -f "a.out" ]
        then
            ./a.out >> ../result.txt
            if diff -q output_1.txt output_answer.txt > /dev/null
            then
                #cat output_1.txt
                #echo "---------"
                #cat output_answer.txt
                #echo "---------"
                score1=$(($score1+20))
                echo " 1-"$j "20" >> ../score.txt
            else
                #cat output_1.txt
                #echo "---------"
                #cat output_answer.txt
                #echo "---------"
                echo $j ": output1 is wrong">> ../result.txt
                echo " 1-"$j "0" >> ../score.txt
            fi
            cp "$file" ../done_zip
        else
            cp "$file" ../compile_error
        fi
    done
    rm a.out >& /dev/null


    echo "\n" $stID "problem2 output----------------------\n" >> ../result.txt
    score2=0
    for j in {1..5}
    do
        input2="$(sed -n $j,${j}p ../inputlist2.txt)"
        cp "$input2" ./input_2.txt
        output2="$(sed -n $j,${j}p ../outputlist2.txt)"
        cp "$output2" ./output_answer.txt
        g++ "$(find ./ \( -iname "*2.cpp" ! -iname ".*" \))" -w || echo "problem2 compile fail" >> ../result.txt
        if [ -f "a.out" ]
        then
            ./a.out >> ../result.txt
            if diff -q output_2.txt output_answer.txt > /dev/null
            then
                score2=$(($score2+20))
                echo " 2-"$j "20" >> ../score.txt
            else
                echo $j ": output2 is wrong">> ../result.txt
                echo " 2-"$j "0" >> ../score.txt
            fi
            cp "$file" ../done_zip
        else
            cp "$file" ../compile_error
        fi
    done

    rm a.out >& /dev/null

    echo $i $stID "(problem1, problem2) = (" $score1 "," $score2 ") = " $(($score1+$score2))>> ../score.txt
    echo "" >> ../score.txt
    tail -n 2 ../score.txt
    rm -rf ../workingggg/*
done
