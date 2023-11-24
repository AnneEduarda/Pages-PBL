import pandas as pd


dados = pd.read_csv('sample_data_clean.csv')


dados = dados.drop(columns=[
       'dh_prescricao_lancamento', 'cd_exame_sgh',
       'ds_alias_exame_millennium',
       'ds_alias_exame_millennium_2', 'ds_alias_exame_millennium_3',
       'cd_status_prescricao', 'st_prescricao_exame', 'id_accession_exame',
       'ds_accession_exame', 'ds_local_coleta','ds_quarto_coleta',
       'ds_leito_coleta', 'dh_coleta_exame', 'dh_recebimento_exame',
       'dh_liberacao_exame', 'ds_metodo_coleta',
       'ds_material_subtipo',
       'ds_micro_organismo',
       'ds_antibiotico_microorganismo', 'ds_mic_microorganismo',
       'cd_metodo_antibiograma',
       'ic_crescimento_microorganismo', 'cd_status_resultado_exame',
       'st_resultado_exame', 'dh_ultima_atualizacao', 'st_tipo_resultado',
       'ds_resultado_exame', 'te_observacoes_hemocultura', 'cd_passagem',
       'cd_prontuario', 'id_passagem', 'id_prontuario', 'id_exame_prescrito',
       'id_evento_prescricao'])


#pd.options.display.max_columns = None

#print(dados.columns)

dados = dados.dropna()

#print(dados.head)

dados = dados.reset_index(drop=True)


dados.to_csv('dadoslimpos.csv')