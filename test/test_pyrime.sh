# A simple shell script to test the PyRIME routine

#echo "The output should be:"
#echo "4779 2  0.5911760 15.166 15.164 16.472 16.468 16.469 16.465 15.579 15.577 15.574 15.572  0.698841  0.066634 -0.019603 -0.059386 0.0323 0.0544 0.000504  108  108"
#echo " , while the 4779_2.pdf should look the same as the included 4779_2_comp.pdf"

echo "The output should be:
9 -1.415 OoII
10 -1.094 OoI
16 -1.016 OoI
25 -0.898 OoI
27 -0.955 OoI
30 -1.041 OoI
43 -1.032 OoII
46 -1.025 OoI
47 -1.083 OoI
49 -1.269 OoII
50 -0.981 OoI
54 -1.312 OoI
56 -0.840 OoII
58 -0.981 OoI
59 -1.094 OoII
62 -0.901 OoI
63 -1.200 OoII
64 -1.025 OoI
66 -1.177 OoI
69 -1.412 OoII

The output is:"

pyrime test_data
