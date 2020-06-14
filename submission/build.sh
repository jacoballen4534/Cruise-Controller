RUN_FILE="CruiseControllerCombined"
TARGET_ESTEREL_FILE=$RUN_FILE.strl
TARGET_C_FILE="$RUN_FILE"_data.c
TARGET_FOLDER="Build"

# Purge old build
rm -rf Build

cp -R CruiseController/. $TARGET_FOLDER/
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

echo -e "\n\nBuild File Setup Complete\n"
make $RUN_FILE.xes
./$RUN_FILE.xes
