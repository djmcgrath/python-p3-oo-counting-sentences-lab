#!/usr/bin/env python3

class MyString:

  def __init__(self, value = ""):
    self.value = value

  def is_sentence (self):
    if self.value.endswith("."):
      return True
    else:
      return False
  
  def is_question (self):
    if self.value.endswith("?"):
      return True
    else:
      return False
    
  def is_exclamation (self):
    if self.value.endswith("!"):
      return True
    else:
      return False
    
  @property
  def value (self):
    """Gets value to see if string"""
    return self._value
  
  @value.setter
  def value (self, new_value):
    """Sets value to new value if it is a string"""
    if isinstance(new_value, str):
      self._value = new_value
    else:
      print("The value must be a string.")
    
  def count_sentences (self):
    for punc in ["!", "?"]:
      self.value = self.value.replace(punc, ".")

    sentences = [sent for sent in self.value.split(".") if sent]

    return len(sentences)
