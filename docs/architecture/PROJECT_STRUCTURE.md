# PERITO-AI — Estrutura do Projeto

> Documento oficial de estrutura do repositório  
> Versão: 0.1.0  
> Status: Definição inicial da base do código

---

# 1. Objetivo

Este documento define a **estrutura física do código-fonte do PERITO-AI**, garantindo:

- Organização previsível
- Escalabilidade
- Separação clara de responsabilidades
- Baixo acoplamento entre módulos
- Facilidade de manutenção e extensão

---

# 2. Visão Geral da Estrutura

```
PERITO-AI/

docs/
src/
tests/
examples/
.github/
```

---

# 3. Estrutura Detalhada do Código

## 3.1 `/src` — Núcleo do Sistema

```
src/

core/
agents/
services/
pipelines/
models/
templates/
validators/
utils/
```

---

# 3.2 Core (Orquestração Central)

```
core/
│
├── orchestrator.py
├── pipeline_engine.py
├── context_manager.py
├── workflow_manager.py
└── config.py
```

### Responsabilidade:

Controlar o fluxo geral do sistema.

- Execução de pipelines
- Coordenação de agentes
- Gerenciamento de contexto
- Configuração global

---

# 4. Agents (Camada de IA)

```
agents/
│
├── base_agent.py
├── ocr_agent.py
├── accounting_agent.py
├── legal_agent.py
├── expert_agent.py
├── review_agent.py
└── registry.py
```

### Responsabilidade:

Executar inteligência especializada.

- Cada agente = 1 responsabilidade clara
- Baseado em prompts versionados
- Independente de infraestrutura

---

# 5. Services (Regras de Negócio)

```
services/
│
├── accounting_service.py
├── calculation_service.py
├── document_service.py
├── validation_service.py
└── export_service.py
```

### Responsabilidade:

Implementar regras de domínio da perícia contábil.

- Cálculos financeiros
- Validação técnica
- Regras periciais
- Processamento estruturado de dados

---

# 6. Pipelines (Fluxos de Execução)

```
pipelines/
│
├── base_pipeline.py
├── document_pipeline.py
├── analysis_pipeline.py
└── report_pipeline.py
```

### Responsabilidade:

Definir fluxos completos de processamento.

Exemplo:

```
Entrada → OCR → Estruturação → Análise → Laudo
```

---

# 7. Models (Estruturas de Dados)

```
models/
│
├── document.py
├── extraction.py
├── analysis.py
├── report.py
└── enums.py
```

### Responsabilidade:

Definir contratos de dados.

- Tipagem clara
- Estruturação de inputs e outputs
- Padronização entre agentes

---

# 8. Templates (Geração de Laudos)

```
templates/
│
├── report_template.py
├── section_templates.py
└── prompt_templates.py
```

### Responsabilidade:

- Estruturar laudos finais
- Padronizar documentos gerados
- Definir formato oficial dos relatórios

---

# 9. Validators (Validação de Dados)

```
validators/
│
├── document_validator.py
├── financial_validator.py
├── consistency_validator.py
└── schema_validator.py
```

### Responsabilidade:

Garantir integridade dos dados.

- Checagem de inconsistências
- Validação estrutural
- Auditoria de resultados

---

# 10. Utils (Utilitários Gerais)

```
utils/
│
├── logger.py
├── file_handler.py
├── date_utils.py
├── text_processing.py
└── config_loader.py
```

### Responsabilidade:

Funções auxiliares reutilizáveis.

---

# 11. Infraestrutura Externa (Futuro)

Estrutura preparada para expansão:

- OCR engines
- APIs externas
- Banco de dados
- Cache
- Mensageria

---

# 12. Testes

```
tests/

unit/
integration/
e2e/
fixtures/
```

### Estratégia:

- Testes unitários para cada módulo
- Testes de integração para pipelines
- Testes E2E para fluxos completos

---

# 13. Examples

```
examples/

sample_documents/
sample_outputs/
notebooks/
```

### Objetivo:

- Demonstração de uso
- Testes manuais
- Protótipos

---

# 14. GitHub / CI

```
.github/

workflows/
```

### Futuro:

- CI/CD automatizado
- Lint
- Testes automáticos
- Build validation

---

# 15. Regras de Importação

## Regra 1 — Fluxo Unidirecional

```
core → pipelines → agents → services → models
```

 proibido:

- agents importarem core
- services importarem agents

---

## Regra 2 — Dependências externas isoladas

- APIs externas ficam isoladas em `services/`

---

## Regra 3 — Models são independentes

- Nenhum módulo altera models diretamente

---

# 16. Convenção de Nomeação

- snake_case → arquivos Python
- PascalCase → classes
- UPPER_CASE → constantes
- sufixo `_agent`, `_service`, `_pipeline`

---

# 17. Princípio de Escalabilidade

Qualquer novo recurso deve seguir:

- criar novo agent OU service
- não modificar core desnecessariamente
- preservar compatibilidade de pipelines

---

# 18. Conclusão

Esta estrutura garante que o PERITO-AI seja:

- escalável
- modular
- testável
- extensível
- pronto para produção

---

# 19. Próximo Passo

Com essa estrutura definida, o próximo arquivo natural é:

 `docs/architecture/TECH_STACK.md`

Onde vamos definir:

- Python versão
- bibliotecas base
- frameworks de IA
- OCR
- banco de dados
- estratégia de deploy
- integrações futuras
```