# Gamepad Stream Controller

## Sobre o Projeto
Este projeto foi feito apenas por diversão e permite que você use seu gamepad como um controlador de stream, controlador de mídias, entre outros, mapeando comandos do teclado para serem executados através do gamepad.

## Como Funciona
O script utiliza as bibliotecas `pyautogui` `pynput`, `pyjoystick` e `plyer` para mapear os inputs do gamepad para comandos de teclado. Por exemplo, você pode pausar, reproduzir ou alterar o volume diretamente do seu gamepad.

## Funcionalidades
- **Mapeamento Personalizável**: Configure seu gamepad para simular qualquer comando de teclado.
- **Perfis Pré-configurados**: Inclui perfis para mudança rápida de cena em aplicativos de streaming.

## Como Usar
1. Clone o repositório para sua máquina local.
2. Instale as dependências necessárias com
```bash
 pip install pyautogui pynput pyjoystick plyer
```
3. Configure o seu gamepad em `gamepad.py`
4. Personalize os atalhos e perfis de acordo com suas necessidades no arquivo `shortcuts.py`.
5. Execute o arquivo `main.py` para iniciar o controlador.

## Dependências
- `pyautogui` : Para a execução de comandos.
- `pynput`: Para captura eventos do teclado.
- `pyjoystick`: Para integração com o gamepad.
- `plyer`: Para notificações do sistema.

## Contribuindo
Contribuições são bem-vindas! Se você tem melhorias ou correções, sinta-se à vontade para fazer um fork do projeto e abrir um pull request, ou criar uma issue.

## Ideas de features:
- Suporte à outros gamepads (PS4, PS5).
- Integração com aplicativos como OBS, Stream Labs, Spotify, Youtube Music, entre outros.
- Abrir jogos/aplicativos.
