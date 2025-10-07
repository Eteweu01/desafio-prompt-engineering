# 🧠 Desafio: Prompt Engineering

Este repositório contém as respostas do **Desafio de Prompt Engineering**, que tem como objetivo aplicar técnicas de formulação de *prompts* (comandos) eficazes para obter respostas mais precisas, relevantes e completas de uma ferramenta de IA generativa (como o ChatGPT da OpenAI).

Cada questão explora uma técnica específica de *Prompt Engineering*, demonstrando como a clareza, o contexto e o detalhamento do pedido influenciam diretamente na qualidade das respostas.

---

## 🔹 Questão 1 — Ray Tracing

**🧩 Técnica usada:** Prompt explicativo + detalhamento técnico  

**💬 Prompt utilizado:**
> Explique detalhadamente, passo a passo, como o algoritmo de Ray Tracing calcula a cor de um pixel em uma imagem renderizada. Inclua no resultado as etapas de interseção de raios, reflexão, refração, sombreamento e cálculo de iluminação. Utilize linguagem técnica, mas de fácil compreensão, e, se possível, um exemplo prático simplificado.

**🤖 Resposta da IA:**

O **Ray Tracing** (traçado de raios) calcula a cor de um pixel simulando o caminho da luz. O processo ocorre em várias etapas:

1. **Emissão do raio:**  
   Para cada pixel da tela, o algoritmo dispara um raio que parte da câmera e passa por aquele pixel no plano da imagem.

2. **Interseção com objetos:**  
   O algoritmo determina qual objeto é atingido primeiro pelo raio, calculando a distância e o ponto de impacto.

3. **Cálculo da iluminação local:**  
   No ponto de interseção, verifica-se a influência das fontes de luz.  
   Para cada luz:
   - Um **raio sombra** é traçado até a luz.  
   - Se não houver obstrução, a luz contribui com componentes **difusas** e **especulares**, baseadas nas leis de Lambert e Phong.

4. **Reflexão e refração (recursão):**  
   Se o material for reflexivo ou translúcido, o algoritmo lança novos raios nas direções adequadas e calcula as cores resultantes.

5. **Composição da cor final:**  
   A cor do pixel é a soma ponderada das contribuições:
   \[
   \text{CorFinal} = \text{Difusa} + \text{Especular} + k_r \times \text{Reflexão} + k_t \times \text{Refração}
   \]
   A recursão termina quando o raio não encontra mais objetos ou atinge a profundidade máxima.

---

## 🔹 Questão 2 — Decomposição numérica

**🧩 Técnica usada:** Prompt educativo + passo a passo  

**💬 Prompt utilizado:**
> Mostre detalhadamente a decomposição numérica do número 142.981. Apresente o cálculo passo a passo e explique o valor posicional de cada algarismo.

**🤖 Resposta da IA:**

A **decomposição numérica** de **142.981** é feita analisando o valor posicional de cada dígito:

\[
142.981 = 100.000 + 40.000 + 2.000 + 900 + 80 + 1
\]

🔹 **Explicação:**
- 1 → Centena de milhar = **100.000**  
- 4 → Dezena de milhar = **40.000**  
- 2 → Unidade de milhar = **2.000**  
- 9 → Centena = **900**  
- 8 → Dezena = **80**  
- 1 → Unidade = **1**

Portanto:
\[
142.981 = (1 × 100.000) + (4 × 10.000) + (2 × 1.000) + (9 × 100) + (8 × 10) + (1 × 1)
\]

---

## 🔹 Questão 3 — Personagens maquiavélicos em *As Crônicas de Gelo e Fogo*

**🧩 Técnica usada:** Prompt analítico + contexto literário e filosófico  

**💬 Prompt utilizado:**
> Analise os personagens de *As Crônicas de Gelo e Fogo* (de George R. R. Martin) e identifique quais possuem características inspiradas na filosofia de Maquiavel, especialmente em *O Príncipe*. Explique as semelhanças e dê exemplos de atitudes que refletem os princípios maquiavélicos.

**🤖 Resposta da IA:**

Diversos personagens da obra apresentam traços **maquiavélicos**, ou seja, buscam o poder por meio da estratégia, manipulação e pragmatismo.  

**Principais exemplos:**

1. **Tywin Lannister:**  
   - Frio, calculista e estrategista.  
   - Prioriza o poder e a estabilidade da Casa Lannister.  
   - Reflete o princípio de que *“os fins justificam os meios”*.

2. **Petyr Baelish (Mindinho):**  
   - Usa a informação e a intriga como armas.  
   - Manipula alianças e eventos para ascender politicamente.  
   - Encarna o perfil do príncipe maquiavélico que busca poder por mérito e astúcia.

3. **Varys:**  
   - Atua nas sombras e influencia o poder político de Westeros.  
   - Justifica seus atos pelo “bem do reino”, priorizando resultados sobre moralidade.  

4. **Cersei Lannister:**  
   - Move-se por poder e controle.  
   - Explora medo e manipulação para governar.

🧩 **Síntese:**  
Esses personagens representam bem o pensamento de Maquiavel, ao compreenderem o poder como uma arte de equilíbrio entre astúcia, controle e estratégia.

---

## 🔹 Questão 4 — Endpoint com FastAPI

**🧩 Técnica usada:** Prompt técnico estruturado + validação de requisitos  

**💬 Prompt utilizado:**
> Crie um endpoint usando FastAPI que receba um objeto `Item` com os campos `nome` (máx. 25 caracteres), `valor` (float) e `data` (date ≤ data atual). O endpoint deve validar os campos e retornar o objeto com um campo adicional `uuid` (gerado dinamicamente). Forneça o código completo e funcional.

**🤖 Resposta da IA:**

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import date
from uuid import uuid4

app = FastAPI()

class Item(BaseModel):
    nome: str = Field(..., max_length=25)
    valor: float
    data: date

@app.post("/item")
def criar_item(item: Item):
    if item.data > date.today():
        raise HTTPException(status_code=400, detail="A data não pode ser superior à data atual.")
    
    item_dict = item.dict()
    item_dict["uuid"] = str(uuid4())
    return item_dict
```

### 🧾 Explicação:
- `max_length=25`: limita o tamanho do nome.  
- `if item.data > date.today()`: impede datas futuras.  
- `uuid4()`: gera um identificador único.  
- O retorno inclui o corpo original + o novo campo `uuid`.

---

## 🏁 Conclusão

Neste desafio, foram aplicadas **técnicas distintas de Prompt Engineering** para diferentes contextos:

| Questão | Técnica aplicada | Objetivo |
|----------|------------------|-----------|
| 1 | Explicativo + técnico | Obter explicação detalhada de um algoritmo |
| 2 | Educativo + passo a passo | Explicar raciocínio matemático |
| 3 | Analítico + contextual | Relacionar literatura e filosofia |
| 4 | Estruturado + técnico | Gerar código validado e funcional |

Esses exemplos mostram como **a clareza e o detalhamento do prompt** determinam o nível de qualidade da resposta da IA, evidenciando o poder do *Prompt Engineering* na comunicação humano-máquina.

---

📌 **Autor:** *Seu Nome Aqui*  
📅 **Data:** Outubro de 2025  
🚀 **Ferramenta usada:** ChatGPT (OpenAI)
