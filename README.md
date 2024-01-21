<p float="left">
  <img src="/img1.png" width="100" />
  <img src="/img2.png" width="100" /> 
  <img src="/img3.png" width="100" />
</p>

# Toml-Json Converter

The objective of this project is to build a tool capable of converting a subset of the Toml language to the Json format. The Toml language is commonly used in configuration files and various other domains, allowing for the easy definition of complex structures analogously to JSON and YAML. Meanwhile, the Json format is widely used in web applications and REST services.

During the development of the tool, a subset of the Toml language will be defined, which will then be converted to Json. The following libraries will be used for this task:

  - Flex

  - Yacc

Consider the following Toml example:

<table>
<tr>
<th>TOML</th>
<th>JSON</th>
</tr>
<tr>
<td>
  
```toml
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
  
</td>
<td>

```json

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

</td>
</tr>
</table>


This will be converted to the following Json format:


# Working Group
### Members:
- [Afonso Bessa](https://github.com/AsseB2519)
- [Martim Ribeiro](https://github.com/sldx12)
- [João Barroso](https://github.com/JoaoBarroso25)


Para mais detalhes sobre a linguagem Toml, acesse https://github.com/toml-lang/toml.

