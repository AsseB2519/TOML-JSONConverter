# Processamento de Linguagens

### Grupo de Trabalho:
- [Afonso Bessa](https://github.com/AsseB2519)
- [Martim Ribeiro](https://github.com/sldx12)
- [João Barroso](https://github.com/JoaoBarroso25)


## Conversor Toml-Json

O objetivo deste projeto é construir uma ferramenta capaz de converter um subconjunto da linguagem Toml para o formato Json. A linguagem Toml é frequentemente usada em arquivos de configuração e em vários outros domínios, permitindo a fácil definição de estruturas complexas de modo análogo ao JSON e ao YAML. Enquanto isso, o formato Json é amplamente utilizado em aplicações web e serviços REST.

Durante o desenvolvimento da ferramenta, será definido um subconjunto da linguagem Toml que será convertido para Json. Para realizar essa tarefa, serão utilizadas as seguintes bibliotecas:

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
