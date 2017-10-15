import pymysql
connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='mysql',
                                     db='Quizzer',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

def queryCheck(table,IDName,rowName,rowValue):
    with connection.cursor() as cursor:
        sql="SELECT %s FROM MCQs WHERE %s = %s"
        cursor.execute(sql,(IDName,rowName,rowValue))
        result = cursor.fetchone()
        print (result)
        return result