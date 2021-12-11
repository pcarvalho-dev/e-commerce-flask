from application.services.http_status import code_http, code_message
from application.services.pagination import pagination_info


def default_return(status=200, message=2, data={}, items_paginate={}, summary={}):
    pagination = pagination_info(items_paginate)

    return {
               "status": code_http(status), "msg": code_message(message), "pagination": pagination,
               "summary": summary, "data": data
           }, status, {'Content-Type': 'application/json'}
