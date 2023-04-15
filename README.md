# pdfcrack

Şifreli PDF dosyalarının şifreleri kaba kuvvet saldırı ile kırmaya yarayan bir araçtır.

## Gereksinimler

pdfcrack aşağıdaki kütüphaneleri kullanır.

* Colorama
* Pikepdf

## Kurulumu

Projeyi klonlamak için;

```python
git clone https://github.com/thealper2/pdfcrack.git
```
Gerekli kütüphaneleri kurmak için;

```python
python -m pip install -r requirements.txt
```

## Kullanımı

| Parametre | Kullanımı |
| --------- | --------- |
| -f        | File. Kırılacak PDF dosyasını için kullanılır. |
| -w        | Host. Parolaların bulunduğu wordlist dosyasını belirtmek için kullanılır. |

```bash
usage: pdfcrack.py [-h] [-f F] [-w W] 

SSH brute force

options:
  -h, --help  show this help message and exit
  -f          pdf file
  -w          wordlist file
```

## Örnekler

```python
python3 pdfcrack.py -f test.pdf -w rockyou.txt
```
