from utils.db_api import mydb


def get_theme(language: str, theme: str) -> tuple:
    """
    Bозвращает Описания, Пример, Тему, ЯП 
    [{'description'}, {'Example'}, {'Theme'}, {'Language'}]
    """

    conn, cur = mydb.connect()

    cur.execute("select he.description, he.exaple, hc.name as thame, hl.name as language from helper_exaple as he "
                "inner join helper_commands as hc on he.helper_commands_id = hc.id inner join helper_language as hl "
                "on he.helper_language_id = hl.id where hl.name = %s and hc.name = %s", (language, theme))

    myresult = cur.fetchone()
    cur.close()
    return myresult


def get_name_theme(language: str) -> list:
    """
    Bозвращает Тему, ЯП 
    [{'Theme'}, {'Language'}]
    """
    conn, cur = mydb.connect()

    cur.execute("SELECT hc.name AS theme, hl.name as language FROM helper_exaple AS he "
                "INNER JOIN helper_commands AS hc ON he.helper_commands_id = hc.id INNER JOIN helper_language AS hl "
                "ON he.helper_language_id = hl.id WHERE hl.name = %s ", (language,))

    myresult = cur.fetchall()
    cur.close()
    return myresult