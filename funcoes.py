def arff_to_arff(dados, cabecalho, destino):
    # Abra o arquivo de origem dados em modo de leitura
    with open(dados, 'r') as arquivo_dados:
        fonte_dados = arquivo_dados.readlines()

    # Abra o arquivo de destino em modo de escrita
    with open(cabecalho, 'r') as arquivo_cabecalho:
        fonte_cabecalho = arquivo_cabecalho.readlines()

    with open(destino, 'w') as arquivo_destino:
        # Encontre os índices de início e fim
        inicio = 0
        meio = 0
        fim = len(fonte_dados)
        for i, linha in enumerate(fonte_dados):
            if '@RELATION' in linha:
                inicio = i
            elif '@DATA' in linha:
                meio = i
                break

        # Escreva as linhas desejadas no arquivo de destino
        for i in range(inicio, fim):
            if i <= meio:
                arquivo_destino.write(fonte_cabecalho[i])
            elif i > meio:
                arquivo_destino.write(fonte_dados[i])

def df_to_arff(df_arff, nome, nomesubdir, case):
    # df_arff = df_arff.sort_index(axis=1)
    # caso queira ordenar
    df_arff = df_arff.copy().astype(str)
    df_arff_desordenado = df_arff.copy().astype(str)
    for coluna in df_arff.columns:
        df_arff[coluna] = sorted(df_arff[coluna])
    #df_arff = df_arff #df_arff.apply(lambda x: x.sort_values().values)


    attributes = [('MATRICULA', 'STRING'),
                  ('ANO_INGRESSO', df_arff['ANO_INGRESSO'].unique().astype(str).tolist()),
                  ('ANO_EVASAO', df_arff['ANO_EVASAO'].unique().astype(str).tolist()),
                  ('PERIODO_INGRESSO', df_arff['PERIODO_INGRESSO'].unique().astype(str).tolist()),
                  ('SEXO', df_arff['SEXO'].unique().astype(str).tolist()),
                  ('FAIXA_ETARIA', df_arff['FAIXA_ETARIA'].unique().astype(str).tolist()),
                  ('IDADE', 'NUMERIC'),
                  ('ETNIA', df_arff['ETNIA'].unique().astype(str).tolist()),
                  ('ESTADO_CIVIL', df_arff['ESTADO_CIVIL'].unique().astype(str).tolist()),
                  ('TEMPO_CURSO', df_arff['TEMPO_CURSO'].unique().astype(str).tolist()),
                  ('PERIODO_ATUAL', df_arff['PERIODO_ATUAL'].unique().astype(str).tolist()),
                  ('POSICAO_SEM', 'NUMERIC'),
                  ('COD_COTA', df_arff['COD_COTA'].unique().astype(str).tolist()),
                  ('MEDIA_REFEICOES_SEM_RU', 'NUMERIC'),
                  ('MEDIA_RETIRADAS_SEM_BIBLIOTECA', 'NUMERIC'),
                  ('BOLSISTA', df_arff['BOLSISTA'].unique().astype(str).tolist()),
                  ('MORADIA_CEU', df_arff['MORADIA_CEU'].unique().astype(str).tolist()),
                  ('MONITORIA', df_arff['MONITORIA'].unique().astype(str).tolist()),
                  ('FORMACAO_ENSINO_MEDIO', df_arff['FORMACAO_ENSINO_MEDIO'].unique().astype(str).tolist()),
                  ('INICIOU_CURSO_SUPERIOR', df_arff['INICIOU_CURSO_SUPERIOR'].unique().astype(str).tolist()),
                  ('COMO_MANTER_DURANTE_CURSO', df_arff['COMO_MANTER_DURANTE_CURSO'].unique().astype(str).tolist()),
                  ('MOTIVO_OPTOU_CURSO', df_arff['MOTIVO_OPTOU_CURSO'].unique().astype(str).tolist()),
                  ('PLANO_ENSINO', df_arff['PLANO_ENSINO'].unique().astype(str).tolist()),
                  ('ORIENTACAO_LABORATORIOS', df_arff['ORIENTACAO_LABORATORIOS'].unique().astype(str).tolist()),
                  ('ATUACAO_COORDENADOR', df_arff['ATUACAO_COORDENADOR'].unique().astype(str).tolist()),
                  ('PRATICA_ESTAGIO', df_arff['PRATICA_ESTAGIO'].unique().astype(str).tolist()),
                  ('CORPO_DOCENTE', df_arff['CORPO_DOCENTE'].unique().astype(str).tolist()),
                  ('APROVADAS', 'NUMERIC'),
                  ('REPROVADAS', 'NUMERIC'),
                  ('REP_FREQ', 'NUMERIC'),
                  ('DISP_NOTA', 'NUMERIC'),
                  ('TRANC_TOT', 'NUMERIC'),
                  ('TRANC_PARC', 'NUMERIC'),
                  ('MATRICULADAS', 'NUMERIC'),
                  ('TOTAL', 'NUMERIC'),
                  ('MEDIA', 'REAL'),
                  ('DESEMP_ACAD', df_arff['DESEMP_ACAD'].unique().astype(str).tolist()),
                  ('MEDIA_DISC_MATRICULA', 'REAL'),
                  ('ATEND_PSICOSOCIAL', df_arff['ATEND_PSICOSOCIAL'].unique().astype(str).tolist()),
                  ('BOLSA_BSE', df_arff['BOLSA_BSE'].unique().astype(str).tolist()),
                  ('BOLSA_BSE_ATIVA_SEM', df_arff['BOLSA_BSE_ATIVA_SEM'].unique().astype(str).tolist()),
                  ('BOLSA_BSE_SITUACAO', df_arff['BOLSA_BSE_SITUACAO'].unique().astype(str).tolist()),
                  ('BOLSA_BSE_TEMPO_TOTAL_DIAS', 'NUMERIC'),
                  ('BOLSA_BSE_TEMPO_CORRENTE_DIAS', 'NUMERIC'),
                  ('BOLSA_BSE_DT_INICIO', 'STRING'),
                  ('BOLSA_BSE_DT_TERMINO', 'STRING'),
                  ('NOTA_LING', 'NUMERIC'),
                  ('NOTA_HUMA', 'NUMERIC'),
                  ('NOTA_NATU', 'NUMERIC'),
                  ('NOTA_MATE', 'NUMERIC'),
                  ('NOTA_REDA', 'NUMERIC'),
                  ('MEDIDA_BAIRRO', df_arff['MEDIDA_BAIRRO'].unique().astype(str).tolist()),
                  ('DIASACESSOONLINE', 'NUMERIC'),
                  ('TOTAL_SESSOES', 'NUMERIC'),
                  ('TEMPO_TOTAL_SEG', 'NUMERIC'),
                  ('TOTAL_HIGHLIGHTS', 'NUMERIC'),
                  ('TOTAL_BOOKMARKS', 'NUMERIC'),
                  ('PREVISAO_ANTERIOR', 'NUMERIC'),
                  ('DIFICULDADE_ESTUDANTE', 'NUMERIC'),
                  ('CRA', 'NUMERIC'),
                  ('MEDIA_APROVADAS', 'NUMERIC'),
                  ('MEDIA_REPROVADAS', 'NUMERIC'),
                  ('MEDIA_REP_FREQ', 'NUMERIC'),
                  ('MEDIA_DISP_NOTA', 'NUMERIC'),
                  ('MEDIA_MATRICULADAS', 'NUMERIC'),
                  ('TOTAL_PROJETOS', df_arff['TOTAL_PROJETOS'].unique().astype(str).tolist()),
                  ('CEP_ENDERECO', 'NUMERIC'),
                  ('PRIMEIRA_GERACAO_SUPERIOR', df_arff['PRIMEIRA_GERACAO_SUPERIOR'].unique().astype(str).tolist()),
                  ('ANO_INGRESSO_INSTITUICAO', df_arff['ANO_INGRESSO_INSTITUICAO'].unique().astype(str).tolist()),
                  ('IDADE_INGRESSO_CURSO', 'NUMERIC'),
                  ('INGRESSO_MESMO_CURSO', df_arff['INGRESSO_MESMO_CURSO'].unique().astype(str).tolist()),
                  ('MATRICULAS_OUTRO_CURSO', df_arff['MATRICULAS_OUTRO_CURSO'].unique().astype(str).tolist()),
                  ('TIPO_CHAMADA_INGRESSO', df_arff['TIPO_CHAMADA_INGRESSO'].unique().astype(str).tolist()),
                  ('FORMA_EVASAO', 'STRING'),
                  ('CLASSE', df_arff['CLASSE'].unique().astype(str).tolist())]

    data = df_arff_desordenado.values.tolist()
    arff_dict = {
        'description': '',
        'relation': 'relation',
        'attributes': attributes,
        'data': data
    }
    # escrever e salvar o arquivo ARFF
    if case == 0:
        with open(
                r'/home/arthur/Documents/CursosGraduacaoCopia/' + nome + '/' + nomesubdir + '/2023-2/mineracao/h.arff',
                'w') as f:
            arff.dump(arff_dict, f)
        with open(
                r'/home/arthur/Documents/CursosGraduacaoCopia/' + nome + '/' + nomesubdir + '/2023-2/mineracao/historico.arff',
                'w') as f:
            arff.dump(arff_dict, f)
    elif case == 1:
        try:
            with open(
                    r'/home/arthur/Documents/CursosGraduacaoCopia/' + nome + '/' + nomesubdir + '/2023-2/mineracao/m.arff',
                    'w') as f:
                arff.dump(arff_dict, f)
            with open(
                    r'/home/arthur/Documents/CursosGraduacaoCopia/' + nome + '/' + nomesubdir + '/2023-2/mineracao/matriculados.arff',
                    'w') as f:
                arff.dump(arff_dict, f)
        except:
            print(f'ERRO CASE 1 df_to_arff'*50)

    elif case == 2:
        try:
            with open(
                    r'/home/arthur/Documents/CursosGraduacaoCopia/' + nome + '/' + nomesubdir + '/2023-2/mineracao/m_concat_h.arff',
                    'w') as f:
                arff.dump(arff_dict, f)
        except:
            print(f'ERRO CASE 2 df_to_arff' * 50)


def listar_diretorios(caminho):
    # Lista todos os arquivos e diretórios no caminho especificado
    conteudo = os.listdir(caminho)

    # Filtra apenas os diretórios
    diretorios = [item for item in conteudo if os.path.isdir(os.path.join(caminho, item))]

    return diretorios


def contar_diretorios(caminho):
    # Lista todos os arquivos e diretórios no caminho especificado
    conteudo = os.listdir(caminho)

    # Filtra apenas os diretórios
    diretorios = [item for item in conteudo if os.path.isdir(os.path.join(caminho, item))]

    # Retorna o número de diretórios
    return len(diretorios)
