from __future__ import annotations

from typing import Any

from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.arm.base_resource_check import BaseResourceCheck


class ACRContainerScanEnabled(BaseResourceCheck):
    SKUS = {"Standard", "Premium"}  # noqa: CCE003  # a static attribute

    def __init__(self) -> None:
        name = "Enable vulnerability scanning for container images."
        id = "CKV_AZURE_163"
        supported_resources = ("Microsoft.ContainerRegistry/registries",)
        categories = (CheckCategories.GENERAL_SECURITY,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf: dict[str, list[Any]]) -> CheckResult:

        if "sku" in conf.keys():
            sku = conf.get("sku")

        if (
                "name" in sku
                and isinstance(sku["name"], str)
                and sku["name"] in ACRContainerScanEnabled.SKUS
        ):
            return CheckResult.PASSED

        return CheckResult.FAILED


check = ACRContainerScanEnabled()
