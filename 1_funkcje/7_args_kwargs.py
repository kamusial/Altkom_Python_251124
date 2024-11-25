def make_sql_query(table: str, *columns: str, **conditions) -> str:
    # SELECT
    if columns:
        columns_sql = ', '.join(columns)
    else:
        columns_sql = '*'

    # WHERE
    conditions_sql = " AND ".join([f"{key}='{value}'" for key, value in conditions.items()])

    # QUERY
    if conditions_sql:
        query = f"SELECT {columns_sql} FROM {table} WHERE {conditions_sql};"
    else:
        query = f"SELECT {columns_sql} FROM {table};"

    return query

query1 = make_sql_query('uzytkownicy', 'imie', 'nazwisko', wiek=30)
print(query1)

query2 = make_sql_query('produkty', 'nazwa', 'cena', kategoria='biznes')
print(query2)

