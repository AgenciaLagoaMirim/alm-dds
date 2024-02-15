import psycopg2


def criar_tabela_channelsummary():
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
            CREATE TABLE IF NOT EXISTS public.channelsummary
            (
                id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
                "Top" double precision,
                "Middle" double precision,
                "Bottom" double precision,
                "Left" double precision,
                "Right" double precision,
                "Total" double precision,
                "MovingBedPercentCorrection" double precision,
                fk_qrev_data bigint NOT NULL,
                CONSTRAINT channelsummary_pkey PRIMARY KEY (id),
                CONSTRAINT channelsummary_fk_qrev_data_8b4354be_fk_qrev_data_id FOREIGN KEY (fk_qrev_data)
                    REFERENCES public.qrev_data (id) MATCH SIMPLE
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
            CREATE INDEX IF NOT EXISTS channelsummary_fk_qrev_data_8b4354be
            ON public.channelsummary USING btree
            (fk_qrev_data ASC NULLS LAST)
            TABLESPACE pg_default;
        """
        )

    # Commit das alterações e fechamento da conexão
    conexao.commit()
    conexao.close()


# Chamada da função
criar_tabela_channelsummary()