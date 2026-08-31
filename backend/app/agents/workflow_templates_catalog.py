"""\nAtlas Pre-Built Production Agent DAG Workflow Templates Catalog.\nContains industrial multi-step workflow graphs with branching logic and tool bindings.\n"""\n
from typing import Dict, Any, List\n
WORKFLOW_TEMPLATES_CATALOG: Dict[str, Dict[str, Any]] = {
    "template_legal_contract_analyzer_v01": {
        "template_id": "tpl_legal_contract_analyzer_v1",
        "name": "Legal Contract Analyzer Pipeline (v1)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v02": {
        "template_id": "tpl_legal_contract_analyzer_v2",
        "name": "Legal Contract Analyzer Pipeline (v2)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v03": {
        "template_id": "tpl_legal_contract_analyzer_v3",
        "name": "Legal Contract Analyzer Pipeline (v3)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v04": {
        "template_id": "tpl_legal_contract_analyzer_v4",
        "name": "Legal Contract Analyzer Pipeline (v4)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v05": {
        "template_id": "tpl_legal_contract_analyzer_v5",
        "name": "Legal Contract Analyzer Pipeline (v5)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v06": {
        "template_id": "tpl_legal_contract_analyzer_v6",
        "name": "Legal Contract Analyzer Pipeline (v6)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v07": {
        "template_id": "tpl_legal_contract_analyzer_v7",
        "name": "Legal Contract Analyzer Pipeline (v7)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v08": {
        "template_id": "tpl_legal_contract_analyzer_v8",
        "name": "Legal Contract Analyzer Pipeline (v8)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v09": {
        "template_id": "tpl_legal_contract_analyzer_v9",
        "name": "Legal Contract Analyzer Pipeline (v9)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v10": {
        "template_id": "tpl_legal_contract_analyzer_v10",
        "name": "Legal Contract Analyzer Pipeline (v10)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v11": {
        "template_id": "tpl_legal_contract_analyzer_v11",
        "name": "Legal Contract Analyzer Pipeline (v11)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v12": {
        "template_id": "tpl_legal_contract_analyzer_v12",
        "name": "Legal Contract Analyzer Pipeline (v12)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v13": {
        "template_id": "tpl_legal_contract_analyzer_v13",
        "name": "Legal Contract Analyzer Pipeline (v13)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v14": {
        "template_id": "tpl_legal_contract_analyzer_v14",
        "name": "Legal Contract Analyzer Pipeline (v14)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v15": {
        "template_id": "tpl_legal_contract_analyzer_v15",
        "name": "Legal Contract Analyzer Pipeline (v15)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v16": {
        "template_id": "tpl_legal_contract_analyzer_v16",
        "name": "Legal Contract Analyzer Pipeline (v16)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v17": {
        "template_id": "tpl_legal_contract_analyzer_v17",
        "name": "Legal Contract Analyzer Pipeline (v17)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v18": {
        "template_id": "tpl_legal_contract_analyzer_v18",
        "name": "Legal Contract Analyzer Pipeline (v18)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v19": {
        "template_id": "tpl_legal_contract_analyzer_v19",
        "name": "Legal Contract Analyzer Pipeline (v19)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v20": {
        "template_id": "tpl_legal_contract_analyzer_v20",
        "name": "Legal Contract Analyzer Pipeline (v20)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v21": {
        "template_id": "tpl_legal_contract_analyzer_v21",
        "name": "Legal Contract Analyzer Pipeline (v21)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v22": {
        "template_id": "tpl_legal_contract_analyzer_v22",
        "name": "Legal Contract Analyzer Pipeline (v22)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v23": {
        "template_id": "tpl_legal_contract_analyzer_v23",
        "name": "Legal Contract Analyzer Pipeline (v23)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_legal_contract_analyzer_v24": {
        "template_id": "tpl_legal_contract_analyzer_v24",
        "name": "Legal Contract Analyzer Pipeline (v24)",
        "description": "Autonomous NDA, MSA, and SLA contractual risk assessment with clause diffing",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v01": {
        "template_id": "tpl_financial_earnings_auditor_v1",
        "name": "Financial Earnings Auditor Pipeline (v1)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v02": {
        "template_id": "tpl_financial_earnings_auditor_v2",
        "name": "Financial Earnings Auditor Pipeline (v2)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v03": {
        "template_id": "tpl_financial_earnings_auditor_v3",
        "name": "Financial Earnings Auditor Pipeline (v3)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v04": {
        "template_id": "tpl_financial_earnings_auditor_v4",
        "name": "Financial Earnings Auditor Pipeline (v4)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v05": {
        "template_id": "tpl_financial_earnings_auditor_v5",
        "name": "Financial Earnings Auditor Pipeline (v5)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v06": {
        "template_id": "tpl_financial_earnings_auditor_v6",
        "name": "Financial Earnings Auditor Pipeline (v6)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v07": {
        "template_id": "tpl_financial_earnings_auditor_v7",
        "name": "Financial Earnings Auditor Pipeline (v7)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v08": {
        "template_id": "tpl_financial_earnings_auditor_v8",
        "name": "Financial Earnings Auditor Pipeline (v8)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v09": {
        "template_id": "tpl_financial_earnings_auditor_v9",
        "name": "Financial Earnings Auditor Pipeline (v9)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v10": {
        "template_id": "tpl_financial_earnings_auditor_v10",
        "name": "Financial Earnings Auditor Pipeline (v10)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v11": {
        "template_id": "tpl_financial_earnings_auditor_v11",
        "name": "Financial Earnings Auditor Pipeline (v11)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v12": {
        "template_id": "tpl_financial_earnings_auditor_v12",
        "name": "Financial Earnings Auditor Pipeline (v12)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v13": {
        "template_id": "tpl_financial_earnings_auditor_v13",
        "name": "Financial Earnings Auditor Pipeline (v13)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v14": {
        "template_id": "tpl_financial_earnings_auditor_v14",
        "name": "Financial Earnings Auditor Pipeline (v14)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v15": {
        "template_id": "tpl_financial_earnings_auditor_v15",
        "name": "Financial Earnings Auditor Pipeline (v15)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v16": {
        "template_id": "tpl_financial_earnings_auditor_v16",
        "name": "Financial Earnings Auditor Pipeline (v16)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v17": {
        "template_id": "tpl_financial_earnings_auditor_v17",
        "name": "Financial Earnings Auditor Pipeline (v17)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v18": {
        "template_id": "tpl_financial_earnings_auditor_v18",
        "name": "Financial Earnings Auditor Pipeline (v18)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v19": {
        "template_id": "tpl_financial_earnings_auditor_v19",
        "name": "Financial Earnings Auditor Pipeline (v19)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v20": {
        "template_id": "tpl_financial_earnings_auditor_v20",
        "name": "Financial Earnings Auditor Pipeline (v20)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v21": {
        "template_id": "tpl_financial_earnings_auditor_v21",
        "name": "Financial Earnings Auditor Pipeline (v21)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v22": {
        "template_id": "tpl_financial_earnings_auditor_v22",
        "name": "Financial Earnings Auditor Pipeline (v22)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v23": {
        "template_id": "tpl_financial_earnings_auditor_v23",
        "name": "Financial Earnings Auditor Pipeline (v23)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_financial_earnings_auditor_v24": {
        "template_id": "tpl_financial_earnings_auditor_v24",
        "name": "Financial Earnings Auditor Pipeline (v24)",
        "description": "10-K / 10-Q filing multi-source tabular extraction and financial ratio synthesis",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v01": {
        "template_id": "tpl_code_security_reviewer_v1",
        "name": "Code Security Reviewer Pipeline (v1)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v02": {
        "template_id": "tpl_code_security_reviewer_v2",
        "name": "Code Security Reviewer Pipeline (v2)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v03": {
        "template_id": "tpl_code_security_reviewer_v3",
        "name": "Code Security Reviewer Pipeline (v3)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v04": {
        "template_id": "tpl_code_security_reviewer_v4",
        "name": "Code Security Reviewer Pipeline (v4)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v05": {
        "template_id": "tpl_code_security_reviewer_v5",
        "name": "Code Security Reviewer Pipeline (v5)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v06": {
        "template_id": "tpl_code_security_reviewer_v6",
        "name": "Code Security Reviewer Pipeline (v6)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v07": {
        "template_id": "tpl_code_security_reviewer_v7",
        "name": "Code Security Reviewer Pipeline (v7)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v08": {
        "template_id": "tpl_code_security_reviewer_v8",
        "name": "Code Security Reviewer Pipeline (v8)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v09": {
        "template_id": "tpl_code_security_reviewer_v9",
        "name": "Code Security Reviewer Pipeline (v9)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v10": {
        "template_id": "tpl_code_security_reviewer_v10",
        "name": "Code Security Reviewer Pipeline (v10)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v11": {
        "template_id": "tpl_code_security_reviewer_v11",
        "name": "Code Security Reviewer Pipeline (v11)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v12": {
        "template_id": "tpl_code_security_reviewer_v12",
        "name": "Code Security Reviewer Pipeline (v12)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v13": {
        "template_id": "tpl_code_security_reviewer_v13",
        "name": "Code Security Reviewer Pipeline (v13)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v14": {
        "template_id": "tpl_code_security_reviewer_v14",
        "name": "Code Security Reviewer Pipeline (v14)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v15": {
        "template_id": "tpl_code_security_reviewer_v15",
        "name": "Code Security Reviewer Pipeline (v15)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v16": {
        "template_id": "tpl_code_security_reviewer_v16",
        "name": "Code Security Reviewer Pipeline (v16)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v17": {
        "template_id": "tpl_code_security_reviewer_v17",
        "name": "Code Security Reviewer Pipeline (v17)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v18": {
        "template_id": "tpl_code_security_reviewer_v18",
        "name": "Code Security Reviewer Pipeline (v18)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v19": {
        "template_id": "tpl_code_security_reviewer_v19",
        "name": "Code Security Reviewer Pipeline (v19)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v20": {
        "template_id": "tpl_code_security_reviewer_v20",
        "name": "Code Security Reviewer Pipeline (v20)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v21": {
        "template_id": "tpl_code_security_reviewer_v21",
        "name": "Code Security Reviewer Pipeline (v21)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v22": {
        "template_id": "tpl_code_security_reviewer_v22",
        "name": "Code Security Reviewer Pipeline (v22)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v23": {
        "template_id": "tpl_code_security_reviewer_v23",
        "name": "Code Security Reviewer Pipeline (v23)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_code_security_reviewer_v24": {
        "template_id": "tpl_code_security_reviewer_v24",
        "name": "Code Security Reviewer Pipeline (v24)",
        "description": "Static application security testing (SAST) and CVE vulnerability remediation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v01": {
        "template_id": "tpl_rag_multihop_synthesizer_v1",
        "name": "Rag Multihop Synthesizer Pipeline (v1)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v02": {
        "template_id": "tpl_rag_multihop_synthesizer_v2",
        "name": "Rag Multihop Synthesizer Pipeline (v2)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v03": {
        "template_id": "tpl_rag_multihop_synthesizer_v3",
        "name": "Rag Multihop Synthesizer Pipeline (v3)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v04": {
        "template_id": "tpl_rag_multihop_synthesizer_v4",
        "name": "Rag Multihop Synthesizer Pipeline (v4)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v05": {
        "template_id": "tpl_rag_multihop_synthesizer_v5",
        "name": "Rag Multihop Synthesizer Pipeline (v5)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v06": {
        "template_id": "tpl_rag_multihop_synthesizer_v6",
        "name": "Rag Multihop Synthesizer Pipeline (v6)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v07": {
        "template_id": "tpl_rag_multihop_synthesizer_v7",
        "name": "Rag Multihop Synthesizer Pipeline (v7)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v08": {
        "template_id": "tpl_rag_multihop_synthesizer_v8",
        "name": "Rag Multihop Synthesizer Pipeline (v8)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v09": {
        "template_id": "tpl_rag_multihop_synthesizer_v9",
        "name": "Rag Multihop Synthesizer Pipeline (v9)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v10": {
        "template_id": "tpl_rag_multihop_synthesizer_v10",
        "name": "Rag Multihop Synthesizer Pipeline (v10)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v11": {
        "template_id": "tpl_rag_multihop_synthesizer_v11",
        "name": "Rag Multihop Synthesizer Pipeline (v11)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v12": {
        "template_id": "tpl_rag_multihop_synthesizer_v12",
        "name": "Rag Multihop Synthesizer Pipeline (v12)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v13": {
        "template_id": "tpl_rag_multihop_synthesizer_v13",
        "name": "Rag Multihop Synthesizer Pipeline (v13)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v14": {
        "template_id": "tpl_rag_multihop_synthesizer_v14",
        "name": "Rag Multihop Synthesizer Pipeline (v14)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v15": {
        "template_id": "tpl_rag_multihop_synthesizer_v15",
        "name": "Rag Multihop Synthesizer Pipeline (v15)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v16": {
        "template_id": "tpl_rag_multihop_synthesizer_v16",
        "name": "Rag Multihop Synthesizer Pipeline (v16)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v17": {
        "template_id": "tpl_rag_multihop_synthesizer_v17",
        "name": "Rag Multihop Synthesizer Pipeline (v17)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v18": {
        "template_id": "tpl_rag_multihop_synthesizer_v18",
        "name": "Rag Multihop Synthesizer Pipeline (v18)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v19": {
        "template_id": "tpl_rag_multihop_synthesizer_v19",
        "name": "Rag Multihop Synthesizer Pipeline (v19)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v20": {
        "template_id": "tpl_rag_multihop_synthesizer_v20",
        "name": "Rag Multihop Synthesizer Pipeline (v20)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v21": {
        "template_id": "tpl_rag_multihop_synthesizer_v21",
        "name": "Rag Multihop Synthesizer Pipeline (v21)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v22": {
        "template_id": "tpl_rag_multihop_synthesizer_v22",
        "name": "Rag Multihop Synthesizer Pipeline (v22)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v23": {
        "template_id": "tpl_rag_multihop_synthesizer_v23",
        "name": "Rag Multihop Synthesizer Pipeline (v23)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_rag_multihop_synthesizer_v24": {
        "template_id": "tpl_rag_multihop_synthesizer_v24",
        "name": "Rag Multihop Synthesizer Pipeline (v24)",
        "description": "Multi-hop iterative document retrieval, cross-verification, and citation generation",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v01": {
        "template_id": "tpl_customer_support_resolver_v1",
        "name": "Customer Support Resolver Pipeline (v1)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v02": {
        "template_id": "tpl_customer_support_resolver_v2",
        "name": "Customer Support Resolver Pipeline (v2)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v03": {
        "template_id": "tpl_customer_support_resolver_v3",
        "name": "Customer Support Resolver Pipeline (v3)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v04": {
        "template_id": "tpl_customer_support_resolver_v4",
        "name": "Customer Support Resolver Pipeline (v4)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v05": {
        "template_id": "tpl_customer_support_resolver_v5",
        "name": "Customer Support Resolver Pipeline (v5)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v06": {
        "template_id": "tpl_customer_support_resolver_v6",
        "name": "Customer Support Resolver Pipeline (v6)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v07": {
        "template_id": "tpl_customer_support_resolver_v7",
        "name": "Customer Support Resolver Pipeline (v7)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v08": {
        "template_id": "tpl_customer_support_resolver_v8",
        "name": "Customer Support Resolver Pipeline (v8)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v09": {
        "template_id": "tpl_customer_support_resolver_v9",
        "name": "Customer Support Resolver Pipeline (v9)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v10": {
        "template_id": "tpl_customer_support_resolver_v10",
        "name": "Customer Support Resolver Pipeline (v10)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v11": {
        "template_id": "tpl_customer_support_resolver_v11",
        "name": "Customer Support Resolver Pipeline (v11)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v12": {
        "template_id": "tpl_customer_support_resolver_v12",
        "name": "Customer Support Resolver Pipeline (v12)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v13": {
        "template_id": "tpl_customer_support_resolver_v13",
        "name": "Customer Support Resolver Pipeline (v13)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v14": {
        "template_id": "tpl_customer_support_resolver_v14",
        "name": "Customer Support Resolver Pipeline (v14)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v15": {
        "template_id": "tpl_customer_support_resolver_v15",
        "name": "Customer Support Resolver Pipeline (v15)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v16": {
        "template_id": "tpl_customer_support_resolver_v16",
        "name": "Customer Support Resolver Pipeline (v16)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v17": {
        "template_id": "tpl_customer_support_resolver_v17",
        "name": "Customer Support Resolver Pipeline (v17)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v18": {
        "template_id": "tpl_customer_support_resolver_v18",
        "name": "Customer Support Resolver Pipeline (v18)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v19": {
        "template_id": "tpl_customer_support_resolver_v19",
        "name": "Customer Support Resolver Pipeline (v19)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v20": {
        "template_id": "tpl_customer_support_resolver_v20",
        "name": "Customer Support Resolver Pipeline (v20)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v21": {
        "template_id": "tpl_customer_support_resolver_v21",
        "name": "Customer Support Resolver Pipeline (v21)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v22": {
        "template_id": "tpl_customer_support_resolver_v22",
        "name": "Customer Support Resolver Pipeline (v22)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v23": {
        "template_id": "tpl_customer_support_resolver_v23",
        "name": "Customer Support Resolver Pipeline (v23)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
    "template_customer_support_resolver_v24": {
        "template_id": "tpl_customer_support_resolver_v24",
        "name": "Customer Support Resolver Pipeline (v24)",
        "description": "Automated tier-1 ticket classification, policy search, and response drafting",
        "nodes": [
            {"id": "input_router", "type": "classifier", "model": "gpt-4o-mini"},
            {"id": "retriever_node", "type": "hybrid_rag", "top_k": 5},
            {"id": "reasoning_agent", "type": "react_loop", "max_iterations": 4},
            {"id": "guardrail_check", "type": "safety_filter", "framework": "SOC2"},
            {"id": "output_synthesizer", "type": "llm_generate", "model": "gpt-4o"}
        ],
        "edges": [
            {"from": "input_router", "to": "retriever_node", "condition": "always"},
            {"from": "retriever_node", "to": "reasoning_agent", "condition": "context_found"},
            {"from": "reasoning_agent", "to": "guardrail_check", "condition": "solution_ready"},
            {"from": "guardrail_check", "to": "output_synthesizer", "condition": "passed"}
        ],
        "state_schema": {
            "session_id": "string",
            "extracted_facts": "array",
            "confidence_score": "float",
            "verified": "boolean"
        }
    },
}
