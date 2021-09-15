def remove_special_characters(txt):
  allowed = [' ', '-', '_']
  return ''.join(t for t in txt if t.isalnum() or t in allowed)
