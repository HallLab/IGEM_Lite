# import os
# import sys
# from pathlib import Path

# import django

# v_root = Path(__file__).parent
# sys.path.append(os.path.abspath(v_root))

# try:
#     from django.conf import settings
#     from django.db import connection

#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')
#     os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
#     django.setup()
#     # from ge.models import (
#     #     Connector,
#     #     Datasource,
#     #     DSTColumn,
#     #     Logs,
#     #     PrefixOpc,
#     #     Term,
#     #     TermCategory,
#     #     TermGroup,
#     #     TermMap,
#     #     WFControl,
#     #     WordMap,
#     #     WordTerm,
#     # )
# except Exception as e:
#     print(e)
#     raise


# # # Truncate Function
# # def truncate_table(table_name):
# table_name = 'termmap'
# try:
#     with connection.cursor() as cursor:
#         # Disable foreign key checks temporarily
#         cursor.execute('PRAGMA foreign_keys = OFF;')
#         # Truncate the table by deleting all records
#         cursor.execute(f"DELETE FROM {table_name};")
#         # Reset the primary key sequence for the table
#         cursor.execute(
#             f"DELETE FROM sqlite_sequence WHERE name='{table_name}';"
#             )
#         # Enable foreign key checks
#         cursor.execute('PRAGMA foreign_keys = ON;')
#         # Vacuum the database to reclaim unused space
#         cursor.execute("VACUUM;")

# except Exception as e:
#     print("ERROR:", e)





# def truncate_ge(table_name):
#     with connection.cursor() as cursor:
#         cursor.execute(f"DELETE FROM {table_name};")
#         cursor.execute("VACUUM;")
#     return True
