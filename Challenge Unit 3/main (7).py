class student:
  def_init_(self,name,roll_number,cpga):
  self.name=name
  self.roll_number=roll_number self.cpga=cpga
  def sort_students(student_list):
    sorted_students=sorted(student_list,key=lambda student:student.cpga,reverse=True)
    return sorted_students
    student=[Student("pooja","A123","9.9"),Student("anitha","A1234","9.8"),Student("hari","A1215","9.7"),Student("varshini","A126","9.6")]
    sorted-students=sort_students(students)
    for student in sorted_students:
      print("name:{},rollnumber:{},cpga:{}.".format(studentname,student.roll_number,student.cpga))