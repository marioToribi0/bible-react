from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from model.tools import tools
from langchain_core.prompts import ChatPromptTemplate
import datetime
from langchain.agents import (
    AgentExecutor,
    create_react_agent,
)
load_dotenv()
template = ChatPromptTemplate.from_template(
    """
Eres un experto de teología y la biblia y pastor de la Iglesia del señor. Recibirás preguntas y dudas acerca de las escrituras, vida espiritual, entre otras.
Todas tus respuestas deben basarse en versículos de la Biblia, y siempre tienes que citarlos. Debes ser abundante en tu respuesta y util, no puedes dejar dudas.
Debes responder siempre las preguntas de la manera más útil posible. Tienes que basarte en tu conocimiento para hacer búsquedas precisa en la biblia debido a que buscar frases no basta.
Debes de ejecutar tus funciones varias veces hasta obtener la respuesta. 

DEBES SER ABUDANTE EN TUS RESPUESTAS

When the information is not there you can use tools. 

TOOLS:
------
You has access to the following tools:

{tools}

To use a tool, please use the following format:

```
Thought: Do I need to use a tool? Yes
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
```

When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:

```
Thought: Do I need to use a tool? No
Final Answer: [your response here]
```

Begin!

Pregunta: {input}

chat_history: {chat_history}

{agent_scratchpad}
"""
)
prompt = template
model = ChatOpenAI(model="gpt-4-1106-preview")
agent = create_react_agent(model, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
)

async def generate_response(**kwargs):
    question = kwargs.get("prompt", None)
    current_time = datetime.datetime.now().strftime("%H:%M:%S %d/%m/%Y")
    chat_history = kwargs.get("chat_history", [])[-6:]
    start_message = 0
    async for event in agent_executor.astream_events(
        {
            "chat_history": chat_history,
            "current_time": current_time,
            "input": question,
            "language": "spanish",
        },
        version="v1",
    ):
        kind = event["event"]
        # if kind == "on_chat_model_stream":
        if kind == "on_chat_model_stream":
            content = event["data"]["chunk"].content
            if content and start_message == 2:
                yield content

            if content.strip() == "Answer":
                start_message = 1
            if content.strip() == ":" and start_message == 1:
                start_message = 2

    