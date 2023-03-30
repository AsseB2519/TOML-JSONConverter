# Processamento de Linguagens

### Grupo de Trabalho:
  - Afonso Bessa  	
  - Martim Ribeiro
  - João Barroso

## Conversor Toml-Json

Este projeto tem como objetivo a construção de uma ferramenta capaz de converter um subconjunto da linguagem Toml para o formato Json.

A linguagem Toml permite uma fácil definição de estruturas complexas, frequentemente usadas em arquivos de configuração e em vários outros domínios de modo análogo ao JSON e ao YAML.

O formato Toml é muito utilizado em configurações de aplicações e sistemas, enquanto o formato Json é utilizado em aplicações web e serviços REST.

O subconjunto da linguagem Toml que será convertido para Json será definido durante o desenvolvimento da ferramenta.

Bibliotecas Utilizadas:

  - Flex

  - Yacc

Considere o seguinte exemplo em Toml:
```
title = "TOML Example"

[owner]

name = "Tom Preston-Werner"
date = 2010-04-23
time = 21:30:00

[database]
server = "192.168.1.1"
ports = [ 8001, 8001, 8002 ]
connection_max = 5000
enabled = true

[servers]

[servers.alpha]
ip = "10.0.0.1"
dc = "eqdc10"

[servers.beta]
ip = "10.0.0.2"
dc = "eqdc10"

hosts = [
"alpha",
"omega"
]


```

Este será convertido para o seguinte formato Json:

```
{
   "title": "TOML Example",
   "owner": {
      "name": "Tom Preston-Werner",
      "date": "2010-04-23",
      "time": "21:30:00"
   },
   "database": {
      "server": "192.168.1.1",
      "ports": [
         8001,
         8001,
         8002
      ],
      "connection_max": 5000,
      "enabled": true
   },
   "servers": {
      "alpha": {
         "ip": "10.0.0.1",
         "dc": "eqdc10",
         "hosts": [
            "alpha",
            "omega"
         ]
      },
      "beta": {
         "ip": "10.0.0.2",
         "dc": "eqdc10",
         "hosts": [
            "alpha",
            "omega"
         ]
      }
   }
}
```

Para mais detalhes sobre a linguagem Toml, acesse https://github.com/toml-lang/toml.
