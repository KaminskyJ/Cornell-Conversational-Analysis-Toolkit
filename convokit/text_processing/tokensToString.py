from convokit.transformer import Transformer
from convokit.model import Corpus
from .textProcessor import TextProcessor

class TokensToString(TextProcessor):
	
	def __init__(self, output_field, 
				 token_formatter=lambda x: x['tok'], token_filter=lambda x: True, 
				 input_field='parsed', verbosity=0):
		aux_input = {'token_formatter': token_formatter, 'token_filter': token_filter}
		TextProcessor.__init__(self, self._get_token_string_wrapper, output_field, aux_input,
							  input_field, verbosity)
	
	
	def _get_token_string_wrapper(self, text_entry, aux_input={}):
		return self._get_token_string(text_entry, aux_input['token_formatter'], aux_input['token_filter'])

	def _get_token_string(self, parse, token_formatter=lambda x: x['tok'], token_filter=lambda x: True):
		return '\n'.join(' '.join(token_formatter(tok) for tok in sent['toks'] if token_filter(tok)) for sent in parse)