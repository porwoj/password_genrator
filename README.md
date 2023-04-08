# password_generator

simply python docerized app created for generate random password based on two args length and character sets

help is available by:

docker run --rm wojpor/password-generator:v1

and an example, for generate password with: letters,digits,specials character set, and with length:

docker run --rm wojpor/password-generator:v1 -c letters digits specials -l 16
