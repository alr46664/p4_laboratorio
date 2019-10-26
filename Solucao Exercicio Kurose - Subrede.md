# Questao

Subdividir a subrede **200.129.39.32/27** em 3 outras subredes.

## Solucao

1) Temos 32 endereços IP disponíveis da seguinte forma:
    * **200.129.39.32/27**
    * Faixa de Endereços: &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;200.129.39.32 - 64
    * Endereço de **Rede**: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;200.129.39.32
    * Endereço de **Broadcast**: &nbsp; &nbsp;200.129.39.64
    * **Mascara** de Subrede: &nbsp;&nbsp; &nbsp; &nbsp;&nbsp; &nbsp;255.255.255.224

### Logo podemos dividir essa rede da seguinte forma
    
* Subrede com 16 IPs 
    * **200.129.39.32/28**
    * Faixa de Endereços: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;200.129.39.32 - 47
    * Endereço de **Rede**:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; 200.129.39.32
    * Endereço de **Broadcast**: &nbsp; 200.129.39.47
    * **Mascara** de Subrede: &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;255.255.255.240
* Subrede com  8 IPs 
    * **200.129.39.48/29**
    * Faixa de Endereços: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;200.129.39.48 - 55
    * Endereço de **Rede**:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; 200.129.39.48
    * Endereço de **Broadcast**: &nbsp; 200.129.39.55
    * **Mascara** de Subrede: &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;255.255.255.248
* Subrede com  8 IPs
    * **200.129.39.56/29**
    * Faixa de Endereços: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;200.129.39.56 - 63
    * Endereço de **Rede**:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; 200.129.39.56
    * Endereço de **Broadcast**: &nbsp; 200.129.39.63
    * **Mascara** de Subrede: &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;255.255.255.248

# Como realizar os cálculos de IPs em Subredes

### Como calcular o numero de IPs disponíveis em uma Subrede - Método 01

1) Pegue 255.255.255.255 e subtraia da mascara de subrede
2) Agora some 1

* Ex:
    * Mascara de subrede 255.255.255.192
    * 255.255.255.255 - 255.255.255.192 = 63
    * 63 + 1 = 64 IPs disponíveis nessa subrede
    * Total de IPs que podem ser associados a cada máquina da rede: 64 - 2 = 62

### Como calcular o numero de IPs disponíveis em uma Subrede - Método 02

1) Pegue 32 e subtraia do CIDR da subrede
2) Agora faça 2 elevado ao número encontrado acima

* Ex:
    * **Subrede** 192.168.0.0/24
    * **CIDR**: 24
    * 32 - 24 = 8
    * 2<sup>8</sup> = 256 IPs disponíveis nessa subrede
    * Total de IPs que podem ser associados a cada máquina da rede: 256 - 2 = 254

### Como calcular Endereço de Broadcast de uma Subrede 

1) Pegue o endereço de rede e some ao número de IPs disponíveis
2) Agora subtraia 1

* Ex:
    * **Subrede** 192.168.0.0/24
    * **Endereço de rede**: 192.168.0.0
    * 256 IPs disponíveis
    * 192.168.0.0 + 256 = 192.168.0.256
    * 192.168.0.256 - 1 = 192.168.0.255
    * **Endereço de Broadcast**: 192.168.0.255
    * **Faixa de Endereços**: 192.168.0.0 - 255
