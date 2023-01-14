
Question:

It's photo day at the local school, and you're the photographer assigned to take class photos.

The class has an even number of students. All the students are wearing red or blue shirts. 

Half are wearing red, the other half is wearing blue.

Arrange the students in two rows before taking the photo.

Each row should contain the same number of students and must follow the below guidelines 
- All studnets wearing red shirts must be in the same row
- All students wearing blue shirts must be in the same row
- Each student in the back row must be taller than the student directly in front of them in the front row.

You're given two input arrays: one with the height of all the students with red shirts and another containing the heights of all the students with blue shirts.

These arrays will always have the same length and each height will be a positive integer.

Write a function that returns whether or not a class photo that follows the above guidelines can be taken.

* you can assume that each class has at least two students.



sample input:

redShirts = [5,8,1,3,4]
blueShirts = [6,9,2,4,5]


sample output:

True
... Place all students with blue shirts in the back row


Optimal space & time complexity:

0(log n) time 
0(1) space

where n is the number of students