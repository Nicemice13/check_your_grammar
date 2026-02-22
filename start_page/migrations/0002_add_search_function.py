from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('start_page', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE OR REPLACE FUNCTION search_word(search_term TEXT)
            RETURNS TABLE(
                id INTEGER,
                user_id INTEGER,
                username VARCHAR,
                language VARCHAR,
                corrected_text TEXT,
                created_at TIMESTAMP
            ) AS $$
            BEGIN
                RETURN QUERY
                SELECT 
                    c.id,
                    c.user_id,
                    u.username,
                    c.language,
                    c.corrected_text,
                    c.created_at
                FROM start_page_content c
                JOIN auth_user u ON c.user_id = u.id
                WHERE c.corrected_text ILIKE '%' || search_term || '%';
            END;
            $$ LANGUAGE plpgsql;
            """,
            reverse_sql="DROP FUNCTION IF EXISTS search_word(TEXT);"
        ),
    ]
