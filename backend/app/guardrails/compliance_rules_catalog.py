"""\nAtlas Enterprise Compliance & Safety Guardrail Rules Catalog.\nImplements regulatory data sanitization profiles for HIPAA, GDPR, PCI-DSS, SOC2, and ISO 27001.\n"""\n
from typing import Dict, Any, List\n
COMPLIANCE_RULES_CATALOG: Dict[str, Dict[str, Any]] = {
    "rule_hipaa_v01": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #1)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v02": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #2)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v03": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #3)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v04": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #4)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v05": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #5)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v06": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #6)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v07": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #7)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v08": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #8)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v09": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #9)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v10": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #10)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v11": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #11)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v12": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #12)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v13": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #13)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v14": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #14)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v15": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #15)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v16": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #16)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v17": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #17)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v18": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #18)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v19": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #19)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v20": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #20)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v21": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #21)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v22": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #22)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v23": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #23)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v24": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #24)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v25": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #25)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v26": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #26)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v27": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #27)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v28": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #28)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_hipaa_v29": {
        "compliance_framework": "HIPAA",
        "description": "Health Insurance Portability and Accountability Act Protected Health Information (PHI) (Profile Tier #29)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.hipaa.violation"
    },
    "rule_gdpr_v01": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #1)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v02": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #2)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v03": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #3)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v04": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #4)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v05": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #5)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v06": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #6)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v07": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #7)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v08": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #8)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v09": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #9)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v10": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #10)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v11": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #11)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v12": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #12)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v13": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #13)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v14": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #14)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v15": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #15)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v16": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #16)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v17": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #17)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v18": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #18)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v19": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #19)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v20": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #20)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v21": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #21)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v22": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #22)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v23": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #23)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v24": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #24)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v25": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #25)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v26": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #26)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v27": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #27)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v28": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #28)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_gdpr_v29": {
        "compliance_framework": "GDPR",
        "description": "General Data Protection Regulation EU Citizen Personal Identifiable Information (Profile Tier #29)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.gdpr.violation"
    },
    "rule_pci_dss_v01": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #1)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v02": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #2)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v03": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #3)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v04": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #4)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v05": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #5)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v06": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #6)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v07": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #7)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v08": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #8)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v09": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #9)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v10": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #10)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v11": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #11)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v12": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #12)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v13": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #13)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v14": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #14)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v15": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #15)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v16": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #16)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v17": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #17)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v18": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #18)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v19": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #19)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v20": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #20)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v21": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #21)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v22": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #22)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v23": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #23)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v24": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #24)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v25": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #25)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v26": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #26)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v27": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #27)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v28": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #28)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_pci_dss_v29": {
        "compliance_framework": "PCI_DSS",
        "description": "Payment Card Industry Data Security Standard Cardholder Data & Auth Vectors (Profile Tier #29)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.pci_dss.violation"
    },
    "rule_soc2_v01": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #1)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v02": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #2)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v03": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #3)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v04": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #4)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v05": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #5)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v06": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #6)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v07": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #7)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v08": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #8)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v09": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #9)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v10": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #10)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v11": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #11)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v12": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #12)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v13": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #13)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v14": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #14)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v15": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #15)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v16": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #16)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v17": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #17)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v18": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #18)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v19": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #19)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v20": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #20)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v21": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #21)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v22": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #22)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v23": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #23)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v24": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #24)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v25": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #25)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v26": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #26)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v27": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #27)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v28": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #28)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_soc2_v29": {
        "compliance_framework": "SOC2",
        "description": "System and Organization Controls Type II Security and Confidentiality Trust Criteria (Profile Tier #29)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.soc2.violation"
    },
    "rule_ferpa_v01": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #1)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v02": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #2)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v03": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #3)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v04": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #4)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v05": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #5)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v06": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #6)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v07": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #7)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v08": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #8)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v09": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #9)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v10": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #10)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v11": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #11)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v12": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #12)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v13": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #13)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v14": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #14)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v15": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #15)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v16": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #16)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v17": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #17)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v18": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #18)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v19": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #19)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v20": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #20)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v21": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #21)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v22": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #22)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v23": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #23)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v24": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #24)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v25": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #25)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v26": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #26)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v27": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #27)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v28": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #28)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ferpa_v29": {
        "compliance_framework": "FERPA",
        "description": "Family Educational Rights and Privacy Act Student Record Confidentiality (Profile Tier #29)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ferpa.violation"
    },
    "rule_ccpa_v01": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #1)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v02": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #2)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v03": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #3)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v04": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #4)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v05": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #5)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v06": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #6)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v07": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #7)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v08": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #8)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v09": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #9)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v10": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #10)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v11": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #11)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v12": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #12)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v13": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #13)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v14": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #14)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v15": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #15)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v16": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #16)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v17": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #17)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v18": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #18)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v19": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #19)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v20": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #20)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v21": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #21)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v22": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #22)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v23": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #23)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v24": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #24)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v25": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #25)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v26": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #26)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v27": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #27)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v28": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #28)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
    "rule_ccpa_v29": {
        "compliance_framework": "CCPA",
        "description": "California Consumer Privacy Act Consumer Identity Anonymization Requirements (Profile Tier #29)",
        "enforcement_level": "BLOCK",
        "redaction_strategy": "HASH_MASK",
        "sensitivity_score": 0.95,
        "target_entities": [
            "PATIENT_ID", "MEDICAL_RECORD_NUMBER", "SSN", "DIAGNOSIS_CODE",
            "CREDIT_CARD_NUMBER", "CVV_CODE", "PASSPORT_NUMBER", "IBAN_CODE"
        ],
        "regex_fallback_patterns": [
            r"\b[A-Z]{2}\d{6}[A-Z0-9]\b",
            r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        ],
        "audit_event_name": "guardrail.compliance.ccpa.violation"
    },
}
