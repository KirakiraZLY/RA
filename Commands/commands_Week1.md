# Commands during RA
## Week 1
2023/11/15   

### Data
```python
dir="/home/lezh/dsmwpred/zly"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
${dir}/data_qc
```  

### High-LD Regions
```python
dir="/home/lezh/dsmwpred/zly"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
echo "Region25 21  14600000 14700000" | cat ${dir}/RA/highld.txt - > ${dir}/RA/highld.fake
${dir_LDAK} --cut-genes ${dir}/RA/highld --bfile ${dir}/data_qc --genefile ${dir}/RA/highld.fake
```  