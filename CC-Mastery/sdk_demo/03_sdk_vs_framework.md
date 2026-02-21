# Exercise 3: SDK vs Framework Comparison

## The Question
When should you use Claude Agent SDK vs LangChain/CrewAI?

## Side-by-Side: "Research Agent" Implementation

### Claude Agent SDK (Python) — ~30 lines

```python
from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

async def research(topic: str) -> dict:
    async for msg in query(
        prompt=f"Research '{topic}' using web search. Summarize findings.",
        options=ClaudeAgentOptions(
            allowed_tools=["WebSearch", "WebFetch"],
            max_turns=8,
            output_format={"type": "json_schema", "schema": REPORT_SCHEMA},
        ),
    ):
        if isinstance(msg, ResultMessage) and msg.structured_output:
            return msg.structured_output
```

**What you get for free**: tool execution, file I/O, search, bash, MCP integration,
session persistence, structured output validation, cost tracking, abort support.

### LangChain Equivalent — ~80+ lines

```python
from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain_anthropic import ChatAnthropic
from langchain.tools import DuckDuckGoSearchResults
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate

# Define tools manually
search = DuckDuckGoSearchResults()
tools = [search]

# Set up model
llm = ChatAnthropic(model="claude-sonnet-4-5-20250929")

# Build prompt template
parser = PydanticOutputParser(pydantic_object=ResearchReport)
prompt = ChatPromptTemplate.from_messages([...])

# Create agent
agent = create_openai_tools_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, max_iterations=8)

# Run
result = await executor.ainvoke({"topic": topic})
report = parser.parse(result["output"])
```

**What you must build yourself**: tool definitions, prompt templates, output parsing,
error handling, session management, file I/O tools, bash execution...

## Decision Matrix

| Criterion | Claude Agent SDK | LangChain/CrewAI |
|-----------|-----------------|------------------|
| **Setup time** | Minutes (CLI already installed) | Hours (deps, config, API keys) |
| **Tool ecosystem** | 10+ built-in (Bash, Read, Edit, Glob, Grep, Write, WebSearch, WebFetch, MCP, Task) | Must define/import each tool |
| **File operations** | Native (Read, Write, Edit, Glob, Grep) | Need custom tools or plugins |
| **Bash execution** | Built-in with sandboxing | Need custom tool, no sandboxing |
| **Session persistence** | Automatic (resume/continue) | Must implement yourself |
| **Structured output** | Native (json-schema flag) | Output parsers, retry logic |
| **Multi-agent** | Built-in (Task tool, --agents flag) | Framework's core value prop |
| **Cost tracking** | Automatic (total_cost_usd) | Must implement yourself |
| **CLAUDE.md** | Automatic context loading | N/A |
| **MCP integration** | Native | N/A |
| **Model flexibility** | Claude only | Any LLM provider |
| **Custom orchestration** | Limited (linear, fan-out) | Full DAG, conditional routing |
| **Community plugins** | Small but growing | Massive ecosystem |
| **Production deployment** | Good (CI/CD, GHA) | Mature (monitoring, tracing) |

## When to Use What

### Use Claude Agent SDK when:
- **Prototyping agents** — test the idea before committing to a framework
- **Coding tasks** — file operations, refactoring, code review, testing
- **Batch operations** — parallel `claude -p` across files/repos
- **Internal tools** — wrap complex workflows for non-technical users
- **CI/CD** — PR review bots, auto-fix pipelines, deploy checks
- **You're already using Claude Code** — zero new dependencies

### Use LangChain/CrewAI when:
- **Multi-provider** — need GPT-4 + Claude + Gemini in same pipeline
- **Complex orchestration** — DAG workflows, conditional branching, human-in-the-loop
- **Existing LangChain ecosystem** — already invested in their tooling
- **Non-Claude models** — open-source models, fine-tuned models
- **Advanced RAG** — vector stores, retrievers, document loaders
- **Production observability** — LangSmith, tracing, evaluation frameworks

### The Curriculum's Advice
> "Use SDK before reaching for LangChain/CrewAI."

Translation: Most "agentic" ideas can be validated with a 20-line SDK script.
If it works, great — ship it. If you need more orchestration, *then* reach for a framework.
The SDK is your **prototyping workbench**, not your production-only tool.

## Cost Comparison (Rough)

| Approach | Setup Time | Lines of Code | Dependencies |
|----------|-----------|--------------|-------------|
| `claude -p` (bash) | 0 min | 1-10 | 0 |
| Python SDK | 5 min | 20-50 | 1 (`claude-agent-sdk`) |
| TypeScript SDK | 5 min | 20-50 | 1 (`@anthropic-ai/claude-agent-sdk`) |
| LangChain | 30+ min | 80-200 | 5-15 packages |
| CrewAI | 30+ min | 100-300 | 5-15 packages |

## Key Takeaway

The SDK's superpower is **Claude Code's built-in tools**.
You don't need to define file readers, bash executors, or search tools.
You don't need prompt templates or output parsers.
You just say what you want and set boundaries (`--allowedTools`, `--max-turns`).

That's the "shoot and forget" philosophy from the curriculum author.
