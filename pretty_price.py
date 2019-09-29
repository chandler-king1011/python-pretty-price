def pretty_price(raw_price, pretty_dec):
    if isinstance(pretty_dec, int):
        pretty_dec = pretty_dec * 0.01
    return(int(raw_price) + pretty_dec)



print(pretty_price(3.20, .95))

print(pretty_price(3.20, 95))