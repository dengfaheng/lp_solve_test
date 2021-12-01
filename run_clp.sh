dir=new_MPS_Files

for file in $dir/*; do
    python cylp/clp_test.py $file
done
