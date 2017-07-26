"""Generated client library for clouddebugger version v2."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.clouddebugger.v2 import clouddebugger_v2_messages as messages


class ClouddebuggerV2(base_api.BaseApiClient):
  """Generated client library for service clouddebugger version v2."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://clouddebugger.googleapis.com/'

  _PACKAGE = u'clouddebugger'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/cloud_debugger']
  _VERSION = u'v2'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'ClouddebuggerV2'
  _URL_VERSION = u'v2'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new clouddebugger handle."""
    url = url or self.BASE_URL
    super(ClouddebuggerV2, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.controller_debuggees_breakpoints = self.ControllerDebuggeesBreakpointsService(self)
    self.controller_debuggees = self.ControllerDebuggeesService(self)
    self.controller = self.ControllerService(self)
    self.debugger_debuggees_breakpoints = self.DebuggerDebuggeesBreakpointsService(self)
    self.debugger_debuggees = self.DebuggerDebuggeesService(self)
    self.debugger = self.DebuggerService(self)

  class ControllerDebuggeesBreakpointsService(base_api.BaseApiService):
    """Service class for the controller_debuggees_breakpoints resource."""

    _NAME = u'controller_debuggees_breakpoints'

    def __init__(self, client):
      super(ClouddebuggerV2.ControllerDebuggeesBreakpointsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      """Returns the list of all active breakpoints for the debuggee.

The breakpoint specification (`location`, `condition`, and `expressions`
fields) is semantically immutable, although the field values may
change. For example, an agent may update the location line number
to reflect the actual line where the breakpoint was set, but this
doesn't change the breakpoint semantics.

