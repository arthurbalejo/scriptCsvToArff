import pandas as pd

from funcoes import arff_to_arff, df_to_arff, contar_diretorios, listar_diretorios 


# Substitua 'caminho/do/seu/diretorio' pelo caminho real do diretório que você deseja verificar
diretorio_especificado = '/home/arthur/Documents/CursosGraduacaoCopia'

numero_de_diretorios = contar_diretorios(diretorio_especificado)

print(f"Número de diretórios em {diretorio_especificado}: {numero_de_diretorios}")

nomes_diretorios = listar_diretorios(diretorio_especificado)

print(f"Nome dos diretorios: {nomes_diretorios}")

for nome in nomes_diretorios:
    subdiretorio_especificado = '/home/arthur/Documents/CursosGraduacaoCopia/' + nome + '/'
    nomes_subdir = listar_diretorios('/home/arthur/Documents/CursosGraduacaoCopia/' + nome + '/')
    numero_de_subdiretorios = contar_diretorios(subdiretorio_especificado)
    print(f"-" * 30)
    print(f"Número de subdiretórios em {nome}: {numero_de_subdiretorios}")
    print(f"Subdiretórios a serem analisados {nomes_subdir}")

    for nomesubdir in nomes_subdir:
        print(f"-" * 30)
        print(f"{nome}: {nomesubdir}")
    #cursos sem a pasta 2023/2: 
    #CAL 724, 725, 726 // CCSH 3004 // CCS 211
        try: 
            diretorio_analise = '/home/arthur/Documents/CursosGraduacaoCopia/' + nome + '/' + nomesubdir + '/2023-2/dadosSQL/'
            arquivo_treina = diretorio_analise + '/treina.csv'
            arquivo_teste = diretorio_analise + '/teste.csv'
            # aplicar df treina
            treina = pd.read_csv(arquivo_treina, encoding='latin-1')
            treina = treina.drop(columns=['NOME_ALUNO', 'NOME_CURSO', 'ID_CURSO_ALUNO', 'ID_ALUNO',
                                        'PERIODO_REALIZACAO'])
            treina.to_csv(
                r'/home/arthur/Documents/CursosGraduacaoCopia/' + nome + '/' + nomesubdir + '/2023-2/mineracao/historico.csv',
                index=False)
            # aplicar df teste
            teste = pd.read_csv(arquivo_teste, encoding='latin-1')
            teste = teste.drop(columns=['NOME_ALUNO', 'NOME_CURSO', 'ID_CURSO_ALUNO', 'ID_ALUNO',
                                        'PERIODO_REALIZACAO'])
            teste['ANO_EVASAO'] = teste['ANO_EVASAO'].fillna('?')
            # remover calouros
            calouros = teste.loc[((teste['ANO_INGRESSO'] == 2023) & (teste['PERIODO_INGRESSO'] == "'2. Semestre'"))]
            # print(calouros)
            teste = teste.loc[~((teste['ANO_INGRESSO'] == 2023) & (teste['PERIODO_INGRESSO'] == "'2. Semestre'"))]
            #teste_calouros_final = pd.concat([teste, calouros])
            #teste_calouros_final.reset_index(drop=True, inplace=True)
            # print(teste_calouros_final.tail())
            teste.to_csv(
                r'/home/arthur/Documents/CursosGraduacaoCopia/' + nome + '/' + nomesubdir + '/2023-2/mineracao/matriculados.csv',
                index=False)
            m_concat_h = pd.concat([treina, teste])
            m_concat_h.reset_index(drop=True, inplace=True)
            m_concat_h.to_csv(
                r'/home/arthur/Documents/CursosGraduacaoCopia/' + nome + '/' + nomesubdir + '/2023-2/mineracao/m_concat_h.csv',
                index=False)

            df_to_arff(treina, nome, nomesubdir, 0)
            df_to_arff(teste, nome, nomesubdir, 1)
            #print(m_concat_h.tail())
            df_to_arff(m_concat_h, nome, nomesubdir, 2)

            arff_to_arff(r'/home/arthur/Documents/CursosGraduacaoCopia/' + nome + '/' + nomesubdir + '/2023-2/mineracao/h.arff',
                        r'/home/arthur/Documents/CursosGraduacaoCopia/' + nome + '/' + nomesubdir + '/2023-2/mineracao/m_concat_h.arff',
                        r'/home/arthur/Documents/CursosGraduacaoCopia/' + nome + '/' + nomesubdir + '/2023-2/mineracao/historico.arff')

            arff_to_arff(
                r'/home/arthur/Documents/CursosGraduacaoCopia/' + nome + '/' + nomesubdir + '/2023-2/mineracao/m.arff',
                r'/home/arthur/Documents/CursosGraduacaoCopia/' + nome + '/' + nomesubdir + '/2023-2/mineracao/m_concat_h.arff',
                r'/home/arthur/Documents/CursosGraduacaoCopia/' + nome + '/' + nomesubdir + '/2023-2/mineracao/matriculados.arff')


        except:
            print(f"*" * 60)
            print(f'O Curso {nomesubdir} não tem a pasta 2023-2')
            print(f"*" * 60)