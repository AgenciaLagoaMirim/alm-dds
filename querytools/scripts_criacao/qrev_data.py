import psycopg2


def criar_tabela_qrev_data():
    # Configurações do banco de dados
    conexao = psycopg2.connect(
        database="teste_dds",
        user="postgres",
        password="admin",
        host="localhost",
        port=5432,
    )

    # Criação da tabela
    with conexao.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS public.qrev_data
            (
                id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
                file_name text COLLATE pg_catalog."default",
                "NumberofTransects" integer,
                startdate timestamp with time zone,
                enddate timestamp with time zone,
                fk_siteinformation bigint NOT NULL,
                CONSTRAINT qrev_data_pkey PRIMARY KEY (id),
                CONSTRAINT qrev_data_fk_siteinformation_c13c78cf_fk_siteinformation_id FOREIGN KEY (fk_siteinformation)
                    REFERENCES public.siteinformation (id) MATCH SIMPLE
                    ON UPDATE NO ACTION
                    ON DELETE NO ACTION
                    DEFERRABLE INITIALLY DEFERRED
            )
            TABLESPACE pg_default;
        """
        )
        # Criação do índice
        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS qrev_data_fk_siteinformation_c13c78cf
            ON public.qrev_data USING btree
            (fk_siteinformation ASC NULLS LAST)
            TABLESPACE pg_default;
        """
        )

    # Commit das alterações e fechamento da conexão
    conexao.commit()
    conexao.close()


# Chamada da função
criar_tabela_qrev_data()