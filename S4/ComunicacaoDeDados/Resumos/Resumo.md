## Modelos de Referência OSI e TCP/IP
---
## <center> Aula 01 - Parte 01/03
---

Os modelos de referência **OSI** e **TCP/IP** são fundamentais na arquitetura de redes, organizando a comunicação em camadas. Cada camada tem funções específicas e protocolos que garantem a troca de informações entre máquinas. O encapsulamento e a segmentação são processos essenciais para a transmissão eficiente de dados através das camadas.

<a href="https://www.youtube.com/watch?v=PFpF38qLOBQ" target="_blank">
  <img src="../../../YouTube.png" alt="Ícone" style="width:16px; height:16px; vertical-align:middle;">
  <b style="font-family: 'Arial', sans-serif; font-size: 16px; color: #FF0000; text-decoration: none;">Link da Aula</b>
</a>

### Destaques

#### 00:08 - Arquitetura de Redes
- A arquitetura de redes é um projeto que define como os sistemas de comunicação são organizados e estruturados. Envolve tanto **hardware** quanto **software**, essenciais para a comunicação eficaz.
  - Existem dois modelos principais de referência em redes: o **modelo OSI** e o **modelo TCP/IP**. Cada um possui suas próprias camadas e protocolos, visando a comunicação padronizada.
  - **Protocolos** são conjuntos de procedimentos que facilitam a comunicação entre máquinas, definindo semântica e sintaxe para a troca de informações. Eles são fundamentais para a **interoperabilidade**.
  - O modelo de camadas organiza a arquitetura de redes em níveis, onde cada camada oferece serviços à camada superior, promovendo uma estrutura **modular** e eficiente. Isso facilita a **implementação**.

#### 04:40 - Comunicação entre Máquinas em Redes
- A comunicação entre máquinas em uma rede é estabelecida através de **camadas**, onde cada camada tem suas próprias funções e protocolos.
  - O modelo de camadas define como as informações são trocadas entre as camadas superior e inferior, garantindo a **padronização dos serviços**. Isso facilita a **evolução das tecnologias** e a interoperabilidade.
  - As **camadas inferiores** estão mais relacionadas à parte física da máquina, enquanto as **camadas superiores** lidam com aspectos de **software** e sistemas operacionais.
  - A comunicação inicia na camada superior com a geração de mensagens, que são transmitidas por diferentes camadas até chegarem ao meio físico.

#### 10:36 - Encapsulamento
- O **encapsulamento** é o processo de agregar informações de uma camada superior com um cabeçalho que contém endereços de origem e destino.
  - Cada camada do modelo **TCP/IP** gera informações específicas que são encapsuladas para a camada correspondente no destino.
  - A camada de **transporte** é responsável por gerenciar a comunicação entre processos, utilizando cabeçalhos que incluem números de porta.
  - A camada de **rede** utiliza **endereços IP** para identificar máquinas na rede, permitindo que os dados sejam enviados da origem ao destino corretamente.

#### 13:08 - Endereço Físico (MAC)
- O endereço físico, conhecido como **MAC**, é fundamental para identificar máquinas dentro de uma rede local.
  - O encapsulamento facilita a comunicação entre diferentes dispositivos na rede, desde a camada de aplicação até a camada de enlace.
  - A **segmentação** é crucial para o envio de dados grandes, como arquivos de 1GB, dividindo-os em pacotes menores.
  - Os **endereços IP** de origem e destino garantem que a informação chegue ao destino correto.

#### 17:14 - Camada de Enlace
- A camada de **enlace** gerencia a comunicação de dados entre dispositivos na mesma rede, utilizando **endereços MAC** e **trailers** para detecção de erros.
  - O processo de **encapsulamento** e **desencapsulamento** é essencial para a comunicação em rede, permitindo que dados sejam enviados e recebidos corretamente.
  - O modelo de referência **OSI**, com suas **sete camadas**, oferece uma estrutura organizada para entender como os dados são processados e transmitidos.
  - A nomenclatura dos dados muda conforme a camada em que se encontram, como **mensagem** na camada de aplicação e **segmento** na camada de transporte.

#### 21:34 - Modelo de Referência OSI
- O modelo de referência **OSI** é fundamental para entender a comunicação em redes.
  - As camadas do modelo **OSI** transformam dados em diferentes formatos, como **pacotes**, **datagramas** e **quadros**.
  - Equipamentos de interconexão, como **switches** e **roteadores**, utilizam apenas algumas camadas do modelo **OSI** para tomar decisões sobre o roteamento de dados.
  - O processo de encapsulamento e desencapsulamento é vital na comunicação em redes.

#### 25:52 - Camada Física
- A **camada física** do modelo **OSI** é fundamental para a transmissão de dados, convertendo sinais elétricos em formatos compatíveis com os meios de comunicação.
  - Essa camada é responsável por traduzir os dados da camada de enlace em **sinais adequados para transmissão**, como níveis de tensão e corrente.
  - A camada física também define o formato dos **conectores** e a **sinalização**, garantindo a transmissão correta dos dados.
  - Quando os dados chegam ao destino, a camada física inverte o processo, convertendo os sinais de volta em dados para a memória do computador.
