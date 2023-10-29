from sqlalchemy import create_engine, text

db_connect="mysql+pymysql://sql12657626:3eLMkVkd6B@sql12.freesqldatabase.com/sql12657626?charset=utf8mb4"

""" working without giving the ssl parameter depanding on sql service use it may varies
    have to prove SSL certificate if rqiured
    engine = create_engine(
    "mysql+mysqldb://scott:tiger@192.168.0.134/test",
        connect_args={
            "ssl": {
                "ca": "/home/gord/client-ssl/ca.pem",
                "cert": "/home/gord/client-ssl/client-cert.pem",
                "key": "/home/gord/client-ssl/client-key.pem"
            }
        }
    )
"""
engine = engine = create_engine(db_connect)

# fetching the all the jobs information from jobs
def fetch_all_jobs_db():
    with engine.connect() as conn:
        result= conn.execute(text("select * from jobs "))
        jobs_list=[]
        for row in result:
            row_as_dict=row._mapping
            jobs_list.append(row_as_dict)
    return jobs_list


