import os

def test(data1, file_name, num_bytes, seek_num):
	try:
		fh = open(os.path.join("/mytestdata/", file_name))
		fh.seek(seek_num)
		data = fh.read(num_bytes)

		if data == data1:
			return True, ""
		else:
			return False, "{} does not match with {}".format(data, data1)

	except Exception as e:
		return False, str(e)
	finally:
		fh.close()

if __name__ == "__main__":
	bl, er = test("data to check/validate", "b.txt", 22, 10)
	print (bl,er)