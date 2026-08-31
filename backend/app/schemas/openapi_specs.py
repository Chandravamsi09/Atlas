"""\nComprehensive Pydantic v2 OpenAPI Schemas, Data Validation Models, and Serializers.\nCovers all multi-tenant endpoints, parameter bounds, error responses, and payload schemas.\n"""\n
from typing import List, Dict, Any, Optional, Union, Literal\n
from pydantic import BaseModel, Field, EmailStr, HttpUrl\n
from datetime import datetime\n

class TenantOrganizationProfileV1(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #1)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=1, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0001",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #1",
                    "version": 1,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV2(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #2)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=2, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0002",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #2",
                    "version": 2,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV3(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #3)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=3, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0003",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #3",
                    "version": 3,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV4(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #4)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=4, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0004",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #4",
                    "version": 4,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV5(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #5)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=5, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0005",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #5",
                    "version": 5,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV6(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #6)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=6, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0006",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #6",
                    "version": 6,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV7(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #7)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=7, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0007",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #7",
                    "version": 7,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV8(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #8)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=8, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0008",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #8",
                    "version": 8,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV9(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #9)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=9, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0009",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #9",
                    "version": 9,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV10(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #10)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=10, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0010",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #10",
                    "version": 10,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV11(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #11)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=11, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0011",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #11",
                    "version": 11,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV12(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #12)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=12, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0012",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #12",
                    "version": 12,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV13(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #13)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=13, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0013",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #13",
                    "version": 13,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV14(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #14)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=14, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0014",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #14",
                    "version": 14,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV15(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #15)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=15, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0015",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #15",
                    "version": 15,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV16(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #16)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=16, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0016",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #16",
                    "version": 16,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV17(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #17)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=17, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0017",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #17",
                    "version": 17,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV18(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #18)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=18, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0018",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #18",
                    "version": 18,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV19(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #19)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=19, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0019",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #19",
                    "version": 19,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV20(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #20)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=20, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0020",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #20",
                    "version": 20,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV21(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #21)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=21, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0021",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #21",
                    "version": 21,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV22(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #22)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=22, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0022",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #22",
                    "version": 22,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV23(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #23)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=23, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0023",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #23",
                    "version": 23,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TenantOrganizationProfileV24(BaseModel):
    """Schema definition for organization hierarchies, billing account tiers, and SSO metadata (Profile Tier #24)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=24, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0024",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TenantOrganization Profile #24",
                    "version": 24,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV1(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #1)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=1, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0001",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #1",
                    "version": 1,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV2(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #2)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=2, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0002",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #2",
                    "version": 2,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV3(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #3)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=3, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0003",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #3",
                    "version": 3,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV4(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #4)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=4, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0004",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #4",
                    "version": 4,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV5(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #5)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=5, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0005",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #5",
                    "version": 5,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV6(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #6)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=6, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0006",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #6",
                    "version": 6,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV7(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #7)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=7, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0007",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #7",
                    "version": 7,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV8(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #8)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=8, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0008",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #8",
                    "version": 8,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV9(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #9)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=9, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0009",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #9",
                    "version": 9,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV10(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #10)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=10, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0010",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #10",
                    "version": 10,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV11(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #11)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=11, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0011",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #11",
                    "version": 11,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV12(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #12)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=12, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0012",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #12",
                    "version": 12,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV13(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #13)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=13, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0013",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #13",
                    "version": 13,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV14(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #14)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=14, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0014",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #14",
                    "version": 14,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV15(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #15)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=15, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0015",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #15",
                    "version": 15,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV16(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #16)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=16, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0016",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #16",
                    "version": 16,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV17(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #17)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=17, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0017",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #17",
                    "version": 17,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV18(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #18)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=18, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0018",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #18",
                    "version": 18,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV19(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #19)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=19, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0019",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #19",
                    "version": 19,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV20(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #20)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=20, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0020",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #20",
                    "version": 20,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV21(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #21)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=21, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0021",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #21",
                    "version": 21,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV22(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #22)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=22, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0022",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #22",
                    "version": 22,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV23(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #23)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=23, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0023",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #23",
                    "version": 23,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class ModelEndpointConfigProfileV24(BaseModel):
    """Schema definition for downstream LLM provider credentials, timeout configs, and retry parameters (Profile Tier #24)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=24, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0024",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production ModelEndpointConfig Profile #24",
                    "version": 24,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV1(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #1)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=1, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0001",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #1",
                    "version": 1,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV2(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #2)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=2, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0002",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #2",
                    "version": 2,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV3(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #3)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=3, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0003",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #3",
                    "version": 3,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV4(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #4)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=4, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0004",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #4",
                    "version": 4,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV5(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #5)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=5, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0005",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #5",
                    "version": 5,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV6(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #6)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=6, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0006",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #6",
                    "version": 6,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV7(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #7)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=7, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0007",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #7",
                    "version": 7,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV8(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #8)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=8, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0008",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #8",
                    "version": 8,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV9(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #9)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=9, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0009",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #9",
                    "version": 9,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV10(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #10)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=10, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0010",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #10",
                    "version": 10,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV11(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #11)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=11, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0011",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #11",
                    "version": 11,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV12(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #12)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=12, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0012",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #12",
                    "version": 12,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV13(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #13)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=13, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0013",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #13",
                    "version": 13,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV14(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #14)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=14, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0014",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #14",
                    "version": 14,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV15(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #15)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=15, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0015",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #15",
                    "version": 15,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV16(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #16)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=16, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0016",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #16",
                    "version": 16,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV17(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #17)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=17, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0017",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #17",
                    "version": 17,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV18(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #18)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=18, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0018",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #18",
                    "version": 18,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV19(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #19)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=19, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0019",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #19",
                    "version": 19,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV20(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #20)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=20, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0020",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #20",
                    "version": 20,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV21(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #21)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=21, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0021",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #21",
                    "version": 21,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV22(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #22)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=22, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0022",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #22",
                    "version": 22,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV23(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #23)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=23, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0023",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #23",
                    "version": 23,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class PromptTemplateSchemaProfileV24(BaseModel):
    """Schema definition for Jinja2 prompt definitions, parameter constraints, and canary splits (Profile Tier #24)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=24, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0024",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production PromptTemplateSchema Profile #24",
                    "version": 24,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV1(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #1)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=1, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0001",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #1",
                    "version": 1,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV2(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #2)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=2, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0002",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #2",
                    "version": 2,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV3(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #3)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=3, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0003",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #3",
                    "version": 3,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV4(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #4)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=4, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0004",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #4",
                    "version": 4,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV5(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #5)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=5, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0005",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #5",
                    "version": 5,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV6(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #6)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=6, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0006",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #6",
                    "version": 6,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV7(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #7)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=7, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0007",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #7",
                    "version": 7,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV8(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #8)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=8, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0008",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #8",
                    "version": 8,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV9(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #9)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=9, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0009",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #9",
                    "version": 9,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV10(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #10)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=10, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0010",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #10",
                    "version": 10,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV11(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #11)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=11, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0011",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #11",
                    "version": 11,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV12(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #12)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=12, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0012",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #12",
                    "version": 12,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV13(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #13)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=13, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0013",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #13",
                    "version": 13,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV14(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #14)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=14, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0014",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #14",
                    "version": 14,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV15(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #15)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=15, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0015",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #15",
                    "version": 15,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV16(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #16)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=16, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0016",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #16",
                    "version": 16,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV17(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #17)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=17, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0017",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #17",
                    "version": 17,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV18(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #18)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=18, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0018",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #18",
                    "version": 18,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV19(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #19)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=19, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0019",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #19",
                    "version": 19,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV20(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #20)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=20, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0020",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #20",
                    "version": 20,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV21(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #21)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=21, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0021",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #21",
                    "version": 21,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV22(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #22)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=22, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0022",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #22",
                    "version": 22,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV23(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #23)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=23, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0023",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #23",
                    "version": 23,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class WorkflowDAGDefinitionProfileV24(BaseModel):
    """Schema definition for directed acyclic graph nodes, edge transition rules, and state schemas (Profile Tier #24)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=24, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0024",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production WorkflowDAGDefinition Profile #24",
                    "version": 24,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV1(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #1)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=1, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0001",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #1",
                    "version": 1,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV2(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #2)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=2, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0002",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #2",
                    "version": 2,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV3(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #3)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=3, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0003",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #3",
                    "version": 3,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV4(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #4)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=4, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0004",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #4",
                    "version": 4,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV5(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #5)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=5, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0005",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #5",
                    "version": 5,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV6(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #6)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=6, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0006",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #6",
                    "version": 6,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV7(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #7)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=7, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0007",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #7",
                    "version": 7,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV8(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #8)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=8, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0008",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #8",
                    "version": 8,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV9(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #9)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=9, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0009",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #9",
                    "version": 9,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV10(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #10)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=10, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0010",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #10",
                    "version": 10,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV11(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #11)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=11, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0011",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #11",
                    "version": 11,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV12(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #12)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=12, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0012",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #12",
                    "version": 12,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV13(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #13)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=13, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0013",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #13",
                    "version": 13,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV14(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #14)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=14, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0014",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #14",
                    "version": 14,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV15(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #15)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=15, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0015",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #15",
                    "version": 15,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV16(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #16)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=16, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0016",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #16",
                    "version": 16,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV17(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #17)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=17, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0017",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #17",
                    "version": 17,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV18(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #18)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=18, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0018",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #18",
                    "version": 18,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV19(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #19)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=19, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0019",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #19",
                    "version": 19,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV20(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #20)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=20, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0020",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #20",
                    "version": 20,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV21(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #21)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=21, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0021",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #21",
                    "version": 21,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV22(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #22)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=22, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0022",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #22",
                    "version": 22,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV23(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #23)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=23, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0023",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #23",
                    "version": 23,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class KnowledgeIndexConfigProfileV24(BaseModel):
    """Schema definition for dense HNSW vector parameters, BM25 tokenizer configs, and chunking boundaries (Profile Tier #24)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=24, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0024",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production KnowledgeIndexConfig Profile #24",
                    "version": 24,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV1(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #1)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=1, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0001",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #1",
                    "version": 1,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV2(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #2)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=2, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0002",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #2",
                    "version": 2,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV3(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #3)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=3, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0003",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #3",
                    "version": 3,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV4(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #4)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=4, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0004",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #4",
                    "version": 4,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV5(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #5)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=5, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0005",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #5",
                    "version": 5,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV6(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #6)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=6, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0006",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #6",
                    "version": 6,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV7(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #7)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=7, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0007",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #7",
                    "version": 7,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV8(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #8)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=8, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0008",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #8",
                    "version": 8,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV9(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #9)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=9, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0009",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #9",
                    "version": 9,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV10(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #10)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=10, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0010",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #10",
                    "version": 10,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV11(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #11)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=11, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0011",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #11",
                    "version": 11,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV12(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #12)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=12, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0012",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #12",
                    "version": 12,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV13(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #13)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=13, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0013",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #13",
                    "version": 13,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV14(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #14)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=14, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0014",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #14",
                    "version": 14,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV15(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #15)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=15, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0015",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #15",
                    "version": 15,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV16(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #16)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=16, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0016",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #16",
                    "version": 16,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV17(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #17)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=17, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0017",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #17",
                    "version": 17,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV18(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #18)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=18, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0018",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #18",
                    "version": 18,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV19(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #19)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=19, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0019",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #19",
                    "version": 19,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV20(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #20)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=20, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0020",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #20",
                    "version": 20,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV21(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #21)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=21, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0021",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #21",
                    "version": 21,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV22(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #22)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=22, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0022",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #22",
                    "version": 22,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV23(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #23)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=23, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0023",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #23",
                    "version": 23,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class GuardrailPolicyRuleProfileV24(BaseModel):
    """Schema definition for PII redaction patterns, adversarial injection thresholds, and toxicity bounds (Profile Tier #24)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=24, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0024",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production GuardrailPolicyRule Profile #24",
                    "version": 24,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV1(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #1)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=1, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0001",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #1",
                    "version": 1,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV2(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #2)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=2, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0002",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #2",
                    "version": 2,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV3(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #3)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=3, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0003",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #3",
                    "version": 3,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV4(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #4)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=4, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0004",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #4",
                    "version": 4,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV5(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #5)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=5, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0005",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #5",
                    "version": 5,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV6(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #6)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=6, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0006",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #6",
                    "version": 6,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV7(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #7)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=7, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0007",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #7",
                    "version": 7,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV8(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #8)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=8, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0008",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #8",
                    "version": 8,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV9(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #9)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=9, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0009",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #9",
                    "version": 9,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV10(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #10)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=10, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0010",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #10",
                    "version": 10,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV11(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #11)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=11, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0011",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #11",
                    "version": 11,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV12(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #12)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=12, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0012",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #12",
                    "version": 12,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV13(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #13)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=13, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0013",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #13",
                    "version": 13,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV14(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #14)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=14, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0014",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #14",
                    "version": 14,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV15(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #15)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=15, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0015",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #15",
                    "version": 15,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV16(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #16)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=16, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0016",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #16",
                    "version": 16,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV17(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #17)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=17, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0017",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #17",
                    "version": 17,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV18(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #18)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=18, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0018",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #18",
                    "version": 18,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV19(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #19)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=19, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0019",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #19",
                    "version": 19,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV20(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #20)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=20, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0020",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #20",
                    "version": 20,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV21(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #21)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=21, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0021",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #21",
                    "version": 21,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV22(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #22)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=22, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0022",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #22",
                    "version": 22,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV23(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #23)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=23, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0023",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #23",
                    "version": 23,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class EvaluationBenchmarkRunProfileV24(BaseModel):
    """Schema definition for LLM-as-a-Judge rubrics, RAG Triad faithfulness criteria, and scores (Profile Tier #24)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=24, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0024",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production EvaluationBenchmarkRun Profile #24",
                    "version": 24,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV1(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #1)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=1, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0001",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #1",
                    "version": 1,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV2(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #2)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=2, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0002",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #2",
                    "version": 2,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV3(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #3)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=3, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0003",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #3",
                    "version": 3,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV4(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #4)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=4, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0004",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #4",
                    "version": 4,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV5(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #5)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=5, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0005",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #5",
                    "version": 5,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV6(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #6)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=6, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0006",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #6",
                    "version": 6,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV7(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #7)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=7, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0007",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #7",
                    "version": 7,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV8(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #8)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=8, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0008",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #8",
                    "version": 8,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV9(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #9)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=9, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0009",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #9",
                    "version": 9,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV10(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #10)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=10, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0010",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #10",
                    "version": 10,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV11(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #11)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=11, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0011",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #11",
                    "version": 11,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV12(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #12)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=12, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0012",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #12",
                    "version": 12,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV13(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #13)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=13, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0013",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #13",
                    "version": 13,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV14(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #14)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=14, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0014",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #14",
                    "version": 14,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV15(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #15)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=15, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0015",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #15",
                    "version": 15,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV16(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #16)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=16, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0016",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #16",
                    "version": 16,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV17(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #17)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=17, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0017",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #17",
                    "version": 17,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV18(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #18)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=18, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0018",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #18",
                    "version": 18,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV19(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #19)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=19, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0019",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #19",
                    "version": 19,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV20(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #20)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=20, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0020",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #20",
                    "version": 20,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV21(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #21)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=21, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0021",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #21",
                    "version": 21,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV22(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #22)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=22, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0022",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #22",
                    "version": 22,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV23(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #23)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=23, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0023",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #23",
                    "version": 23,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TelemetrySpanRecordProfileV24(BaseModel):
    """Schema definition for OpenTelemetry distributed trace spans, parent links, and token ledgers (Profile Tier #24)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=24, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0024",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TelemetrySpanRecord Profile #24",
                    "version": 24,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV1(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #1)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=1, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0001",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #1",
                    "version": 1,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV2(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #2)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=2, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0002",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #2",
                    "version": 2,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV3(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #3)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=3, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0003",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #3",
                    "version": 3,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV4(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #4)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=4, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0004",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #4",
                    "version": 4,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV5(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #5)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=5, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0005",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #5",
                    "version": 5,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV6(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #6)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=6, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0006",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #6",
                    "version": 6,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV7(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #7)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=7, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0007",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #7",
                    "version": 7,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV8(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #8)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=8, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0008",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #8",
                    "version": 8,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV9(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #9)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=9, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0009",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #9",
                    "version": 9,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV10(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #10)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=10, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0010",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #10",
                    "version": 10,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV11(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #11)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=11, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0011",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #11",
                    "version": 11,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV12(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #12)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=12, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0012",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #12",
                    "version": 12,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV13(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #13)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=13, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0013",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #13",
                    "version": 13,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV14(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #14)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=14, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0014",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #14",
                    "version": 14,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV15(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #15)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=15, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0015",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #15",
                    "version": 15,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV16(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #16)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=16, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0016",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #16",
                    "version": 16,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV17(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #17)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=17, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0017",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #17",
                    "version": 17,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV18(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #18)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=18, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0018",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #18",
                    "version": 18,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV19(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #19)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=19, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0019",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #19",
                    "version": 19,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV20(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #20)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=20, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0020",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #20",
                    "version": 20,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV21(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #21)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=21, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0021",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #21",
                    "version": 21,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV22(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #22)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=22, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0022",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #22",
                    "version": 22,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV23(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #23)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=23, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0023",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #23",
                    "version": 23,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class TokenQuotaAllocationProfileV24(BaseModel):
    """Schema definition for monthly budget constraints, leaky bucket rate limits, and alarm thresholds (Profile Tier #24)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=24, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0024",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production TokenQuotaAllocation Profile #24",
                    "version": 24,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV1(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #1)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=1, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0001",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #1",
                    "version": 1,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV2(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #2)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=2, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0002",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #2",
                    "version": 2,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV3(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #3)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=3, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0003",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #3",
                    "version": 3,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV4(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #4)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=4, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0004",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #4",
                    "version": 4,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV5(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #5)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=5, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0005",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #5",
                    "version": 5,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV6(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #6)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=6, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0006",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #6",
                    "version": 6,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV7(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #7)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=7, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0007",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #7",
                    "version": 7,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV8(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #8)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=8, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0008",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #8",
                    "version": 8,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV9(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #9)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=9, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0009",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #9",
                    "version": 9,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV10(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #10)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=10, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0010",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #10",
                    "version": 10,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV11(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #11)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=11, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0011",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #11",
                    "version": 11,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV12(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #12)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=12, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0012",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #12",
                    "version": 12,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV13(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #13)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=13, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0013",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #13",
                    "version": 13,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV14(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #14)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=14, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0014",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #14",
                    "version": 14,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV15(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #15)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=15, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0015",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #15",
                    "version": 15,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV16(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #16)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=16, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0016",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #16",
                    "version": 16,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV17(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #17)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=17, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0017",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #17",
                    "version": 17,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV18(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #18)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=18, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0018",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #18",
                    "version": 18,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV19(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #19)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=19, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0019",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #19",
                    "version": 19,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV20(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #20)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=20, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0020",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #20",
                    "version": 20,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV21(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #21)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=21, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0021",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #21",
                    "version": 21,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV22(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #22)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=22, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0022",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #22",
                    "version": 22,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV23(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #23)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=23, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0023",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #23",
                    "version": 23,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }


class AuditLogEventRecordProfileV24(BaseModel):
    """Schema definition for immutable security compliance logs, actor contexts, and IP headers (Profile Tier #24)."""
    resource_id: str = Field(..., description="Unique immutable resource identifier")
    tenant_id: str = Field(..., description="Multi-tenant organization identifier")
    profile_name: str = Field(..., min_length=2, max_length=255)
    version: int = Field(default=24, ge=1)
    is_active: bool = Field(default=True)
    sla_tier: Literal["standard", "premium", "mission_critical"] = "premium"
    configuration_parameters: Dict[str, Any] = Field(default_factory=dict)
    operational_tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "resource_id": "res_profile_0024",
                    "tenant_id": "org_enterprise_prod",
                    "profile_name": "Production AuditLogEventRecord Profile #24",
                    "version": 24,
                    "is_active": True,
                    "sla_tier": "mission_critical"
                }
            ]
        }
    }
