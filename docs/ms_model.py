from datetime import datetime
from canaa_base import BaseModel

from domain.models.microservice.cross_entity.description_model import DescriptionModel
from domain.models.microservice.parameters.county_model import CountyModel
from domain.models.microservice.parameters.resaler_city_model import ResalerCityModel
from domain.models.microservice.parameters.permissions_model import PermissionsModel

class ParametersModel(BaseModel):

    def __init__(self):
        self.integration_fields: dict = {}
        self.promax_operation_date: datetime = None
        self.company_id: int = 0
        self.branch_id: int = 0
        self.active_branch: bool = False
        self.branch_type: DescriptionModel = DescriptionModel()
        self.resaler_id: int = 0
        self.resaler_name: str = ''
        self.resaler_address: str = ''
        self.resaler_zipcode: str = ''
        self.county: CountyModel = CountyModel()
        self.resaler_city: ResalerCityModel = ResalerCityModel()
        self.resaler_subscription: str = ''
        self.resaler_document: str = ''
        self.actual_date: datetime = None
        self.resaler_branch: int = 0
        self.expiration: datetime = None
        self.promax_notification_days: int = 0
        self.dmax_notification_days: int = 0
        self.multi_site: str = ''
        self.new_review_id: bool = False
        self.serial_number: int = 0
        self.integrate_egs: bool = False
        self.permissions: PermissionsModel = PermissionsModel()
        self.master_password: str = ''
        self.route_model: DescriptionModel = DescriptionModel()
        self.labeler_clients_quantity: int = 0
        self.main_file_code: str = ''
        self.reorg_limit_date: int = 0
        self.erp_software: DescriptionModel = DescriptionModel()
        self.previous_date: datetime = None
        self.sales_profile_group_code: int = 0
        self.solicitation_days: int = 0
        self.generates_review_log_id: bool = False
        self.app_normal_order_id: bool = False
        self.app_contingent_imp_prder_id: bool = False
        self.financ_value_sum_id: bool = False