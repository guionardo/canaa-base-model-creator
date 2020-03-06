from datetime import date
from canaa_base import BaseModel


class ParametrosModel(BaseModel):

	def __init__(self, parametros_0200: dict):
		super().__init__(parametros_0200)


		# date_testing
		self.teste_date: date = \
			self.get_value('teste_date',field_type=date)

		# company_id
		self.codigo_empresa: int = \
			int(
				self.get_value('codigo_empresa',field_type=dict)).to_dict()

		# branch_id
		self.codigo_filial: int = \
			int(
				self.get_value('codigo_filial',field_type=dict)).to_dict()

		# uses_robin_hood
		self.utiliza_robin_hood: bool = \
			self.get_value('utiliza_robin_hood',field_type=bool)

		# permanences
		self.permanencias: Permanencias = \
			Permanencias(
				self.get_value('permanencias',field_type=dict)).to_dict()

		# advance_discharge_operation
		self.operacao_baixa_vale: int = \
			int(
				self.get_value('operacao_baixa_vale',field_type=dict)).to_dict()

		# advance_credit_account
		self.cta_cred_vale: int = \
			int(
				self.get_value('cta_cred_vale',field_type=dict)).to_dict()

		# advance_credit_sub_account
		self.sub_cta_cred_vale: int = \
			int(
				self.get_value('sub_cta_cred_vale',field_type=dict)).to_dict()

		# products_invoice_series
		self.serie_nf_produtos: str = \
			self.get_value('serie_nf_produtos',field_type=str)

		# products_invoice_report_number
		self.nr_relatorio_nf_produtos: int = \
			int(
				self.get_value('nr_relatorio_nf_produtos',field_type=dict)).to_dict()

		# uses_input_invoice_module
		self.utiliza_modulo_nf_entrada: bool = \
			self.get_value('utiliza_modulo_nf_entrada',field_type=bool)

		# uses_scb_interface
		self.utiliza_interface_scb: str = \
			self.get_value('utiliza_interface_scb',field_type=str)

		# uses_sales_attributes
		self.utilizar_atributos_vendas: str = \
			self.get_value('utilizar_atributos_vendas',field_type=str)

		# advance_bank
		self.banco_para_vale: int = \
			int(
				self.get_value('banco_para_vale',field_type=dict)).to_dict()

		# advance_modality
		self.modalidade_para_vale: int = \
			int(
				self.get_value('modalidade_para_vale',field_type=dict)).to_dict()

		# post_dated_check_interest_account
		self.conta_juros_prest: int = \
			int(
				self.get_value('conta_juros_prest',field_type=dict)).to_dict()

		# calc_rule_number
		self.nr_regra_calculo: int = \
			int(
				self.get_value('nr_regra_calculo',field_type=dict)).to_dict()

		# assignment_discount
		self.desconto_consignacao: str = \
			self.get_value('desconto_consignacao',field_type=str)

		# create_sav_interface
		self.gerar_interface_sav: str = \
			self.get_value('gerar_interface_sav',field_type=str)

		# carrying_code
		self.codigo_transportadora: int = \
			int(
				self.get_value('codigo_transportadora',field_type=dict)).to_dict()

		# sales_with_dozen_critic
		self.criticar_vendas_com_duzia: float = \
			self.get_value('criticar_vendas_com_duzia',field_type=float)

		# retail_infoice_series
		self.serie_nf_varejo: str = \
			self.get_value('serie_nf_varejo',field_type=str)

		# bonification_discount
		self.desconto_bonificacao: str = \
			self.get_value('desconto_bonificacao',field_type=str)

		# incoming_invoice_series
		self.serie_nf_entrada: str = \
			self.get_value('serie_nf_entrada',field_type=str)

		# mapping
		self.mapeamento: str = \
			self.get_value('mapeamento',field_type=str)

		# mapping_criteria
		self.criterio_mapeamento: str = \
			self.get_value('criterio_mapeamento',field_type=str)

		# cask_valorize
		self.valoriza_vasilhame: str = \
			self.get_value('valoriza_vasilhame',field_type=str)

		# cask_valorization_table
		self.tabela_valorizacao_vasilhame: int = \
			int(
				self.get_value('tabela_valorizacao_vasilhame',field_type=dict)).to_dict()

		# uses_combined_table
		self.utiliza_tabela_combinada: float = \
			self.get_value('utiliza_tabela_combinada',field_type=float)

		# informs_payment_condition
		self.informa_cond_pagamento: str = \
			self.get_value('informa_cond_pagamento',field_type=str)

		# assignment_sale_operation
		self.operacao_venda_comodato: int = \
			int(
				self.get_value('operacao_venda_comodato',field_type=dict)).to_dict()

		# consists_ttc
		self.consiste_ttc: str = \
			self.get_value('consiste_ttc',field_type=str)

		# auto_order_number
		self.nr_pedido_auto: str = \
			self.get_value('nr_pedido_auto',field_type=str)

		# as_price_table
		self.tabela_preco_as: int = \
			int(
				self.get_value('tabela_preco_as',field_type=dict)).to_dict()

		# off_route_box_min_qty
		self.qtde_minima_cx_fora_rota: int = \
			int(
				self.get_value('qtde_minima_cx_fora_rota',field_type=dict)).to_dict()

		# pis_cofins_rate
		self.aliquota_pis_cofins: int = \
			int(
				self.get_value('aliquota_pis_cofins',field_type=dict)).to_dict()

		# invoice_credit_account
		self.conta_credito_nf: int = \
			int(
				self.get_value('conta_credito_nf',field_type=dict)).to_dict()

		# invoice_credit_sub_account
		self.sub_conta_credito_nf: int = \
			int(
				self.get_value('sub_conta_credito_nf',field_type=dict)).to_dict()

		# load_monitoring
		self.monitoramento_carga: str = \
			self.get_value('monitoramento_carga',field_type=str)

		# planner
		self.planner: bool = \
			self.get_value('planner',field_type=bool)

		# outcoming_invoice_format_number
		self.nr_formato_nf_saida: int = \
			int(
				self.get_value('nr_formato_nf_saida',field_type=dict)).to_dict()

		# outcoming_document_report_number
		self.nr_relatorio_documento_saida: int = \
			int(
				self.get_value('nr_relatorio_documento_saida',field_type=dict)).to_dict()

		# customer_block_days_number
		self.nr_dias_bloqueio_clientes: int = \
			int(
				self.get_value('nr_dias_bloqueio_clientes',field_type=dict)).to_dict()

		# incoming_invoice_format_number
		self.nr_formato_nf_entrada: int = \
			int(
				self.get_value('nr_formato_nf_entrada',field_type=dict)).to_dict()

		# incoming_document_report_number
		self.nr_relatorio_documento_entrada: int = \
			int(
				self.get_value('nr_relatorio_documento_entrada',field_type=dict)).to_dict()

		# palmtop_invoice_format_number
		self.nr_formato_nf_palmtop: int = \
			int(
				self.get_value('nr_formato_nf_palmtop',field_type=dict)).to_dict()

		# invoice_products_new_series
		self.serie_nf_produtos_nova: str = \
			self.get_value('serie_nf_produtos_nova',field_type=str)

		# informs_cancelling_devolution_map
		self.informa_mapa_devolucao_cancelamento: bool = \
			self.get_value('informa_mapa_devolucao_cancelamento',field_type=bool)

		# lists_total_cask
		self.lista_vasilhame_total: str = \
			self.get_value('lista_vasilhame_total',field_type=str)

		# uses_stock_grid
		self.utiliza_grade_estoque: str = \
			self.get_value('utiliza_grade_estoque',field_type=str)

		# due_date_from_issue
		self.vencimento_apartir_emissao: str = \
			self.get_value('vencimento_apartir_emissao',field_type=str)

		# income_statement_type
		self.tipo_prestacao_contas: str = \
			self.get_value('tipo_prestacao_contas',field_type=str)

		# payment_parcel_account
		self.conta_pagamento_prestacao: int = \
			int(
				self.get_value('conta_pagamento_prestacao',field_type=dict)).to_dict()

		# radio_frequence
		self.radio_frequencia: RadioFrequencia = \
			RadioFrequencia(
				self.get_value('radio_frequencia',field_type=dict)).to_dict()

		# sales_state
		self.ind_est_vendas: DescricaoModel = \
			DescricaoModel(
				self.get_value('ind_est_vendas',field_type=dict)).to_dict()

		# accounts_receivable_customer_key
		self.contas_a_receber_clientes_chave: DescricaoModel = \
			DescricaoModel(
				self.get_value('contas_a_receber_clientes_chave',field_type=dict)).to_dict()


# CREATED BY MODEL_CREATOR IN 2020-03-06 17:38:59.127152
