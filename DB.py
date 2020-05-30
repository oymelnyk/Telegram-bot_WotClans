import pypyodbc


connection = pypyodbc.connect('Driver={SQL Server};''Server=MINOTEBOOK\SQL_SERVER;UID=USER;PWD=Qq_1234567;Database=b_telegram;') #ODBC Driver 17 for SQL Server
cursor= connection.cursor()

SQL_SELECT_TOP_50="""
                    SELECT TOP (50)
       [efficiency_rank]
      ,[clan_tag]
      ,[efficiency_rank_delta]

      
      
  FROM [b_telegram].[dbo].[Clans] 
  ORDER BY efficiency_rank"""



SQL_DELETE_DATA_Clans="""
DELETE FROM [b_telegram].[dbo].[Clans]
"""



connection.commit()

