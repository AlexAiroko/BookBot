import os
import sys
import math

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
	raw_part = text[start:start+page_size]
	num_punctum = -1
	for i, symb in enumerate(raw_part[::-1]):
		if symb in ",.!:;?":
			num_punctum = i
			break
	end = start+page_size-num_punctum
	part = text[start:end]
	
	if end < len(text) and text[end] in ",.!:;?":
		space_ind = part.rindex(' ')
		part = part[:space_ind]
		while part[-1] not in ",.!:;?":
			part = part[:-1]
	
	return part, len(part)


def prepare_book(path: str) -> None:
	with open(path, encoding="utf-8") as f:
		text = f.read()
	
	symb_cnt = 0
	page_cnt = 1

	while symb_cnt < len(text):
		part, ln = _get_part_text(text, symb_cnt, PAGE_SIZE)
		symb_cnt += ln
		book[page_cnt] = part
		page_cnt += 1



prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
