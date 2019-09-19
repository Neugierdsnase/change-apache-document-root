# Change Apache Document Root
This is rather hacky and if you found this because you need it, I would guess it won't work without you customizing the script so it suits your system.

## What is does
Apache2's default `DocumentRoot`directory is `/var/www/html`. But me - and probably others too - have more folders than just the `html` folder in `/var/www/`. This script lets you switch between these folders.

## How to use
Clone this repo and adjust the `apache_config_file_path` in `config.py`.

It is probably most convenient to set up a bash function to use this like so:
```bash
chadr() {
  sudo python3 ~/path/to/where/you/cloned/change_apache_document_root/change_doc_root.py "$1"
}
```
or like so in [fish](https://fishshell.com/):
```fish
function chadr
    sudo python3 ~/path/to/where/you/cloned/change_apache_document_root/change_doc_root.py $argv
end
```

When this is set up, swapping between projects this way is a breeze.
