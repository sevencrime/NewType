#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-15 10:03:05
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import requests

url = 'https://cognito-idp.ap-southeast-1.amazonaws.com/'
headers = {
    'content_type' : 'application/x-amz-json-1.0'
}

data = {
    "ChallengeName": "PASSWORD_VERIFIER",
    "ClientId": "513jfcktr1m6evogfqu7osk7pa",
    "ChallengeResponses": {
        "USERNAME": "sales_t1",
        "PASSWORD_CLAIM_SECRET_BLOCK": "IhZpF0pO7UfHHJlVm1i7/1ze7NEHBvOwLup17hucx36xMQg14lKSdakhr1/F6TEdnXSVLMsjJib7qdTelr7obvQZo3hdeWvb+oqc2LzcmH2UdsZdTrzGIjQ6ebQX2MHd46JIs7S4SnusstVh+qHhj2URz/tbQO14QGXdZXZw/AR5N54jn1XZD1boHO2p+8vku3xpifo4a9iNNMTUtYzp1AqBKuX1qOvpupY3xZxCwyzV95s+hVXKJFmlcth/mWl855EY6Gzu3n9buMH3ZLhVD7AV6YFzfOP7zHwMYBwouQI8QP9sUS1t9Bvn1vKX0gtACK0ILIBc1f4zAUjgZbQiJG1286cQCDhluxPUuD8yRfJRJ5T5ot+wpY+d00lp7BCB3+nHYpgQXyg1uNAKzW+RyuuOZX2ZdUMiQn+bC4htbM1jpDpaz5CjHOUauxoD2qVCsqMaXrssxBA4trFv99q4zxfAhr1YKrYICpb3WFs4QknA1xbxdEpK6rpEDqWwFXyiTFPIxBVV87gpCuAZGH4yopklcWy19x/SxmOXUq9v6bD9uMvc4CidQJ6M6Al3uWYeIThM63uBCNrxBt/M5EHdUqkjL67h7VDL7yzhfEB5CkedmazEIHxUJ9UMMeH+RSaZ+bt47ZlRR6nkrz/Iikc40ft3LdMdgte+mEAa7oGBGOz9hAatZHAR1f5bedPIAr8nk8dpl8Ur/KMCm+bpHyOtjzOPP6J9glNLLFCn5xBHAIlKsuw4lmIilEes76xgaKq2h+7w9mh1Y4n8zmJGX0RBlXUnHcO/1Q9tJU1FMRx+bH+apUG2/xcGzosKWos8rqczQ1R1bbCeOQXgCw7Nv0QJZUeLZXa+sTfjCwPKjNBvXEjdFtJeUn7Lw+YGuz/qIyjoHqvSOiJvMfL7SGa739aSYH+FKPZJ1eFCvPa82PV+tefIxWps0A03noXPQn3jwWF4eoW5CBo0QWaixUze8c5C8A2LWaCqlOxRPiGn/MMljRl9EKunp6MA0ss7kP0hS81AaA8POpKE/WjTsMsY52f+D9HILLM3ywYLeyEEKxJ1kpkgLSSmTxKwrhVAxObxcniCpP4Jdqu1vwtByv/Xw92zs1LypZXKYiod3YrtZ5sj6B7cHc0TfremxpVFz+OMUJSnUVRRmFhXpZmmbDgWsPuTwSoY61pdiiLFPQ5vaksl02BXzEqr2imiBQOMT3sxVS0zQEzOCn4bq0ZMaUZ2qOwBDuruMk8cDNbYs0NkCT/YhGJOJjJaL99UWXQHg8XLAVBwiCcXSvr8yFYTWT2cPtaJwst3hmZID3ttcJyEaCyA254OtmQjOOhFUjMrlqWq4wwL/BkHrHisBxGsP9qNi+bLjvrqUap4T4lwrRYjm7Bx2k3TDp8s+4E2B0krZO2hwYuZ1ILnFGTTZzFYulcsXCobqidEIKZbvqZuG80Kj+BhcKNBlZezdgKwdJ1a2fg5AgEnhmmgO2EuvzC7QHM3HBgyIqqhwngQQbwIDRjTmEX+i/nTT6lpv76J8MxDvmKkQAVgr7wSShWnqoOy+VAE1CvAjTQcFWk9tqe7s6z0Swg3MbHTHUW72Ytko1do+bu+XvudMrRe5ItY/1h7QkhKo6j+OhtmRZKteMInc6Z9YlM/wLWgv/yoswZPXUC7hss15L266FUpSbypWFtBdkgiicbr9LKCbM+Ig06xz3C22v/oUehccqKzPsWtq8Kjx5o=",
        "TIMESTAMP": "Fri Feb 15 10:39:21 UTC 2019",
        "PASSWORD_CLAIM_SIGNATURE": "zPvLiDASRbLbhC5r6Jo5pl3FBMiE1mHWbSngY8Qan4I="
    }
}
resp = requests.post(url, params=data, headers=headers)
print(resp)
print(resp.json())
