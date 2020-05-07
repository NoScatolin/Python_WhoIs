#!/usr/bin/python
import whois

data = raw_input("Insira a URL alvo: ")
w = whois.whois(data)

print w