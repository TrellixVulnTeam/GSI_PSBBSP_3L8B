import connexion
from swagger_server.models.account import Account
from swagger_server.models.accounts import Accounts
from swagger_server.models.dataclass import Dataclass
from swagger_server.models.dataclasses import Dataclasses
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.process import Process
from swagger_server.models.process_dataclass_matrix import ProcessDataclassMatrix
from swagger_server.models.processes import Processes
from swagger_server.models.project import Project
from swagger_server.models.projects import Projects
from swagger_server.models.subsystem import Subsystem
from swagger_server.models.subsystems import Subsystems
from swagger_server.models.support_system import SupportSystem
from swagger_server.models.support_system_dataclass_matrix import SupportSystemDataclassMatrix
from swagger_server.models.support_system_organization_unit_matrix import SupportSystemOrganizationUnitMatrix
from swagger_server.models.support_system_process_matrix import SupportSystemProcessMatrix
from swagger_server.models.support_systems import SupportSystems
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_user_to_project(project_id, account_id, account_id_session, token):
    """
    Add user to project
    
    :param project_id: Project Id
    :type project_id: int
    :param account_id: Account identifier located in the url path
    :type account_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def create_account(username, email, password, account_id_session, token):
    """
    Create new account
    
    :param username: Account username
    :type username: str
    :param email: Account email
    :type email: str
    :param password: Account password
    :type password: str
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def create_dataclass(project_id, name, description, account_id_session, token):
    """
    Create new dataclass
    
    :param project_id: Project Id
    :type project_id: int
    :param name: Name
    :type name: str
    :param description: Description
    :type description: str
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def create_organization_unit(name, account_id_session, token):
    """
    Create new organization unit
    
    :param name: Name
    :type name: str
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def create_process(project_id, name, description, account_id_session, token):
    """
    Create new process
    
    :param project_id: Project Id
    :type project_id: int
    :param name: Name
    :type name: str
    :param description: Description
    :type description: str
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def create_process_dataclass_matrix(project_id, process_dataclass_matrix, account_id_session, token):
    """
    Create new process X dataclass matrix
    
    :param project_id: Project Id
    :type project_id: int
    :param process_dataclass_matrix: Process X dataclass values
    :type process_dataclass_matrix: dict | bytes
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    if connexion.request.is_json:
        process_dataclass_matrix = ProcessDataclassMatrix.from_dict(connexion.request.get_json())
    return 'do some magic!'


def create_projects(name, account_id_session, token):
    """
    Create new project
    
    :param name: Name
    :type name: str
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def create_subsystem(project_id, name, description, account_id_session, token):
    """
    Create new subsystem
    
    :param project_id: Project Id
    :type project_id: int
    :param name: Name
    :type name: str
    :param description: Description
    :type description: str
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def create_support_system(name, account_id_session, token):
    """
    Create new support system
    
    :param name: Name
    :type name: str
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def create_support_system_dataclass_matrix(project_id, support_system_dataclass_matrix, account_id_session, token):
    """
    Create new support system X dataclass matrix
    
    :param project_id: Project Id
    :type project_id: int
    :param support_system_dataclass_matrix: Support system X dataclass values
    :type support_system_dataclass_matrix: dict | bytes
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    if connexion.request.is_json:
        support_system_dataclass_matrix = SupportSystemDataclassMatrix.from_dict(connexion.request.get_json())
    return 'do some magic!'


def create_support_system_organization_unit_matrix(project_id, support_system_organization_unit_matrix, account_id_session, token):
    """
    Create new support system X organization unit matrix
    
    :param project_id: Project Id
    :type project_id: int
    :param support_system_organization_unit_matrix: Support system X organization unit values
    :type support_system_organization_unit_matrix: dict | bytes
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    if connexion.request.is_json:
        support_system_organization_unit_matrix = SupportSystemOrganizationUnitMatrix.from_dict(connexion.request.get_json())
    return 'do some magic!'


def create_support_system_process_matrix(project_id, support_system_process_matrix, account_id_session, token):
    """
    Create new support system X process matrix
    
    :param project_id: Project Id
    :type project_id: int
    :param support_system_process_matrix: Support system X process values
    :type support_system_process_matrix: dict | bytes
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    if connexion.request.is_json:
        support_system_process_matrix = SupportSystemProcessMatrix.from_dict(connexion.request.get_json())
    return 'do some magic!'


