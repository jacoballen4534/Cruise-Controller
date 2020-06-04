TARGET_FILE="PedalControl.strl"
RUN_FILE="PedalControl"

cp -R CruiseController/. Build/
cd Build
echo "" >> $TARGET_FILE
cat AccelPedal.strl >> $TARGET_FILE
echo "" >> $TARGET_FILE
cat BrakePedal.strl >> $TARGET_FILE
echo "" >> $TARGET_FILE

make $RUN_FILE.xes
./$RUN_FILE.xes
