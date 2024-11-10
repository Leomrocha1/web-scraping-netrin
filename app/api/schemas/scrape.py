from pydantic import BaseModel, field_validator
import re


class ScrapeSchema(BaseModel):
    cnpj: str
    
    @field_validator("cnpj")
    def validate_cnpj(cls, value):
        cnpj = value.replace(".", "").replace("/", "").replace("-", "")
        cleaned_cnpj = re.sub(r'[^0-9]', '', cnpj)
        
        if not cleaned_cnpj or len(cleaned_cnpj) != 14:
            raise ValueError("CNPJ inválido")
        return cnpj