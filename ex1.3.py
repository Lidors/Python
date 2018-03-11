sun_class = [['Name', 'Kandel', 'Rafi', 'Sason', 'Akon'],
             ['Grade A', 60, 90, 100, 80], ['Grade B', 70, 95, 20, 80]]

#print(sun_class)

linear_algebra4 = [['Name', 'Kandel', 'Hodgkin', 'Huxley', 'Akon'],
                   ['Grade A', 48, 18, 45, 100], ['Grade B', 50, 32, 45, 98]]

#print(linear_algebra4)


def compare_subjects_within_student(subj1_all_students, subj2_all_students):
      """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """
  max_grade1 =[]
  max_grade1.append(sun_class[0][1:])
  var = max(sun_class[1][1:], sun_class[2][1:])
  max_grade1.append(var)

#finding the max grade btween tow semesters for linear_algebra4
  max_grade2 = []
  max_grade2.append(linear_algebra4[0][1:])
  var = max(linear_algebra4[1][1:], linear_algebra4[2][1:])
  max_grade2.append(var)

  finel_list = dict()
  for j in max_grade1[0]:
	  if j in max_grade2[0]:
		  i1 = max_grade1[0].index(j)
		  i2 = max_grade1[0].index(j)
		  if max_grade1[1][i1] > max_grade2[1][i2]:
			  finel_list[j] = 'sunclass'
		  else:
			  finel_list[j] = 'linear algebra4'
  return print(finel_list)


#finding the max grade btween tow semesters for sun_class
  
