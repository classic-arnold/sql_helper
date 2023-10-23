import os
from mysql.connector import connect, Error

def get_mutual_res(res1, res2):
    map_helper = {}
    mutual_res = []

    for res in res1:
        map_helper[res[0]] = None

    for res in res2:
        if type(res) is tuple and res[0] in map_helper:
            mutual_res.append(res[0])
        elif res in map_helper:
            mutual_res.append(res)

    return mutual_res

try:
    with connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS"),
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("USE movies;")

            def helper(query_no, prev_res):
                if query_no == 6:
                    return

                with open(f"sql_files/{query_no}.sql", "r+") as query:
                    with open(f"sql_files/{query_no}.opp.sql", "r+") as query_opp:
                        # query
                        cursor.execute(query.read())
                        res = cursor.fetchall()
                        if len(res) > 0 and prev_res is not None:
                            res = get_mutual_res(res, prev_res)
                        print("\t" * (query_no-1), "Yes: ", len(res))
                        helper(query_no+1, res)
                        
                        # opposite query
                        cursor.execute(query_opp.read())
                        res = cursor.fetchall()
                        if len(res) > 0 and prev_res is not None:
                            res = get_mutual_res(res, prev_res)
                        print("\t" * (query_no-1), "No: ", len(res))
                        helper(query_no+1, res)

            helper(1, None)
except Error as e:
    print(e)