#!/usr/bin/env python

template_dict = {
    "TPL_ANACONDA_TOKEN": "EwDvNNbo6xnXz99ggD//LSbi0Bs8MNME3AuxAPB7LQiSsFcMZ3EETE1OkAmvSQDTgCjpO6x0izy8i3H+H249f/FI89bfPMvd67RB1YQAnkPj05HWx9zUxyCGaxdSMdw0IKLZBUq2itwSsx6+ltbNhgCAbWxB7vOBpNeIHmk7zv753sSfk5C/cI48SzZyRbfliAMqcfXyj6kM3uhmAVmQ/Li5wkXY7Owhp9oYw1/Lpfl0FZUA5km3jUdCWg/yMQ0rdKtDvm749GASIIKChIdjmSFlfAc8pvKahHfpiL1XO9+NdwflU7AMkg6RYZpDxyM5wt86MdyLyIOxqzhD8a4DNzkpm2u9eGsxx77SxtteNVkDkxkt1xhW5Vw3amdIIKn+/VVR1Oyq8A13ZzLCtiqvrn+lJaWvejpF39fJPBXtvWxBmDJQYOL98nrG8vNwyFw6dQOgMKJEtfmxEH/2gjeJvi/cY8aNUMrVDWF304v9rrbO6Nm9LrM220Tq1/OfSdgqb9hBo7EwyDHZ9kV0yRLcU30LBDOGlBqa9BUq/CQbPFjWLfJuUqpVFKBOpvmBFt9OSP53m45DqcVWSdNBDeCawlpaDHfHJ95fUi+kS04KkmzaBos6vWpyxs2oIylLhi+r3SQYR1jyavG0r14d7SXLa/AU11f+p6eEoiM6Zp3fPIQ=",
    "TPL_GITHUB_TOKEN": "s9VMWQYN93W702bHud7wl29qKJfYIQH5B2d0b2rPU+/ZGW32AO3ichF8kRR5Z2ePJGETw2h20r6GEigUToC4eum9VA9yuLClDyvUP41XYslh0ZFT7RSCuVAl0pyhB9zml6LpnDa4EB2zuo6W/cbnvhvq5MJi9PHP0nSmGKBX/RIN0Yz5kkH6hjo3YqRu6NwftsDyRdpgFSmtDSSOrHRfwzFogg4OLNexGXC5AEgwjjEHH4N+2YCwX0LmZY5tlyxElkj23WGAlp9B3OFNnA68cw1axnNKiNKRL7VmlmykXxplkLz2YxKqovhup9uUlkzmC7aRlgEWrCvMAgaxDtgYf0KDCrYn4HQCmcuxuIgSqY8srLxEiZPuHxfBalTqvEXuehJQTDj9AmKx7v3jEYlAlDLS86sdxKtIpmsb5ReJcJ4aWWRJWcN7TdiRqINIasqYZuxPJqR7eVp1mNhXUq/uxi2RHxcdbt54f7eKz3ZBP9LpmyxcMWa9lrHjyvIz8BerLbkWSBfo8v62VJgG8hhn7JOm0e+5LO7y7vRldcpknVOLvrmsSIp/5T0ybQtka9FNQBV5/fPl3Ty7JMOvpYgrf4llXP1BG8WQWlpCI2Xbj7PM8//qWfnFa63n/dm3Q9+Z1bwftDMEqaLb972t68gl+K9gh2iT3+smHnGztow3NtE=",
    "TPL_PYPI_PASSWORD": "eVqw72IFej1iFYefMNd67CXu82CiLrpten2SYarRsnrn5BIHFIrnNmeZ7ZVBv35oHsfk9rCJZBjwUKlzDKDKi9KX7NqVz2hMMJGxnHrAAdy4fYEPj0sRp9thtfsgRs24Ekmeyo/mqAd/qZOhDEGKJFERdvrTXIe0Gv4imKJDv5ZPdp7uelMGTS7nWRHa2uqKhGtEE8tEKtdsBJh27rjPv4nfyjfg3gsS8cbAL7gPBs5+5yZZo6SVJjpWBrWSIKpPBHqxFx9d6Rt/ebLbVNriUzJoS7lP4KT7CnllgQDY39sm0WT0XD41Z2FsbziZ5u4ede9rGIsJpB3Nls554dvb/saxlnO4fzAEu4tTT4ErRRdJaaAgxkx/CMDTL5ztKlyeh9Pq1qPzhaFDjG5qnE3ES1y8jyQkiZ583JMFvoCyGditFpBxEA7xOHCPpbN6D4U6JamlY9Ol7SlNpgfEH+/dFyOQ73r5skmj8zBbxAFaUK1vtpp7xRJDgxBU3ZRyHPq333Te0sxwikX4GTdBH0jTmWA25BzjgANPda5WI4RgQxNZ4f4GJJm1ldUziVl/SSltUBp5WIx3VjmeNNLRSygXyg/OleLH0pYtQO4fKb2DPo80TAO58Bqu4f0haPuymX7D5xB/L5y+GidJdJSuQ+c49YUNpROlGOJ4WrcCN1yrAT8=",
    "PROJECT_NAME": "gbasis",
    "GITHUB_REPO_NAME": "theochem/gbasis",
    }

import sys
from string import Template

template_fn = sys.argv[1]

with open(template_fn) as fh:
    l = fh.read()

t = Template(l)
s = t.safe_substitute(**template_dict)
with open(".travis.yml", "w") as fh:
    fh.write(
        "#\n# THIS FILE IS AUTOGENERATED. DO NOT EDIT DIRECTLY. CHANGES IN \".travis.yml.tpl\" INSTEAD.\n#\n")
    fh.write(s)