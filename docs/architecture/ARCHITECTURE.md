# PERITO-AI — Arquitetura do Sistema

> Documento de Arquitetura Técnica Oficial  
> Versão: 0.1.0  
> Status: Em definição inicial

---

# 1. Visão Geral

O PERITO-AI é um framework de inteligência artificial orientado a agentes especializados, projetado para automação e suporte à **Perícia Contábil Técnica**.

Seu objetivo arquitetural é transformar documentos, dados financeiros e informações processuais em **laudos periciais estruturados, auditáveis e tecnicamente consistentes**.

O sistema é baseado em:

- Arquitetura Modular
- Clean Architecture
- Multi-Agent Systems
- Pipeline de Processamento de Documentos
- Camada de abstração de modelos de IA (LLM-agnostic)

---

# 2. Princípios Arquiteturais

O sistema segue rigorosamente os seguintes princípios:

## 2.1 Separação de Responsabilidades (SRP)

Cada módulo deve possuir uma única responsabilidade clara:

- Agentes não executam infraestrutura
- Serviços não contêm regras de negócio
- Pipelines não decidem lógica contábil

---

## 2.2 Independência de Modelos de IA

O sistema NÃO depende de um modelo específico.

Modelos suportados:

- Claude
- GPT
- Gemini
- Modelos locais (Ollama, Llama, etc.)

---

## 2.3 Observabilidade e Auditabilidade

Toda decisão gerada por IA deve ser:

- Rastreável
- Explicável
- Reproduzível

---

## 2.4 Modularidade Extrema

Cada componente pode ser:

- substituído
- estendido
- versionado independentemente

---

## 2.5 Fluxo Orientado a Pipeline

Todo documento percorre um fluxo padronizado:

```
Input → Pré-processamento → OCR → Estruturação → Análise → Validação → Geração → Output
```

---

# 3. Arquitetura em Camadas

O PERITO-AI é dividido em 5 camadas principais:

```
┌──────────────────────────────┐
│ 1. Interface / API Layer     │
├──────────────────────────────┤
│ 2. Orquestração (Core)      │
├──────────────────────────────┤
│ 3. Agentes de IA            │
├──────────────────────────────┤
│ 4. Serviços de Domínio      │
├──────────────────────────────┤
│ 5. Infraestrutura           │
└──────────────────────────────┘
```

---

## 3.1 Interface / API Layer

Responsável por:

- Entrada de documentos
- Integração com n8n
- Webhooks
- APIs REST
- Upload de arquivos

---

## 3.2 Orquestração (Core)

Responsável por:

- Controlar fluxos de execução
- Gerenciar pipelines
- Coordenar agentes
- Garantir consistência do processo

Componentes:

- Workflow Engine
- Pipeline Manager
- Context Manager

---

## 3.3 Agentes de IA

Camada responsável por inteligência:

- Agente Pericial
- Agente Contábil
- Agente Jurídico
- Agente OCR
- Agente Revisor

Cada agente:

- Recebe contexto estruturado
- Executa tarefa específica
- Retorna output validado

---

## 3.4 Serviços de Domínio

Responsáveis por regras de negócio:

- Cálculos contábeis
- Regras de perícia
- Validação de dados
- Regras jurídicas auxiliares
- Normalização de dados

---

## 3.5 Infraestrutura

Responsável por:

- OCR engines
- Storage (local / cloud)
- APIs externas
- Banco de dados
- Logging
- Cache

---

# 4. Fluxo Completo do Sistema

## 4.1 Fluxo Geral

```
[Documento de Entrada]
        ↓
[Pré-processamento]
        ↓
[OCR / Extração de Texto]
        ↓
[Normalização de Dados]
        ↓
[Pipeline de Análise]
        ↓
    ┌───────────────┐
    │ Agentes IA     │
    └───────────────┘
        ↓
[Validação Técnica]
        ↓
[Geração de Laudo]
        ↓
[Exportação Final]
```

---

## 4.2 Fluxo com Agentes

```
Documento Estruturado
        ↓
┌──────────────────────┐
│ Agente OCR           │
│ Agente Contábil      │
│ Agente Jurídico      │
│ Agente Pericial      │
└──────────────────────┘
        ↓
Resultado Consolidado
        ↓
Agente Revisor
        ↓
Laudo Final
```

---

# 5. Sistema de Agentes

Os agentes seguem o padrão:

```
Input Context → Reasoning → Tool Use → Output → Validation
```

## 5.1 Características dos Agentes

- Stateless (não mantêm estado persistente)
- Baseados em prompts versionados
- Podem ser substituídos por novos modelos
- Trabalham com contexto estruturado

---

## 5.2 Exemplo de Responsabilidade

| Agente | Responsabilidade |
|--------|-----------------|
| OCR Agent | Extração e limpeza de texto |
| Accounting Agent | Análise contábil |
| Legal Agent | Interpretação jurídica auxiliar |
| Expert Agent | Consolidação técnica |
| Review Agent | Validação final |

---

# 6. Pipeline Engine

O Pipeline Engine controla todo o fluxo:

- Encadeamento de etapas
- Retry em falhas
- Logging de execução
- Versionamento de pipelines

Estrutura:

```
Pipeline
 ├── Stage 1: Input
 ├── Stage 2: Processing
 ├── Stage 3: AI Agents
 ├── Stage 4: Validation
 └── Stage 5: Output
```

---

# 7. Estratégia de IA

O sistema utiliza:

## 7.1 Multi-Model Abstraction

Cada agente pode escolher modelo:

- Claude → análises complexas
- GPT → general reasoning
- Local models → tarefas leves

---

## 7.2 Prompt Engineering Versionado

Prompts ficam armazenados em:

```
/docs/prompts/
```

---

## 7.3 Context Engineering

O sistema utiliza:

- Context builder
- Context filters
- Context compression

---

# 8. Persistência de Dados

Tipos de dados:

- Documentos brutos
- Documentos processados
- Resultados de agentes
- Logs de execução
- Laudos finais

---

# 9. Segurança e Auditoria

Todo output deve conter:

- Origem dos dados
- Histórico de processamento
- Agentes envolvidos
- Versão do prompt/modelo

---

# 10. Escalabilidade

O sistema é preparado para:

- Execução distribuída
- Processamento paralelo de documentos
- Integração com filas (RabbitMQ / Redis)
- Microsserviços futuros

---

# 11. Extensibilidade

Novos módulos podem ser adicionados via:

- Novos agentes
- Novos pipelines
- Novos serviços
- Plugins de IA

Sem alterar o core do sistema.

---

# 12. Decisão Arquitetural Central

O PERITO-AI é:

> Um sistema orientado a pipeline de documentos com inteligência multiagente desacoplada do modelo de IA.

---

# 13. Próximos Passos

Este documento habilita a construção de:

- Estrutura de diretórios real em `src/`
- Definição dos primeiros agentes
- Implementação do Pipeline Engine
- Sistema de prompts versionados
```