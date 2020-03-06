from domain.models.microservice.parameters.parameters_model import ParametersModel
from domain.models.promax.parametros.parametros_model import ParametrosModel
from domain.models.dtos.cross_dto.description_dto import DescriptionDTO
from domain.models.dtos.parameters.county_dto import CountyDTO
from domain.models.dtos.parameters.resaler_city_dto import ResalerCityDTO
from domain.models.dtos.parameters.permissions_dto import PermissionsDTO


class ParametersDTO(ParametersModel):

    def __init__(self, parametros_model: ParametrosModel):
        super().__init__()
        self.integration_fields = {
            "company_id": 1,
            "branch_id": 2,
        }
        self.promax_operation_date = parametros_model.data_operacao_promax
        self.company_id = parametros_model.codigo_empresa
        self.branch_id = parametros_model.codigo_filial
        self.active_branch = parametros_model.unidade_ativa
        self.branch_type = DescriptionDTO(parametros_model.tipo_cdd).to_dict()
        self.resaler_id = parametros_model.codigo_revenda
        self.resaler_name = parametros_model.nome_revenda
        self.resaler_address = parametros_model.endereco_revenda
        self.resaler_zipcode = parametros_model.cep_revenda
        self.county = CountyDTO(parametros_model.municipio).to_dict()
        self.resaler_city = ResalerCityDTO(parametros_model.municipio_revenda).to_dict()
        self.resaler_subscription = parametros_model.inscricao_estadual
        self.resaler_document = parametros_model.cnpj_revenda
        self.actual_date = parametros_model.data_atual
        self.resaler_branch = parametros_model.unidade_revenda
        self.expiration = parametros_model.data_expiracao
        self.promax_notification_days = parametros_model.qtde_dias_aviso_promax
        self.dmax_notification_days = parametros_model.qtde_dias_aviso_dmax
        self.multi_site = parametros_model.multi_site
        self.new_review_id = parametros_model.nova_critica
        self.serial_number = parametros_model.numero_serie
        self.integrate_egs = parametros_model.integrou_egs
        self.permissions = PermissionsDTO(parametros_model.permissoes).to_dict()
        self.master_password = parametros_model.senha_mestre
        self.route_model = DescriptionDTO(parametros_model.modelo_roteirizacao).to_dict()
        self.labeler_clients_quantity = parametros_model.qtde_clientes_etiquetador
        self.main_file_code = parametros_model.codigo_bandeira
        self.reorg_limit_date = parametros_model.dia_limite_reorg
        self.erp_software = DescriptionDTO(parametros_model.software_erp).to_dict()
        self.previous_date = parametros_model.data_anterior
        self.sales_profile_group_code = parametros_model.grupo_perfil_venda
        self.solicitation_days = parametros_model.numero_dias_solicitacao
        self.generates_review_log_id = parametros_model.gera_log_critica
        self.app_normal_order_id = parametros_model.pedido_normal_palm
        self.app_contingent_imp_prder_id = parametros_model.pedido_berco_palm
        self.financ_value_sum_id = parametros_model.verificar_valor_financeiro