This means that an agent does not need to check if a breakpoint has changed
when it encounters the same breakpoint on a successive call.
Moreover, an agent should remember the breakpoints that are completed
until the controller removes them from the active list to avoid
setting those breakpoints again.

      Args:
        request: (ClouddebuggerControllerDebuggeesBreakpointsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListActiveBreakpointsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'clouddebugger.controller.debuggees.breakpoints.list',
        ordered_params=[u'debuggeeId'],
        path_params=[u'debuggeeId'],
        query_params=[u'successOnTimeout', u'waitToken'],
        relative_path=u'v2/controller/debuggees/{debuggeeId}/breakpoints',
        request_field='',
        request_type_name=u'ClouddebuggerControllerDebuggeesBreakpointsListRequest',
        response_type_name=u'ListActiveBreakpointsResponse',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      """Updates the breakpoint state or mutable fields.
The entire Breakpoint message must be sent back to the controller
service.

Updates to active breakpoint fields are only allowed if the new value
does not change the breakpoint specification. Updates to the `location`,
`condition` and `expressions` fields should not alter the breakpoint
semantics. These may only make changes such as canonicalizing a value
or snapping the location to the correct line of code.

      Args:
        request: (ClouddebuggerControllerDebuggeesBreakpointsUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (UpdateActiveBreakpointResponse) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PUT',
        method_id=u'clouddebugger.controller.debuggees.breakpoints.update',
        ordered_params=[u'debuggeeId', u'id'],
        path_params=[u'debuggeeId', u'id'],
        query_params=[],
        relative_path=u'v2/controller/debuggees/{debuggeeId}/breakpoints/{id}',
        request_field=u'updateActiveBreakpointRequest',
        request_type_name=u'ClouddebuggerControllerDebuggeesBreakpointsUpdateRequest',
        response_type_name=u'UpdateActiveBreakpointResponse',
        supports_download=False,
    )

  class ControllerDebuggeesService(base_api.BaseApiService):
    """Service class for the controller_debuggees resource."""

    _NAME = u'controller_debuggees'

    def __init__(self, client):
      super(ClouddebuggerV2.ControllerDebuggeesService, self).__init__(client)
      self._upload_configs = {
          }

    def Register(self, request, global_params=None):
      """Registers the debuggee with the controller service.

All agents attached to the same application should call this method with
the same request content to get back the same stable `debuggee_id`. Agents
should call this method again whenever `google.rpc.Code.NOT_FOUND` is
returned from any controller method.

This allows the controller service to disable the agent or recover from any
data loss. If the debuggee is disabled by the server, the response will
have `is_disabled` set to `true`.

      Args:
        request: (RegisterDebuggeeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (RegisterDebuggeeResponse) The response message.
      """
      config = self.GetMethodConfig('Register')
      return self._RunMethod(
          config, request, global_params=global_params)

    Register.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'clouddebugger.controller.debuggees.register',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path=u'v2/controller/debuggees/register',
        request_field='<request>',
        request_type_name=u'RegisterDebuggeeRequest',
        response_type_name=u'RegisterDebuggeeResponse',
        supports_download=False,
    )

  class ControllerService(base_api.BaseApiService):
    """Service class for the controller resource."""

    _NAME = u'controller'

    def __init__(self, client):
      super(ClouddebuggerV2.ControllerService, self).__init__(client)
      self._upload_configs = {
          }

  class DebuggerDebuggeesBreakpointsService(base_api.BaseApiService):
    """Service class for the debugger_debuggees_breakpoints resource."""

    _NAME = u'debugger_debuggees_breakpoints'

    def __init__(self, client):
      super(ClouddebuggerV2.DebuggerDebuggeesBreakpointsService, self).__init__(client)
      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      """Deletes the breakpoint from the debuggee.

      Args:
        request: (ClouddebuggerDebuggerDebuggeesBreakpointsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'DELETE',
        method_id=u'clouddebugger.debugger.debuggees.breakpoints.delete',
        ordered_params=[u'debuggeeId', u'breakpointId'],
        path_params=[u'breakpointId', u'debuggeeId'],
        query_params=[u'clientVersion'],
        relative_path=u'v2/debugger/debuggees/{debuggeeId}/breakpoints/{breakpointId}',
        request_field='',
        request_type_name=u'ClouddebuggerDebuggerDebuggeesBreakpointsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets breakpoint information.

      Args:
        request: (ClouddebuggerDebuggerDebuggeesBreakpointsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GetBreakpointResponse) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'clouddebugger.debugger.debuggees.breakpoints.get',
        ordered_params=[u'debuggeeId', u'breakpointId'],
        path_params=[u'breakpointId', u'debuggeeId'],
        query_params=[u'clientVersion'],
        relative_path=u'v2/debugger/debuggees/{debuggeeId}/breakpoints/{breakpointId}',
        request_field='',
        request_type_name=u'ClouddebuggerDebuggerDebuggeesBreakpointsGetRequest',
        response_type_name=u'GetBreakpointResponse',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists all breakpoints for the debuggee.

      Args:
        request: (ClouddebuggerDebuggerDebuggeesBreakpointsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListBreakpointsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'clouddebugger.debugger.debuggees.breakpoints.list',
        ordered_params=[u'debuggeeId'],
        path_params=[u'debuggeeId'],
        query_params=[u'action_value', u'clientVersion', u'includeAllUsers', u'includeInactive', u'stripResults', u'waitToken'],
        relative_path=u'v2/debugger/debuggees/{debuggeeId}/breakpoints',
        request_field='',
        request_type_name=u'ClouddebuggerDebuggerDebuggeesBreakpointsListRequest',
        response_type_name=u'ListBreakpointsResponse',
        supports_download=False,
    )

    def Set(self, request, global_params=None):
      """Sets the breakpoint to the debuggee.

      Args:
        request: (ClouddebuggerDebuggerDebuggeesBreakpointsSetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SetBreakpointResponse) The response message.
      """
      config = self.GetMethodConfig('Set')
      return self._RunMethod(
          config, request, global_params=global_params)

    Set.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'clouddebugger.debugger.debuggees.breakpoints.set',
        ordered_params=[u'debuggeeId'],
        path_params=[u'debuggeeId'],
        query_params=[u'clientVersion'],
        relative_path=u'v2/debugger/debuggees/{debuggeeId}/breakpoints/set',
        request_field=u'breakpoint',
        request_type_name=u'ClouddebuggerDebuggerDebuggeesBreakpointsSetRequest',
        response_type_name=u'SetBreakpointResponse',
        supports_download=False,
    )

  class DebuggerDebuggeesService(base_api.BaseApiService):
    """Service class for the debugger_debuggees resource."""

    _NAME = u'debugger_debuggees'

    def __init__(self, client):
      super(ClouddebuggerV2.DebuggerDebuggeesService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      """Lists all the debuggees that the user can set breakpoints to.

      Args:
        request: (ClouddebuggerDebuggerDebuggeesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListDebuggeesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'clouddebugger.debugger.debuggees.list',
        ordered_params=[],
        path_params=[],
        query_params=[u'clientVersion', u'includeInactive', u'project'],
        relative_path=u'v2/debugger/debuggees',
        request_field='',
        request_type_name=u'ClouddebuggerDebuggerDebuggeesListRequest',
        response_type_name=u'ListDebuggeesResponse',
        supports_download=False,
    )

  class DebuggerService(base_api.BaseApiService):
    """Service class for the debugger resource."""

    _NAME = u'debugger'

    def __init__(self, client):
      super(ClouddebuggerV2.DebuggerService, self).__init__(client)
      self._upload_configs = {
          }
