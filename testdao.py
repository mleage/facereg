from DAO import stuDAO
from Entity import StudentInfo

if __name__=="__main__":
    studao=stuDAO.stuDAO();
    stu=studao.selectStudentByIdToStudent("12345")
    print(stu.id)