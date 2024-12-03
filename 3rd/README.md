*Part 1*
Used this command to generate a parsed file:

grep -o -E "mul\([0-9]{1,3},[0-9]{1,3}\)" input | grep -o -E "[0-9]{1,3},[0-9]{1,3}" > parsed

*Part 2*

grep -v -E "don't()*do()" input | grep -o -E "mul\([0-9]{1,3},[0-9]{1,3}\)" | grep -o -E "[0-9]{1,3},[0-9]{1,3}" > parsed2
grep -E -v "don't\(\)(.*?)do\(\)" input

