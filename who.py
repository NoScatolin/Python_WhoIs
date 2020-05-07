#!/usr/bin/python
# -*- coding: utf-8 -*-
import whois

host = raw_input("Insira a URL alvo: ")

res = whois.whois(host)

print res



# Função para filtrar resultados

#for x in res.name_servers:
#	print ('Name Servers =>', x)