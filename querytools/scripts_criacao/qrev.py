import psycopg2


def criar_tabela_qrev():
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
            CREATE TABLE IF NOT EXISTS public.qrev
            (
                id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
                "MeanWidth" double precision,
                "WidthCOV" double precision,
                "MeanArea" double precision,
                "AreaCOV" double precision,
                "MeanBoatSpeed" double precision,
                "MeanQoverA" double precision,
                "MeanCourseMadeGood" double precision,
                "MeanFlowDirection" double precision,
                "MeanDepth" double precision,
                "MaximumDepth" double precision,
                "MaximumWaterSpeed" double precision,
                "NumberofTransects" integer,
                "Duration" integer,
                "LeftQPer" double precision,
                "RightQPer" double precision,
                "InvalidCellsQPer" double precision,
                "InvalidEnsQPer" double precision,
                "UserRating" text COLLATE pg_catalog."default",
                "DischargePPDefault" double precision,
                fk_qrev bigint NOT NULL,
                CONSTRAINT qrev_pkey PRIMARY KEY (id),
                CONSTRAINT qrev_fk_qrev_90a36a81_fk_qrev_data_id FOREIGN KEY (fk_qrev)
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
            CREATE INDEX IF NOT EXISTS qrev_fk_qrev_90a36a81
            ON public.qrev USING btree
            (fk_qrev ASC NULLS LAST)
            TABLESPACE pg_default;
        """
        )

    # Commit das alterações e fechamento da conexão
    conexao.commit()
    conexao.close()


# Chamada da função
criar_tabela_qrev()