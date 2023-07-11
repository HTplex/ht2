## simple tokenizer
https://huggingface.co/docs/transformers/tokenizer_summary

```
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('t5-small')
output = tokenizer.encode("dujing yan is a wonderful place to live, it's underwater but (0-10__3*)")
print([tokenizer.decoder(x) for x in output])
```