def delete_account(account_id, account_id_session, token):
    """
    Delete account
    
    :param account_id: Account identifier located in the url path
    :type account_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def delete_dataclass(project_id, dataclass_id, account_id_session, token):
    """
    Delete dataclass
    
    :param project_id: Project Id
    :type project_id: int
    :param dataclass_id: Dataclass identifier located in the url path
    :type dataclass_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def delete_organization_unit(organization_unit_id, account_id_session, token):
    """
    Delete organization unit
    
    :param organization_unit_id: Organization unit identifier located in the url path
    :type organization_unit_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def delete_process(project_id, process_id, account_id_session, token):
    """
    Delete process
    
    :param project_id: Project Id
    :type project_id: int
    :param process_id: Process identifier located in the url path
    :type process_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def delete_process_dataclass_matrix(project_id, account_id_session, token):
    """
    Delete process X dataclass matrix
    
    :param project_id: Project Id
    :type project_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def delete_project(project_id, account_id_session, token):
    """
    Delete project
    
    :param project_id: Project Id
    :type project_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def delete_subsystem(project_id, subsystem_id, account_id_session, token):
    """
    Delete subsystem
    
    :param project_id: Project Id
    :type project_id: int
    :param subsystem_id: Subsystem identifier located in the url path
    :type subsystem_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def delete_support_system(support_system_id, account_id_session, token):
    """
    Delete support system
    
    :param support_system_id: Support system identifier located in the url path
    :type support_system_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def delete_support_system_dataclass_matrix(project_id, account_id_session, token):
    """
    Delete support system X dataclass matrix
    
    :param project_id: Project Id
    :type project_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def delete_support_system_organization_unit_matrix(project_id, account_id_session, token):
    """
    Delete support system X organization unit matrix
    
    :param project_id: Project Id
    :type project_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def delete_support_system_process_matrix(project_id, account_id_session, token):
    """
    Delete support system X process matrix
    
    :param project_id: Project Id
    :type project_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def get_account(account_id, account_id_session, token):
    """
    Get account
    
    :param account_id: Account identifier located in the url path
    :type account_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: Account
    """
    return 'do some magic!'


def get_dataclass(project_id, dataclass_id, account_id_session, token):
    """
    Get dataclass
    
    :param project_id: Project Id
    :type project_id: int
    :param dataclass_id: Dataclass identifier located in the url path
    :type dataclass_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: Dataclass
    """
    return 'do some magic!'


def get_organization_unit(organization_unit_id, account_id_session, token):
    """
    Get organization unit
    
    :param organization_unit_id: Organization unit identifier located in the url path
    :type organization_unit_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: SupportSystem
    """
    return 'do some magic!'


def get_process(project_id, process_id, account_id_session, token):
    """
    Get process
    
    :param project_id: Project Id
    :type project_id: int
    :param process_id: Process identifier located in the url path
    :type process_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: Process
    """
    return 'do some magic!'


def get_process_dataclass_matrix(project_id, account_id_session, token):
    """
    Get process X dataclass matrix
    
    :param project_id: Project Id
    :type project_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: ProcessDataclassMatrix
    """
    return 'do some magic!'


def get_project(project_id, account_id_session, token):
    """
    Get project
    
    :param project_id: Project Id
    :type project_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: Project
    """
    return 'do some magic!'


def get_subsystem(project_id, subsystem_id, account_id_session, token):
    """
    Get subsystem
    
    :param project_id: Project Id
    :type project_id: int
    :param subsystem_id: Subsystem identifier located in the url path
    :type subsystem_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: Subsystem
    """
    return 'do some magic!'


def get_support_system(support_system_id, account_id_session, token):
    """
    Get support system
    
    :param support_system_id: Support system identifier located in the url path
    :type support_system_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: SupportSystem
    """
    return 'do some magic!'


def get_support_system_dataclass_matrix(project_id, account_id_session, token):
    """
    Get support system X dataclass matrix
    
    :param project_id: Project Id
    :type project_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: SupportSystemDataclassMatrix
    """
    return 'do some magic!'


def get_support_system_organization_unit_matrix(project_id, account_id_session, token):
    """
    Get support system X organization unit matrix
    
    :param project_id: Project Id
    :type project_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: SupportSystemOrganizationUnitMatrix
    """
    return 'do some magic!'


def get_support_system_process_matrix(project_id, account_id_session, token):
    """
    Get support system X process matrix
    
    :param project_id: Project Id
    :type project_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: SupportSystemProcessMatrix
    """
    return 'do some magic!'


def list_accounts(account_id_session, token):
    """
    List accounts
    
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: Accounts
    """
    return 'do some magic!'


def list_dataclasses(project_id, account_id_session, token):
    """
    List dataclasses
    
    :param project_id: Project Id
    :type project_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: Dataclasses
    """
    return 'do some magic!'


def list_organization_units(account_id_session, token):
    """
    List organization units
    
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: SupportSystems
    """
    return 'do some magic!'


def list_processes(project_id, account_id_session, token):
    """
    List processes
    
    :param project_id: Project Id
    :type project_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: Processes
    """
    return 'do some magic!'


def list_projects(account_id_session, token):
    """
    List projects
    
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: Projects
    """
    return 'do some magic!'


def list_subsystems(project_id, account_id_session, token):
    """
    List subsystems
    
    :param project_id: Project Id
    :type project_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: Subsystems
    """
    return 'do some magic!'


def list_support_systems(account_id_session, token):
    """
    List support systems
    
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: SupportSystems
    """
    return 'do some magic!'


def list_users_in_project(project_id, account_id_session, token):
    """
    List users in project
    
    :param project_id: Project Id
    :type project_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: Accounts
    """
    return 'do some magic!'


def login(email, password):
    """
    User authentication
    
    :param email: Account email
    :type email: str
    :param password: Account password
    :type password: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def logout(account_id_session, token):
    """
    User logs out
    
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def remove_user_from_project(project_id, account_id, account_id_session, token):
    """
    Remove user from project
    
    :param project_id: Project Id
    :type project_id: int
    :param account_id: Account identifier located in the url path
    :type account_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def update_account(account_id, account_id_session, token, account_username=None, email=None, account_password=None):
    """
    Update account
    
    :param account_id: Account identifier located in the url path
    :type account_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str
    :param account_username: Account username
    :type account_username: str
    :param email: Account email
    :type email: str
    :param account_password: Account password
    :type account_password: str

    :rtype: None
    """
    return 'do some magic!'


