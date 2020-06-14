RUN_FILE="cruise"
TARGET_ESTEREL_FILE=$RUN_FILE.strl
TARGET_C_FILE="$RUN_FILE"_data.c
TARGET_FOLDER="Build_For_Tests"

# Purge old build
rm -rf $TARGET_FOLDER

cp -R CruiseController/. $TARGET_FOLDER/

# Move auto tester and expected input outputs
cp -R Test/. $TARGET_FOLDER/

cd $TARGET_FOLDER

shopt -s nullglob #Dont enter if no files were found

# Copy then delete each strl files into RUN_FILE..
for EsterelFile in *.strl; do
    if [ $EsterelFile != $TARGET_ESTEREL_FILE ]; then
        echo "Moving $EsterelFile --> $TARGET_ESTEREL_FILE"
        echo "" >> $TARGET_ESTEREL_FILE
        cat $EsterelFile >> $TARGET_ESTEREL_FILE
        rm -f $EsterelFile
    fi
done
echo ""

# Move the delete all C files into 1
for CFile in *.c; do
    if [ $CFile != $TARGET_C_FILE ] && [ $CFile != 'ctype.c' ]; then
        echo "Moving $CFile --> $TARGET_C_FILE"
        echo "" >> $TARGET_C_FILE
        cat $CFile >> $TARGET_C_FILE
        rm -f $CFile
    fi
done

# ensure a .h is present
touch $RUN_FILE.h

echo -e "\n\nTest File Setup Complete\n"

# Dont want to delete created .o files
make clean

# Manualy build for comand line mode.
/opt/esterelv6_01/bin/esterel -simul $TARGET_ESTEREL_FILE
gcc -m32 -c $RUN_FILE.c $TARGET_C_FILE
gcc -m32 -o $RUN_FILE $RUN_FILE.o "$RUN_FILE"_data.o /opt/esterelv6_01/lib/libcsimul.a

echo -e "\n\nManual Build Complete\n"

echo -e "Starting tests\n"
python3 autoTest.py

# Clean up
cd ../
rm -rf $TARGET_FOLDER