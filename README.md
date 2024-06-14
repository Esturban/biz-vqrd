## Business vQRd  

> Simple script that to takes your vCard ... on the road 😅

Turn your `.vcf` to a QR code for easy scanning and sharing.  

### Getting Started

Set up is pretty standard. 🐣

1.  Get the project locally
```bash
git clone git@github.com:Esturban/biz-vqrd.git 
cd biz-vqrd
# Here you just copy the vqrd sample so it won't break
cp src/vcard-sample.py src/vcard.py
```

2. Create and initialize virtualenv - `venv`
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements
```

3. Run the code 

```bash
python main.py
```


### Considerations 

- Put your own headshot. lol
- Just create a nice vcf on your phone, send it to yourself, read it as a text file and copy it directly into VCARD.
- Ideally, env would encompass the full .vcf contents in a VCF_BLOB value and then parse it accordingly.