def update_dataclass(project_id, dataclass_id, account_id_session, token, dataclass_name=None, dataclass_description=None):
    """
    Update dataclass
    
    :param project_id: Project Id
    :type project_id: int
    :param dataclass_id: Dataclass identifier located in the url path
    :type dataclass_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str
    :param dataclass_name: Dataclass name
    :type dataclass_name: str
    :param dataclass_description: Dataclass description
    :type dataclass_description: str

    :rtype: None
    """
    return 'do some magic!'


def update_organization_unit(organization_unit_id, account_id_session, token, support_system_name=None):
    """
    Update organization unit
    
    :param organization_unit_id: Organization unit identifier located in the url path
    :type organization_unit_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str
    :param support_system_name: Support system name
    :type support_system_name: str

    :rtype: None
    """
    return 'do some magic!'


def update_process(project_id, process_id, account_id_session, token, dataclass_name=None, dataclass_description=None):
    """
    Update process
    
    :param project_id: Project Id
    :type project_id: int
    :param process_id: Process identifier located in the url path
    :type process_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str
    :param dataclass_name: Dataclass name
    :type dataclass_name: str
    :param dataclass_description: Dataclass description
    :type dataclass_description: str

    :rtype: None
    """
    return 'do some magic!'


def update_process_dataclass_matrix(project_id, process_dataclass_matrix, account_id_session, token):
    """
    Update process X dataclass matrix
    
    :param project_id: Project Id
    :type project_id: int
    :param process_dataclass_matrix: Process X dataclass values
    :type process_dataclass_matrix: dict | bytes
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    if connexion.request.is_json:
        process_dataclass_matrix = ProcessDataclassMatrix.from_dict(connexion.request.get_json())
    return 'do some magic!'


def update_project(project_id, account_id_session, token, project_name=None):
    """
    Update project
    
    :param project_id: Project Id
    :type project_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str
    :param project_name: Project name
    :type project_name: str

    :rtype: None
    """
    return 'do some magic!'


def update_subsystem(project_id, subsystem_id, account_id_session, token, subsystem_name=None, subsystem_description=None):
    """
    Update subsystem
    
    :param project_id: Project Id
    :type project_id: int
    :param subsystem_id: Subsystem identifier located in the url path
    :type subsystem_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str
    :param subsystem_name: Subsystem name
    :type subsystem_name: str
    :param subsystem_description: Subsystem description
    :type subsystem_description: str

    :rtype: None
    """
    return 'do some magic!'


def update_support_system(support_system_id, account_id_session, token, support_system_name=None):
    """
    Update support system
    
    :param support_system_id: Support system identifier located in the url path
    :type support_system_id: int
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str
    :param support_system_name: Support system name
    :type support_system_name: str

    :rtype: None
    """
    return 'do some magic!'


def update_support_system_dataclass_matrix(project_id, support_system_dataclass_matrix, account_id_session, token):
    """
    Update support system X dataclass matrix
    
    :param project_id: Project Id
    :type project_id: int
    :param support_system_dataclass_matrix: Support system X dataclass values
    :type support_system_dataclass_matrix: dict | bytes
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    if connexion.request.is_json:
        support_system_dataclass_matrix = SupportSystemDataclassMatrix.from_dict(connexion.request.get_json())
    return 'do some magic!'


def update_support_system_organization_unit_matrix(project_id, support_system_organization_unit_matrix, account_id_session, token):
    """
    Update support system X organization unit matrix
    
    :param project_id: Project Id
    :type project_id: int
    :param support_system_organization_unit_matrix: Support system X organization unit values
    :type support_system_organization_unit_matrix: dict | bytes
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    if connexion.request.is_json:
        support_system_organization_unit_matrix = SupportSystemOrganizationUnitMatrix.from_dict(connexion.request.get_json())
    return 'do some magic!'


def update_support_system_process_matrix(project_id, support_system_process_matrix, account_id_session, token):
    """
    Update support system X process matrix
    
    :param project_id: Project Id
    :type project_id: int
    :param support_system_process_matrix: Support system X process values
    :type support_system_process_matrix: dict | bytes
    :param account_id_session: Account id of the session
    :type account_id_session: int
    :param token: Session token
    :type token: str

    :rtype: None
    """
    if connexion.request.is_json:
        support_system_process_matrix = SupportSystemProcessMatrix.from_dict(connexion.request.get_json())
    return 'do some magic!'
