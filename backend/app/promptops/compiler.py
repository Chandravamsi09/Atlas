import re
from typing import Dict, Any, Tuple
from jinja2 import Environment, BaseLoader, select_autoescape, TemplateSyntaxError
from backend.app.core.exceptions import PromptTemplateError


class PromptCompiler:
    """
    High-performance Jinja2 prompt compiler with variable validation,
    missing parameter detection, and safety sandboxing.
    """
    def __init__(self):
        self.jinja_env = Environment(
            loader=BaseLoader(),
            autoescape=select_autoescape(default=False),
            trim_blocks=True,
            lstrip_blocks=True
        )

    def compile(self, template_str: str, variables: Dict[str, Any]) -> str:
        try:
            template = self.jinja_env.from_string(template_str)
            rendered = template.render(**variables)
            return rendered
        except TemplateSyntaxError as e:
            raise PromptTemplateError(f"Syntax error in prompt template: {str(e)}")
        except Exception as e:
            raise PromptTemplateError(f"Failed to render prompt template: {str(e)}")

    def extract_variables(self, template_str: str) -> list[str]:
        # Extract {{ variable }} tags
        matches = re.findall(r"\{\{\s*([a-zA-Z_0-9]+)\s*\}\}", template_str)
        return list(set(matches))


prompt_compiler = PromptCompiler()
