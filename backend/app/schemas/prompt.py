from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class InputVariableDef(BaseModel):
    name: str
    type: str = "string" # string, number, boolean, json
    required: bool = True
    default_value: Optional[Any] = None
    description: Optional[str] = None


class PromptCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=255)
    description: Optional[str] = None
    tags: List[str] = Field(default_factory=list)
    system_prompt: Optional[str] = None
    user_prompt_template: str = Field(..., min_length=1)
    input_variables: List[InputVariableDef] = Field(default_factory=list)
    model_config_schema: Dict[str, Any] = Field(default_factory=lambda: {"model": "gpt-4o", "temperature": 0.7})
    commit_message: Optional[str] = "Initial prompt creation"


class PromptVersionRead(BaseModel):
    id: str
    template_id: str
    version_number: int
    system_prompt: Optional[str]
    user_prompt_template: str
    input_variables: List[InputVariableDef]
    model_config_schema: Dict[str, Any]
    commit_message: Optional[str]
    created_at: datetime


class PromptRead(BaseModel):
    id: str
    org_id: str
    name: str
    description: Optional[str]
    tags: List[str]
    active_version_id: Optional[str]
    created_at: datetime
    updated_at: datetime
    active_version: Optional[PromptVersionRead] = None


class PromptCompileRequest(BaseModel):
    variables: Dict[str, Any]
    version_id: Optional[str] = None


class PromptCompileResponse(BaseModel):
    system_prompt: Optional[str]
    user_prompt: str
    model_config: Dict[str, Any]
    estimated_tokens: int
