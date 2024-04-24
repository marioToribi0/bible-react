from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_openai import ChatOpenAI
from unidecode import unidecode

BOOK_LIST = ['Génesis', 'Éxodo', 'Levítico', 'Números', 'Deuteronomio', 'Josué', 'Jueces', 'Rut', '1 Samuel', '2 Samuel', '1 Reyes', '2 Reyes', '1 Crónicas', '2 Crónicas', 'Esdras', 'Nehemías', 'Ester', 'Job', 'Salmos', 'Proverbios', 'Eclesiastés', 'Cantares', 'Isaías', 'Jeremías', 'Lamentaciones', 'Ezequiel', 'Daniel', 'Oseas', 'Joel', 'Amós', 'Abdías', 'Jonás', 'Miqueas', 'Nahúm', 'Habacuc', 'Sofonías', 'Hageo', 'Zacarías', 'Malaquías', 'Mateo', 'Marcos', 'Lucas', 'Juan', 'Hechos', 'Romanos', '1 Corintios', '2 Corintios', 'Gálatas', 'Efesios', 'Filipenses', 'Colosenses', '1 Tesalonicenses', '2 Tesalonicenses', '1 Timoteo', '2 Timoteo', 'Tito', 'Filemón', 'Hebreos', 'Santiago', '1 Pedro', '2 Pedro', '1 Juan', '2 Juan', '3 Juan', 'Judas', 'Apocalipsis']
BOOK_LIST = [unidecode(book) for book in BOOK_LIST]

template = PromptTemplate.from_template(
    """
Eres un experto de teología y la biblia y pastor de la Iglesia del señor. Dado el siguiente texto debes de identificar un capítulo de la Biblia importante para leerlo.
Los libros de las biblias que usarás serán:

Tu output debe ser solamente el versiculo. De esta manera:

```

Chapter: 1 Juan,5

```

Begin!

input: {input}
"""
)

model = ChatOpenAI(
    model="gpt-3.5-turbo-0125",
    callbacks=[StreamingStdOutCallbackHandler()],
)
prompt = template

output_parser = StrOutputParser()
chain = prompt | model | output_parser
