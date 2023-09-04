# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "site-recovery protectable-item show",
)
class Show(AAZCommand):
    """Get operation to get the details of a protectable item.

    :example: protectable-item show
        az site-recovery protectable-item show --fabric-name "fabric" --protection-container "container_name" -g "rg_name" --vault-name "vault_name" -n "protectable_item_name"
    """

    _aaz_info = {
        "version": "2022-08-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.recoveryservices/vaults/{}/replicationfabrics/{}/replicationprotectioncontainers/{}/replicationprotectableitems/{}", "2022-08-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.fabric_name = AAZStrArg(
            options=["--fabric-name"],
            help="Fabric name.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.protectable_item_name = AAZStrArg(
            options=["-n", "--name", "--protectable-item-name"],
            help="Protectable item name.",
            required=True,
            id_part="child_name_3",
        )
        _args_schema.protection_container_name = AAZStrArg(
            options=["--protection-container", "--protection-container-name"],
            help="Protection container name.",
            required=True,
            id_part="child_name_2",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.vault_name = AAZStrArg(
            options=["--vault-name"],
            help="The name of the recovery services vault.",
            required=True,
            id_part="name",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ReplicationProtectableItemsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ReplicationProtectableItemsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectableItems/{protectableItemName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "fabricName", self.ctx.args.fabric_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "protectableItemName", self.ctx.args.protectable_item_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "protectionContainerName", self.ctx.args.protection_container_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceName", self.ctx.args.vault_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-08-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType()
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.custom_details = AAZObjectType(
                serialized_name="customDetails",
            )
            properties.friendly_name = AAZStrType(
                serialized_name="friendlyName",
            )
            properties.protection_readiness_errors = AAZListType(
                serialized_name="protectionReadinessErrors",
            )
            properties.protection_status = AAZStrType(
                serialized_name="protectionStatus",
            )
            properties.recovery_services_provider_id = AAZStrType(
                serialized_name="recoveryServicesProviderId",
            )
            properties.replication_protected_item_id = AAZStrType(
                serialized_name="replicationProtectedItemId",
            )
            properties.supported_replication_providers = AAZListType(
                serialized_name="supportedReplicationProviders",
            )

            custom_details = cls._schema_on_200.properties.custom_details
            custom_details.instance_type = AAZStrType(
                serialized_name="instanceType",
                flags={"required": True},
            )

            disc_hyper_v_virtual_machine = cls._schema_on_200.properties.custom_details.discriminate_by("instance_type", "HyperVVirtualMachine")
            disc_hyper_v_virtual_machine.disk_details = AAZListType(
                serialized_name="diskDetails",
            )
            disc_hyper_v_virtual_machine.generation = AAZStrType()
            disc_hyper_v_virtual_machine.has_fibre_channel_adapter = AAZStrType(
                serialized_name="hasFibreChannelAdapter",
            )
            disc_hyper_v_virtual_machine.has_physical_disk = AAZStrType(
                serialized_name="hasPhysicalDisk",
            )
            disc_hyper_v_virtual_machine.has_shared_vhd = AAZStrType(
                serialized_name="hasSharedVhd",
            )
            disc_hyper_v_virtual_machine.hyper_v_host_id = AAZStrType(
                serialized_name="hyperVHostId",
            )
            disc_hyper_v_virtual_machine.os_details = AAZObjectType(
                serialized_name="osDetails",
            )
            _ShowHelper._build_schema_os_details_read(disc_hyper_v_virtual_machine.os_details)
            disc_hyper_v_virtual_machine.source_item_id = AAZStrType(
                serialized_name="sourceItemId",
            )

            disk_details = cls._schema_on_200.properties.custom_details.discriminate_by("instance_type", "HyperVVirtualMachine").disk_details
            disk_details.Element = AAZObjectType()
            _ShowHelper._build_schema_disk_details_read(disk_details.Element)

            disc_v_mware_virtual_machine = cls._schema_on_200.properties.custom_details.discriminate_by("instance_type", "VMwareVirtualMachine")
            disc_v_mware_virtual_machine.agent_generated_id = AAZStrType(
                serialized_name="agentGeneratedId",
            )
            disc_v_mware_virtual_machine.agent_installed = AAZStrType(
                serialized_name="agentInstalled",
            )
            disc_v_mware_virtual_machine.agent_version = AAZStrType(
                serialized_name="agentVersion",
            )
            disc_v_mware_virtual_machine.discovery_type = AAZStrType(
                serialized_name="discoveryType",
            )
            disc_v_mware_virtual_machine.disk_details = AAZListType(
                serialized_name="diskDetails",
            )
            disc_v_mware_virtual_machine.ip_address = AAZStrType(
                serialized_name="ipAddress",
            )
            disc_v_mware_virtual_machine.os_type = AAZStrType(
                serialized_name="osType",
            )
            disc_v_mware_virtual_machine.powered_on = AAZStrType(
                serialized_name="poweredOn",
            )
            disc_v_mware_virtual_machine.v_center_infrastructure_id = AAZStrType(
                serialized_name="vCenterInfrastructureId",
            )
            disc_v_mware_virtual_machine.validation_errors = AAZListType(
                serialized_name="validationErrors",
            )

            disk_details = cls._schema_on_200.properties.custom_details.discriminate_by("instance_type", "VMwareVirtualMachine").disk_details
            disk_details.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.custom_details.discriminate_by("instance_type", "VMwareVirtualMachine").disk_details.Element
            _element.disk_configuration = AAZStrType(
                serialized_name="diskConfiguration",
            )
            _element.disk_id = AAZStrType(
                serialized_name="diskId",
            )
            _element.disk_name = AAZStrType(
                serialized_name="diskName",
            )
            _element.disk_size_in_mb = AAZStrType(
                serialized_name="diskSizeInMB",
            )
            _element.disk_type = AAZStrType(
                serialized_name="diskType",
            )
            _element.volume_list = AAZListType(
                serialized_name="volumeList",
            )

            volume_list = cls._schema_on_200.properties.custom_details.discriminate_by("instance_type", "VMwareVirtualMachine").disk_details.Element.volume_list
            volume_list.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.custom_details.discriminate_by("instance_type", "VMwareVirtualMachine").disk_details.Element.volume_list.Element
            _element.label = AAZStrType()
            _element.name = AAZStrType()

            validation_errors = cls._schema_on_200.properties.custom_details.discriminate_by("instance_type", "VMwareVirtualMachine").validation_errors
            validation_errors.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.custom_details.discriminate_by("instance_type", "VMwareVirtualMachine").validation_errors.Element
            _element.creation_time_utc = AAZStrType(
                serialized_name="creationTimeUtc",
            )
            _element.customer_resolvability = AAZStrType(
                serialized_name="customerResolvability",
            )
            _element.entity_id = AAZStrType(
                serialized_name="entityId",
            )
            _element.error_category = AAZStrType(
                serialized_name="errorCategory",
            )
            _element.error_code = AAZStrType(
                serialized_name="errorCode",
            )
            _element.error_id = AAZStrType(
                serialized_name="errorId",
            )
            _element.error_level = AAZStrType(
                serialized_name="errorLevel",
            )
            _element.error_message = AAZStrType(
                serialized_name="errorMessage",
            )
            _element.error_source = AAZStrType(
                serialized_name="errorSource",
            )
            _element.error_type = AAZStrType(
                serialized_name="errorType",
            )
            _element.inner_health_errors = AAZListType(
                serialized_name="innerHealthErrors",
            )
            _element.possible_causes = AAZStrType(
                serialized_name="possibleCauses",
            )
            _element.recommended_action = AAZStrType(
                serialized_name="recommendedAction",
            )
            _element.recovery_provider_error_message = AAZStrType(
                serialized_name="recoveryProviderErrorMessage",
            )
            _element.summary_message = AAZStrType(
                serialized_name="summaryMessage",
            )

            inner_health_errors = cls._schema_on_200.properties.custom_details.discriminate_by("instance_type", "VMwareVirtualMachine").validation_errors.Element.inner_health_errors
            inner_health_errors.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.custom_details.discriminate_by("instance_type", "VMwareVirtualMachine").validation_errors.Element.inner_health_errors.Element
            _element.creation_time_utc = AAZStrType(
                serialized_name="creationTimeUtc",
            )
            _element.customer_resolvability = AAZStrType(
                serialized_name="customerResolvability",
            )
            _element.entity_id = AAZStrType(
                serialized_name="entityId",
            )
            _element.error_category = AAZStrType(
                serialized_name="errorCategory",
            )
            _element.error_code = AAZStrType(
                serialized_name="errorCode",
            )
            _element.error_id = AAZStrType(
                serialized_name="errorId",
            )
            _element.error_level = AAZStrType(
                serialized_name="errorLevel",
            )
            _element.error_message = AAZStrType(
                serialized_name="errorMessage",
            )
            _element.error_source = AAZStrType(
                serialized_name="errorSource",
            )
            _element.error_type = AAZStrType(
                serialized_name="errorType",
            )
            _element.possible_causes = AAZStrType(
                serialized_name="possibleCauses",
            )
            _element.recommended_action = AAZStrType(
                serialized_name="recommendedAction",
            )
            _element.recovery_provider_error_message = AAZStrType(
                serialized_name="recoveryProviderErrorMessage",
            )
            _element.summary_message = AAZStrType(
                serialized_name="summaryMessage",
            )

            disc_vmm_virtual_machine = cls._schema_on_200.properties.custom_details.discriminate_by("instance_type", "VmmVirtualMachine")
            disc_vmm_virtual_machine.disk_details = AAZListType(
                serialized_name="diskDetails",
            )
            disc_vmm_virtual_machine.generation = AAZStrType()
            disc_vmm_virtual_machine.has_fibre_channel_adapter = AAZStrType(
                serialized_name="hasFibreChannelAdapter",
            )
            disc_vmm_virtual_machine.has_physical_disk = AAZStrType(
                serialized_name="hasPhysicalDisk",
            )
            disc_vmm_virtual_machine.has_shared_vhd = AAZStrType(
                serialized_name="hasSharedVhd",
            )
            disc_vmm_virtual_machine.hyper_v_host_id = AAZStrType(
                serialized_name="hyperVHostId",
            )
            disc_vmm_virtual_machine.os_details = AAZObjectType(
                serialized_name="osDetails",
            )
            _ShowHelper._build_schema_os_details_read(disc_vmm_virtual_machine.os_details)
            disc_vmm_virtual_machine.source_item_id = AAZStrType(
                serialized_name="sourceItemId",
            )

            disk_details = cls._schema_on_200.properties.custom_details.discriminate_by("instance_type", "VmmVirtualMachine").disk_details
            disk_details.Element = AAZObjectType()
            _ShowHelper._build_schema_disk_details_read(disk_details.Element)

            protection_readiness_errors = cls._schema_on_200.properties.protection_readiness_errors
            protection_readiness_errors.Element = AAZStrType()

            supported_replication_providers = cls._schema_on_200.properties.supported_replication_providers
            supported_replication_providers.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_disk_details_read = None

    @classmethod
    def _build_schema_disk_details_read(cls, _schema):
        if cls._schema_disk_details_read is not None:
            _schema.max_size_mb = cls._schema_disk_details_read.max_size_mb
            _schema.vhd_id = cls._schema_disk_details_read.vhd_id
            _schema.vhd_name = cls._schema_disk_details_read.vhd_name
            _schema.vhd_type = cls._schema_disk_details_read.vhd_type
            return

        cls._schema_disk_details_read = _schema_disk_details_read = AAZObjectType()

        disk_details_read = _schema_disk_details_read
        disk_details_read.max_size_mb = AAZIntType(
            serialized_name="maxSizeMB",
        )
        disk_details_read.vhd_id = AAZStrType(
            serialized_name="vhdId",
        )
        disk_details_read.vhd_name = AAZStrType(
            serialized_name="vhdName",
        )
        disk_details_read.vhd_type = AAZStrType(
            serialized_name="vhdType",
        )

        _schema.max_size_mb = cls._schema_disk_details_read.max_size_mb
        _schema.vhd_id = cls._schema_disk_details_read.vhd_id
        _schema.vhd_name = cls._schema_disk_details_read.vhd_name
        _schema.vhd_type = cls._schema_disk_details_read.vhd_type

    _schema_os_details_read = None

    @classmethod
    def _build_schema_os_details_read(cls, _schema):
        if cls._schema_os_details_read is not None:
            _schema.o_s_major_version = cls._schema_os_details_read.o_s_major_version
            _schema.o_s_minor_version = cls._schema_os_details_read.o_s_minor_version
            _schema.o_s_version = cls._schema_os_details_read.o_s_version
            _schema.os_edition = cls._schema_os_details_read.os_edition
            _schema.os_type = cls._schema_os_details_read.os_type
            _schema.product_type = cls._schema_os_details_read.product_type
            return

        cls._schema_os_details_read = _schema_os_details_read = AAZObjectType()

        os_details_read = _schema_os_details_read
        os_details_read.o_s_major_version = AAZStrType(
            serialized_name="oSMajorVersion",
        )
        os_details_read.o_s_minor_version = AAZStrType(
            serialized_name="oSMinorVersion",
        )
        os_details_read.o_s_version = AAZStrType(
            serialized_name="oSVersion",
        )
        os_details_read.os_edition = AAZStrType(
            serialized_name="osEdition",
        )
        os_details_read.os_type = AAZStrType(
            serialized_name="osType",
        )
        os_details_read.product_type = AAZStrType(
            serialized_name="productType",
        )

        _schema.o_s_major_version = cls._schema_os_details_read.o_s_major_version
        _schema.o_s_minor_version = cls._schema_os_details_read.o_s_minor_version
        _schema.o_s_version = cls._schema_os_details_read.o_s_version
        _schema.os_edition = cls._schema_os_details_read.os_edition
        _schema.os_type = cls._schema_os_details_read.os_type
        _schema.product_type = cls._schema_os_details_read.product_type


__all__ = ["Show"]
