<div align="center">
  
# Toml-Json Converter

</div>

In this project we built a tool capable of converting a subset of the **[TOML Language](https://github.com/toml-lang/toml)** to the JSON format. 

<h3>TOML:</h3>

The **TOML Language** is commonly used in configuration files and various other domains, allowing for the easy definition of complex structures analogously to JSON and YAML. 

<h3>JSON:</h3>

Meanwhile, the JSON format is widely used in web applications and REST services because it offers a lightweight and easily readable way to structure data, making it a popular choice for exchanging information between servers and clients.

<h3>Example:</h3>

<div align="center">
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
</div>

<h3>Team Members:</h3>
<p> 
  
  - <a href="https://github.com/AsseB2519">Afonso Bessa</a>
  - <a href="https://github.com/arete12">Martim Ribeiro</a>
  - <a href="https://github.com/JoaoBarroso25">Joao Barroso</a>
</p>

<div style="flex: 1;">
  <h3>Evaluation:</h3>
  <p><strong>Score:</strong> 15/20</p>
  <p><strong>Tools:</strong> Python / Yacc / Flex </p>
</div>

