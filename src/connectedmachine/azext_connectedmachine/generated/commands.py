# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
# pylint: disable=bad-continuation
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType
from azext_connectedmachine.generated._client_factory import (
    cf_machine,
    cf_machine_extension,
    cf_connectedmachine_cl,
    cf_private_link_scope,
    cf_private_link_resource,
    cf_private_endpoint_connection,
)


connectedmachine_private_link_scope = CliCommandType(
    operations_tmpl='azext_connectedmachine.vendored_sdks.connectedmachine.operations._private_link_scopes_operations#PrivateLinkScopesOperations.{}',
    client_factory=cf_private_link_scope,
)


def load_command_table(self, _):
    with self.command_group(
        'connectedmachine private-link-scope', connectedmachine_private_link_scope, client_factory=cf_private_link_scope
    ) as g:
        g.custom_command('update-tag', 'connectedmachine_private_link_scope_update_tag')
